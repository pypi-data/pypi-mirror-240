import torch
from torch.utils.tensorboard.writer import SummaryWriter
from phi.ddsp.model import DDSP
from os import path
import os
from phi.preprocess import Dataset
from tqdm import tqdm
from phi.ddsp.core import multiscale_fft, safe_log, mean_std_loudness
import soundfile as sf
from einops import rearrange
from phi.ddsp.utils import get_scheduler
import numpy as np

_MODEL_DIR = "models"

def train(model_params, train_params, data_params, device):
    # Check if the directory exists, and create one if not
    if not os.path.exists(_MODEL_DIR):
        os.makedirs(_MODEL_DIR)

    # Define a model and dataset
    model = DDSP(model_params["hidden_size"], 
                 model_params["n_harmonics"],
                 model_params["n_bands"], 
                 data_params["sampling_rate"],
                 model_params["block_size"]).to(device)

    dataset = Dataset(data_params["data_directory"])

    # Make a dataloader
    dataloader = torch.utils.data.DataLoader(
        dataset,
        train_params["batch_size"],
        True,
        drop_last=True,
    )

    # Extract mean/std loudness 
    mean_loudness, std_loudness = mean_std_loudness(dataloader)

    # Define a summary writer 
    writer = SummaryWriter(path.join(_MODEL_DIR, train_params["model_name"]),
                           flush_secs=20)

    # Define an optimizer
    opt = torch.optim.Adam(model.parameters(), lr=train_params["start_lr"])

    # Define a scheduler 
    schedule = get_scheduler(
        len(dataloader),
        train_params["start_lr"],
        train_params["stop_lr"],
        train_params["decay"],
    )

    # Define hyperparameters for training 
    best_loss = float("inf")
    mean_loss = 0
    n_element = 0
    step = 0
    epochs = int(np.ceil(train_params["steps"] / len(dataloader)))

    # Train the model
    for e in tqdm(range(epochs)):
        for s, p, c, l in dataloader:
            s = s.to(device)
            p = p.unsqueeze(-1).to(device)
            c = c.unsqueeze(-1).to(device)
            l = l.unsqueeze(-1).to(device)

            l = (l - mean_loudness) / std_loudness

            y = model(p, c, l).squeeze(-1)

            ori_stft = multiscale_fft(
                s,
                model_params["scales"],
                model_params["overlap"],
            )
            rec_stft = multiscale_fft(
                y,
                model_params["scales"],
                model_params["overlap"],
            )

            loss = 0
            for s_x, s_y in zip(ori_stft, rec_stft):
                lin_loss = (s_x - s_y).abs().mean()
                log_loss = (safe_log(s_x) - safe_log(s_y)).abs().mean()
                loss = loss + lin_loss + log_loss

            opt.zero_grad()
            loss.backward()
            opt.step()

            writer.add_scalar("loss", loss.item(), step)

            step += 1

            n_element += 1
            mean_loss += (loss.item() - mean_loss) / n_element

        if not e % 10:
            writer.add_scalar("lr", schedule(e), e)
            writer.add_scalar("reverb_decay", model.reverb.decay.item(), e)
            writer.add_scalar("reverb_wet", model.reverb.wet.item(), e)
            # scheduler.step()
            if mean_loss < best_loss:
                best_loss = mean_loss
                torch.save(
                    model.state_dict(),
                    path.join(_MODEL_DIR, train_params["model_name"], "state.pth"),
                )

            mean_loss = 0
            n_element = 0

            audio = torch.cat([s, y], -1).reshape(-1).detach().cpu().numpy()

            sf.write(
                path.join(_MODEL_DIR, train_params["model_name"],
                          f"eval_{e:06d}.wav"),
                audio,
                data_params["sampling_rate"],
            )

