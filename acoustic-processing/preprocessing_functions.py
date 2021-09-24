#import necessary libraries
import numpy as np


# fmean = np.load('fmean.npy')
# fstd = np.load('fstd.npy')


# def compute_feature_mean_std(feature):
#     """Compute the mean and standard deviation of all the feature
#     Args:
#         feature: melspectrogram of an audio
#     Returns:
#         mean: mean of all channels
#         std: standard deviation of all channels
#     """

#     feature = np.log(feature + 1e-8)
#     feature = feature.T

#     return np.mean(feature, axis=0), np.std(feature, axis=0)


def all_summary_features(feature, num_frame, fmean, fstd):
    """Splits melspectrograms into chunks and and compute
    the mean and standard deviation of frequency channels of the chunks

    Args: feature- melspectrogram
          num_fram- number of frames 
    """

#     fmean, fstd = compute_feature_mean_std(feature)

    feature = np.log(feature + 1e-8)

    feature = ((feature.T - fmean) /
                   (fstd + 1e-8)).T

    features = []

    if feature.shape[1] > 2 * num_frame + 1:

        for indx in range(num_frame, feature.shape[1] - num_frame - 1, num_frame):

            current_feature = feature[:, indx - num_frame: indx + num_frame + 1]


            features.append(np.concatenate((np.mean(current_feature, axis=1),
                                            np.std(current_feature, axis=1))))


    return np.array(features)
