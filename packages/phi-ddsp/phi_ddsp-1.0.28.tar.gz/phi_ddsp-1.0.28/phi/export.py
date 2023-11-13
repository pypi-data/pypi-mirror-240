import torch
import yaml
from os import path, makedirs 
from phi.ddsp.model import DDSP
from phi.preprocess import Dataset
from phi.ddsp.core import mean_std_loudness
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


def export(config, model_directory, output_directory):
    # Check if the directory exists, and create one if not
    if not path.exists(output_directory):
        makedirs(path.join(output_directory))
        
    if not path.exists(path.join(output_directory, config["train"]["model_name"])):
        makedirs(path.join(output_directory, config["train"]["model_name"]))

    ddsp = DDSP(config["model"]["hidden_size"], 
                 config["model"]["n_harmonics"],
                 config["model"]["n_bands"], 
                 config["data"]["sampling_rate"],
                 config["model"]["block_size"])

    state = ddsp.state_dict()
    pretrained = torch.load(path.join(model_directory, config["train"]["model_name"], "state.pth"), map_location="cpu")
    state.update(pretrained)
    ddsp.load_state_dict(state)

    name = path.basename(path.normpath(output_directory))

    # TODO: This should be abstracted from training such that it's not called here
    dataset = Dataset(config["data"]["data_directory"])

    # Make a dataloader
    dataloader = torch.utils.data.DataLoader(
        dataset,
        config["train"]["batch_size"],
        True,
        drop_last=True,
    )

    # Extract mean/std loudness 
    mean_loudness, std_loudness = mean_std_loudness(dataloader)

    scripted_model = torch.jit.script(
        ScriptDDSP(
            ddsp,
            mean_loudness,
            std_loudness,
            False,
        ))

    torch.jit.save(
        scripted_model,
        path.join(output_directory, config["train"]["model_name"], f"ddsp_{name}_pretrained.ts"),
    )

    impulse = ddsp.reverb.build_impulse().reshape(-1).detach().numpy()

    sf.write(
        path.join(output_directory, config["train"]["model_name"], f"ddsp_{name}_impulse.wav"),
        impulse,
        config["data"]["sampling_rate"],
    )

    with open(
            path.join(output_directory, config["train"]["model_name"], f"ddsp_{name}_config.yaml"),
            "w",
    ) as config_out:
        yaml.safe_dump(config, config_out)
