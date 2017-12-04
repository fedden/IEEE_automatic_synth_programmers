import numpy as np
import sys
import os
import warnings
from tqdm import tqdm

sys.path.append('utils')

from plugin_feature_extractor import PluginFeatureExtractor
from utility_functions import get_batches, get_stats, display_stats, plot_error, write_wavs
from tqdm import trange

# Granulator
# overriden_parameters = [(2, 1.0), (3, 0.0), (4, 1.0)]

# FM
overriden_parameters = []

data_folder = "data/fm/"

desired_features = [0, 1, 6]
desired_features.extend([i for i in range(8, 21)])

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    extractor = PluginFeatureExtractor(midi_note=24, note_length_secs=0.4,
                                       desired_features=desired_features,
                                       overriden_parameters=overriden_parameters,
                                       render_length_secs=0.7,
                                       pickle_path="utils/normalisers",
                                       warning_mode="ignore",
                                       normalise_audio=False)
    # Granulator
    # path = "/home/tollie/Development/vsts/synths/granulator/Builds/build-granulator-Desktop-Debug/build/debug/granulator.so"

    path = "/home/tollie/Downloads/synths/FMSynth/Builds/LinuxMakefile/build/FMSynthesiser.so"
    extractor.load_plugin(path)

    all_patches = np.load(data_folder + "all_patches.npy")
    all_x = []
    all_y = []

    step = 3
    chunk_size = 4

    start = int(step * float(len(all_patches)) / chunk_size)
    end = int((1 + step) * float(len(all_patches)) / chunk_size)
    print "\n" * 4
    print start
    print end
    print "\n" * 4
    for i in tqdm(range(start, end), desc="Creating dataset"):
        parameters = all_patches[i]
        patch = extractor.partial_patch_to_patch(parameters)
        patch = extractor.add_patch_indices(patch)
        features = extractor.get_features_from_patch(patch)
        all_x += [features]
        all_y += [parameters]

    np.save(data_folder + str(step) + "_all_x.npy", np.array(all_x))
    np.save(data_folder + str(step) + "_all_y.npy", np.array(all_y))
    np.save(data_folder + "overriden_parameters.npy", np.array(overriden_parameters))
    np.save(data_folder + "desired_features.npy", np.array(desired_features))
