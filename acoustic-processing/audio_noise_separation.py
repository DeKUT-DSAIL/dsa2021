#import necessary libraries
import numpy as np
import librosa
from scipy.ndimage import binary_dilation, binary_erosion


#These functions get the indices corresponding to audio and noise in a file

def compute_audio_mask(norm_specgram, hop_len, category='audio'):
    """ Compute the section of signal corresponding to audio or noise
    This follows the approach described in
    Sprengel, E., Jaggi, M., Kilcher, Y., & Hofmann, T. (2016).
    Audio based bird species identification using deep learning techniques
    Args:
        norm_specgram: input spectrogram with values in range [0,1]
        hop_len: hop length used to generate the spectrogram
        category: whether 'audio' or 'noise'
    Returns:
        mask: the mask of samples belonging to 'category'
    Raises: ValueError if the category is not known
    """

    if category == 'audio':
        threshold = 3
    elif category == 'noise':
        threshold = 2.5
    else:
        raise ValueError('Unknown category')

    col_mask = norm_specgram > threshold * np.median(norm_specgram, axis=0)
    row_mask = norm_specgram.T > threshold * np.median(norm_specgram, axis=1)
    row_mask  = row_mask.T
    mask = col_mask & row_mask

    # erosion
    be_mask = binary_erosion(mask, np.ones((4, 4)))

    # dilation
    bd_be_mask = binary_dilation(be_mask, np.ones((4, 4)))

    bd_be_mask = bd_be_mask.astype(int)
    selected_col = np.max(bd_be_mask, axis=0)
    bd_sel_col = binary_dilation(selected_col[:, None], np.ones((4, 1)))
    bd2_sel_col = binary_dilation(bd_sel_col, np.ones((4, 1)))


    # translate to audio samples
    selection_mtx = np.ones((norm_specgram.shape[1], hop_len)) * selected_col[:, None]

    audio_indx = selection_mtx.flatten().astype(bool)

    if category == 'audio':
        return audio_indx
    else:
        return ~audio_indx



def get_audio_noise(audio_array, nfft, hop_len):
    """ Get both the signal and noise
    Args:
        audio_array: an array of audio
        nfft: FFT length
        hop_len: hop length
    Returns:
        signal and noise
    """
    
    specgram = np.abs(librosa.stft(audio_array, n_fft=nfft, hop_length=hop_len))
    specgram_norm = specgram / (specgram.max() + 1e-8)

    audio_indx = compute_audio_mask(specgram_norm, hop_len)[:len(audio_array)]
    noise_indx = compute_audio_mask(specgram_norm, hop_len, 'noise')[:len(audio_array)]


    return audio_array[audio_indx], audio_array[noise_indx]