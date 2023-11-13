import librosa as li
from phi.ddsp.core import extract_loudness, extract_pitch, extract_centroid
import numpy as np
import pathlib
from os import makedirs, path
from tqdm import tqdm
import torch

class Dataset(torch.utils.data.Dataset):

    def __init__(self, out_dir):
        super().__init__()
        self.signals = np.load(path.join(out_dir, "signals.npy"))
        self.pitchs = np.load(path.join(out_dir, "pitchs.npy"))
        self.centroids = np.load(path.join(out_dir, "centroids.npy"))
        self.loudness = np.load(path.join(out_dir, "loudness.npy"))

    def __len__(self):
        return self.signals.shape[0]

    def __getitem__(self, idx):
        s = torch.from_numpy(self.signals[idx])
        p = torch.from_numpy(self.pitchs[idx])
        c = torch.from_numpy(self.centroids[idx])
        l = torch.from_numpy(self.loudness[idx])
        return s, p, c, l

def _get_files(data_location, extension):
    return list(pathlib.Path(data_location).rglob(f"*.{extension}"))

def _preprocess_file(f, sampling_rate, block_size, signal_length):
    x, _ = li.load(f)
    N = (signal_length - len(x) % signal_length) % signal_length
    x = np.pad(x, (0, N))

    pitch = extract_pitch(x, sampling_rate, block_size)
    centroid = extract_centroid(x, sampling_rate, block_size)
    loudness = extract_loudness(x, block_size)

    x = x.reshape(-1, signal_length)
    pitch = pitch.reshape(x.shape[0], -1)
    centroid = centroid.reshape(x.shape[0], -1)
    loudness = loudness.reshape(x.shape[0], -1)

    return x, pitch, centroid, loudness

def preprocess(config):
    # Parse the JSON response into a Python object (dictionary)
    files = _get_files(config["data"]["audio_directory"],
                       config["data"]["extension"])
    pb = tqdm(files)

    signals = []
    pitchs = []
    centroids = []
    loudness = []

    for f in pb:
        print("Processing file: ", str(f))
        pb.set_description(str(f))
        x, p, c, l = _preprocess_file(f, config["data"]["sampling_rate"],
                                config["model"]["block_size"],
                                config["model"]["signal_length"])
        signals.append(x)
        pitchs.append(p)
        centroids.append(c)
        loudness.append(l)

    signals = np.concatenate(signals, 0).astype(np.float32)
    pitchs = np.concatenate(pitchs, 0).astype(np.float32)
    centroids = np.concatenate(centroids, 0).astype(np.float32)
    loudness = np.concatenate(loudness, 0).astype(np.float32)

    out_dir = config["data"]["data_directory"]
    makedirs(out_dir, exist_ok=True)

    np.save(path.join(out_dir, "signals.npy"), signals)
    np.save(path.join(out_dir, "pitchs.npy"), pitchs)
    np.save(path.join(out_dir, "centroids.npy"), centroids)
    np.save(path.join(out_dir, "loudness.npy"), loudness)

    
