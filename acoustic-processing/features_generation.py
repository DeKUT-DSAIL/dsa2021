import os
import random
import librosa
import numpy as np
import configparser
import matplotlib.pyplot as plt
import audio_noise_separation as an


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
    
    
def features_extraction(audio,
                         nfft,
                         hop_len,
                         noise_dir,
                         sampling_rate,
                         duration,
                         win_length,
                         hop_length,
                         num_mels):
    
    """Returns a melspectrogram of an audio
    Args:
        audio: a numpy array of audio samples
        noise_dir: directory with noise samples for padding
        sampling_rate: audio sampling rate
        duration: minimum duration of files
        nfft: FFT length
        win_length: window length
        hop_length: overlap between adjascent frames
        num_mels: number of melspectrogram channels
        melspectrogram_dir: directory to save spectrograms
    """
      
    #signal, _ = an.get_audio_noise(audio, nfft, hop_len)

    signal = pad_audio(audio, duration, sampling_rate, noise_dir)

    feature = librosa.feature.melspectrogram(signal,
                                                    sr=sampling_rate,
                                                    n_fft=nfft,
                                                    hop_length=hop_length,
                                                    win_length=win_length,
                                                    window='hamming',
                                                    n_mels=num_mels)
    
    return feature
