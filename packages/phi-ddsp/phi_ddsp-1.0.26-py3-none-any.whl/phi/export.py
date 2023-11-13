import torch
import yaml
import os
from effortless_config import Config
from os import path, makedirs, system
from phi.ddsp.model import DDSP
import soundfile as sf

torch.set_grad_enabled(False)

class ScriptDDSP(torch.nn.Module):

    def __init__(self, ddsp, mean_loudness, std_loudness, realtime):
        super().__init__()
        self.ddsp = ddsp
        self.ddsp.gru.flatten_parameters()

        self.register_buffer("mean_loudness", torch.tensor(mean_loudness))
        self.register_buffer("std_loudness", torch.tensor(std_loudness))
        self.realtime = realtime

    def forward(self, pitch, centroid, loudness):
        loudness = (loudness - self.mean_loudness) / self.std_loudness
        if self.realtime:
            pitch = pitch[:, ::self.ddsp.block_size]
            loudness = loudness[:, ::self.ddsp.block_size]
            centroid = centroid[:, ::self.ddsp.block_size]
            return self.ddsp.realtime_forward(pitch, centroid, loudness)
        else:
            return self.ddsp(pitch, centroid, loudness)


def export(config, output_directory, device):
    # Check if the directory exists, and create one if not
    if not path.exists(output_directory):
        makedirs(output_directory)

    ddsp = DDSP(config["model"]["hidden_size"], 
                 config["model"]["n_harmonics"],
                 config["model"]["n_bands"], 
                 config["data"]["sampling_rate"],
                 config["model"]["block_size"]).to(device)

    state = ddsp.state_dict()
    pretrained = torch.load(path.join(output_directory, "state.pth"), map_location="cpu")
    state.update(pretrained)
    ddsp.load_state_dict(state)

    name = path.basename(path.normpath(output_directory))

    scripted_model = torch.jit.script(
        ScriptDDSP(
            ddsp,
            config["data"]["mean_loudness"],
            config["data"]["std_loudness"],
            False,
        ))
    torch.jit.save(
        scripted_model,
        path.join(config["train"]["model_name"], f"ddsp_{name}_pretrained.ts"),
    )

    impulse = ddsp.reverb.build_impulse().reshape(-1).numpy()
    sf.write(
        path.join(config["train"]["model_name"], f"ddsp_{name}_impulse.wav"),
        impulse,
        config["data"]["sampling_rate"],
    )

    with open(
            path.join(config["train"]["model_name"], f"ddsp_{name}_config.yaml"),
            "w",
    ) as config_out:
        yaml.safe_dump(config, config_out)
