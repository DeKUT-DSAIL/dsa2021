import os
import random
import librosa
import numpy as np
import configparser
import matplotlib.pyplot as plt
import preprocessing_functions as pf


def pad_audio(signal, duration, sampling_rate, noise_dir):
    """ Pad signal if necessary to ensure it is at least duration seconds long
    Args:
        signal: the signal to be padded
        duration: the minimum duration
        sampling_rate: the sampling rate
        noise_dir: the noise directory
    Returns:
        the original signal or a signal padded to duration
    """
    
    audio_duration = len(signal) / sampling_rate
    noise_files = os.listdir(noise_dir)
    if audio_duration >= duration:
        return signal
    else:
#         print(len(signal) / sampling_rate)
        filename = random.choice(noise_files)
        noise_signal, _ = librosa.load(os.path.join(noise_dir, filename),
                                      sr=sampling_rate)
        while (len(signal) / sampling_rate) < duration:
            signal = np.concatenate((signal, noise_signal))
        #print(len(signal) / sampling_rate)  
        return signal[:int(duration * sampling_rate) + 1]
    
    
def features_extraction(audio_array,
                         nfft,
                         hop_len,
                         noise_dir,
                         sampling_rate,
                         duration,
                         win_length,
                         hop_length,
                         num_mels,
                         num_frame):
    
    """Compute features for all files in the list
    Args:
        audio_dir: directory containig audio
        name: name to save the melspectrogram with
        species: name of the subdirectory containing a given species' recordings
        file: name of the recording
        noise_dir: directory with noise samples for padding
        sampling_rate: audio sampling rate
        duration: minimum duration of files
        nfft: FFT length
        win_length: window length
        hop_length: overlap between adjascent frames
        num_mel: number of melspectrogram channels
        melspectrogram_dir: directory to save spectrograms
    """
      
    #signal, _ = pf.get_audio_noise(audio_array, nfft, hop_len)

    #signal = pad_audio(audio, duration, sampling_rate, noise_dir)

    features = librosa.feature.melspectrogram(audio_array,
                                                    sr=sampling_rate,
                                                    n_fft=nfft,
                                                    hop_length=hop_length,
                                                    win_length=win_length,
                                                    window='hamming',
                                                    n_mels=num_mels)

    fmean = np.mean(features, axis=1)
    fstd = np.std(features, axis=1)

    features = np.log(features + 1e-8)

    features = ((features.T - fmean) /
                       (fstd + 1e-8)).T

    print(features.shape)
    features_list = []
    if features.shape[1] > 2 * num_frame + 1:

        for indx in range(num_frame, features.shape[1] - num_frame - 1, num_frame):

            current_feature = features[:, indx - num_frame: indx + num_frame + 1]


            features_list.append(np.concatenate((np.mean(current_feature, axis=1),
                                            np.std(current_feature, axis=1))))
    print(len(features_list))

    return np.array(features_list)