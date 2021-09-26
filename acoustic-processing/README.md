# Acoustic Data Processing
IoT systems are frequently equiped with microphones which can capture acoustic signals from the environment. These signals contain a lot of information which can be extracted by combining digital signal processing and machine learning.

Here we will describe the steps necessary to work with acoustic signals and demonstrate the application of acoustic processing in two applications: 1) ecosystems monitoring for conservation and 2) traffic monitoring.

## Data Processing

Before describing the applications, we will go through general steps in working with audio signals. These steps are descibed in the notebook `audio-processing.ipynb`. Activate `iot-env` created earlier and launch the notebook.



## Acoustic Ecosytstem Monitoring
Ecosystems contain vast amounts of acoustic data that tell a lot about what is happening in them. In this task, we will demonstrate how we can automatically classify birds from their vocalizations. We will use acoustic data from [Xeno-canto](https://www.xeno-canto.org/) to train baseline models for acoustic classification of birds

## Acoustic Road Traffic Monotoring
This work will use a data set from the [Fraunhofer Institute for Digital Media Technology](https://www.idmt.fraunhofer.de/en/publications/traffic.html) of audio recordings of vehicles driving along a road under different conditions. The dataset contains four vehicle types namely bus, car, motorcycle and truck.

We will use this dataset to train a neural network to classify vehicles based on audio recordings and deploy it on a system  based on the Raspberry Pi and a cheap USB microphone to perform classification in the field.


### Get the data
Ensure you have downloaded and unpacked the data as descibed [here](../README.md) and that the data directory looks as shown below.

```
data
├── audio-16kHz-mono-mp3
│   ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_10077440_SE_CH34-BG.mp3
│   ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_10173440_SE_CH34-BG.mp3
...
├── melspec-16kHz-mp3
│   ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_10077440_SE_CH34-BG.npy
│   ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_10173440_SE_CH34-BG.npy
```




### Run the notebook
The file `acoustic-traffic-monitoring.ipynb` shows the steps used to train the models and test them.


### [For later] New Melspectrograms
To process the entire dataset and generate new melspectrograms with new parameters, run the following command

```
python parallel_feature_compute.py -a data/audio-16kHz-mono-mp3/ -f data/melspec-16kHz-mp3/ -e mp3
```

This program will exploit multiple cores on your machine if they exist and use the parameters specified in `files/parameters.ini` to generate the melspectrograms.
