"""
Copyright 2018 - 2020 Ciira wa Maina, DeKUT DSAIL

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import json
import os
import random
import math
import scipy.ndimage
import datetime
import numpy as np
import pandas as pd

import tensorflow as tf
from tqdm import tqdm

def generate_spectrogram_window(melspectrogram,
                                duration=1,
                                sampling_frequency=16000,
                                hop_size=256):
    """Generate a window of given duration centered at an active frame
    Args:
        melspectrogram: input melspectrogram
        duration: duration of window
        sampling_frequency: sampling frequency of audio
        hop_size: hop size per frame used to generate spectrogram
    Returns:
        spectrogram_window: the frames corresponding to the window
    """
    frame_rate = hop_size / sampling_frequency
    min_frame_number = math.floor((0.5 * duration) / frame_rate)

    index = random.randint(min_frame_number, melspectrogram.shape[1] - min_frame_number - 1)


    return melspectrogram[:, index - min_frame_number:index + min_frame_number]


def generate_all_spectrogram_windows(melspectrogram,
                                     duration=1,
                                     sampling_frequency=16000,
                                     hop_size=256):
    """Generate all  windows from a melspectrogram with a single frame shift
    Args:
        melspectrogram: input spectrogram
        duration: duration of window
        sampling_frequency: sampling frequency of audio
        hop_size: hop size per frame used to generate spectrogram
    Returns:
        melspectrogram_windows: a multidimensional array with all non-overlaping windows
    """
    frame_rate = hop_size / sampling_frequency
    min_frame_number = math.floor((0.5 * duration) / frame_rate)

    windows = []
    for index in range(min_frame_number,
                       melspectrogram.shape[1] - min_frame_number - 1,
                       1):
        current_window = melspectrogram[:, index - min_frame_number:index + min_frame_number]
        windows.append(current_window.reshape(current_window.shape[0], current_window.shape[1], 1))
    return windows



def data_generator_windowed(melspectrogram_dir,
                            filelist,
                            annotation_dict,
                            batch_size,
                            shuffle=False,
                            duration=1,
                            sampling_frequency=16000,
                            hop_size=256):
    """ A generator for use in training the neural networks

    Args:
        melspectrogram_dir: directory where spectrograms are stored
        filelist: files containing the training spectrograms
        annotation_dict: a dictionary with the labels
        batch_size: batch size for training
        duration: duration of window to serve as training input
        sampling_frequency: sampling frequency of audio
        hop_size: hop size per frame used to generate spectrogram

    Yields:
        a tuple containing features and their labels
    """
    if shuffle:
        random.shuffle(filelist)
    batch_num = 0
    num_generator_calls = int(len(filelist) / batch_size)
    frame_rate = hop_size / sampling_frequency
    min_frame_number = math.floor((0.5 * duration) / frame_rate)

    while True:
        features = []
        labels = []
        for b in range(batch_size):
            melspec = np.load(os.path.join(melspectrogram_dir,
                                           filelist[batch_size * batch_num + b]))
            normed_mel = ((melspec.T - np.mean(melspec, 1)) / np.std(melspec, 1)).T


            if normed_mel.shape[1] > 2 * min_frame_number:
                data = generate_spectrogram_window(normed_mel,
                                                   duration,
                                                   sampling_frequency,
                                                   hop_size)

                if not np.isnan(data).any():

                    #features.append(data.reshape(data.shape[0], data.shape[1], 1))
                    features.append(np.stack((data,) * 3, axis=-1))
                    labels.append(annotation_dict[filelist[batch_size * batch_num + b]])

        batch_num += 1
        batch_num %= num_generator_calls

        yield np.array(features).astype('float32'), tf.one_hot(labels, len(set(annotation_dict.values())))
