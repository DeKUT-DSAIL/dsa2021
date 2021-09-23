"""
Copyright 2021 Ciira wa Maina, DeKUT DSAIL

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
import os
import argparse
import configparser
import time
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

from multiprocessing import Pool
from multiprocessing import cpu_count
from tqdm import tqdm


def divide_tasks(filelist, files_per_process):
    # source https://www.pyimagesearch.com/2019/09/09/multiprocessing-with-opencv-and-python/
    # loop over the list in chunks
    for indx in range(0, len(filelist), files_per_process):
        # yield the chunk to the calling function
        yield filelist[indx: indx + files_per_process]


def compute_feature(filename,
                    audio_dir,
                    feature_dir,
                    audio_ext,
                    sampling_rate,
                    nfft,
                    hop_len,
                    win_len,
                    num_mels):

    try:
        signal, _ = librosa.load(os.path.join(audio_dir, filename),
                                 sampling_rate)
        file_features = librosa.feature.melspectrogram(signal,
                                                       sr=sampling_rate,
                                                       n_fft=nfft,
                                                       hop_length=hop_len,
                                                       win_length=win_len,
                                                       window='hamming',
                                                       n_mels=num_mels)
        features_db = librosa.power_to_db(file_features, ref=np.max)
        np.save(os.path.join(feature_dir, filename.replace(audio_ext, 'npy')),
                             features_db)


    except (FileNotFoundError, EOFError) as e:
        print('{} not found'.format(filename))

def process_files(payload):

    for filename in payload['filelist']:
        compute_feature(filename,
                        payload['audio_dir'],
                        payload['feature_dir'],
                        payload['audio_ext'],
                        payload['sampling_rate'],
                        payload['nfft'],
                        payload['hop_len'],
                        payload['win_len'],
                        payload['num_mels'])




def main():
    """ Compute spectrograms or melspectograms for audio files"""

    parser = argparse.ArgumentParser()
    parser.add_argument('--audio-dir', '-a', type=str,
                        help="Directory containing audio files",
                        required=True)
    parser.add_argument('--feature-dir', '-f', type=str,
                        help="Directory to store spectrograms",
                        required=True)
    parser.add_argument('--ext', '-e', type=str,
                        help="Extension (mp3, wav, ...)",
                        required=True)
    args = parser.parse_args()


    # Get parameters from configuration file
    config = configparser.ConfigParser()
    config.read('parameters.ini')


    win_len_ms = int(config['audio']['win_len_ms'])
    overlap = float(config['audio']['overlap'])
    sampling_rate = int(config['audio']['sampling_rate'])
    num_mels = int(config['audio']['num_mel'])

    # Derive audio processing values
    win_len = int((win_len_ms * sampling_rate) / 1000)
    hop_len = int(win_len * (1 - overlap))
    nfft = int(2 ** np.ceil(np.log2(win_len)))

    # audio data
    filenames = os.listdir(args.audio_dir)
    num_files = len(filenames)

    already_processed = os.listdir(args.feature_dir)
    already_processed = [f.replace('jpg', args.ext) for f in already_processed]

    filenames = list(set(filenames) - set(already_processed))


    n_cpu = cpu_count()
    files_per_process = int(np.ceil(len(filenames) / n_cpu))
    divided_file_list = list(divide_tasks(filenames,
                                          files_per_process))

    payloads = []

    for files in divided_file_list:
        data = {}
        data['filelist'] = files
        data['audio_dir'] = args.audio_dir
        data['feature_dir'] = args.feature_dir
        data['audio_ext'] = args.ext
        data['sampling_rate'] = sampling_rate
        data['nfft'] = nfft
        data['hop_len'] = hop_len
        data['win_len'] = win_len
        data['num_mels'] = num_mels

        payloads.append(data)


    print('Generating features ...')
    start_time = time.perf_counter()


    pool = Pool(processes=n_cpu)
    pool.map(process_files, payloads)
    # close the pool and wait for all processes to finish

    pool.close()
    pool.join()




    stop_time = time.perf_counter()
    time_taken = stop_time - start_time
    print(('Features generated in {:.2f} minutes,'
           '{:.2f} seconds per file').format(time_taken / 60, time_taken / num_files))
    print('Saving...')



if __name__ == '__main__':
    main()
