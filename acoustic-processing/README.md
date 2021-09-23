# Acoustic Data Processing
IoT sensors are frequently equiped with microphones which can capture acoustic signals from the environment. These signals contain a lot of information which can be extracted by combining digital signal processing and machine learning.

Here we will describe the steps necessary to work with acoustic signals and demonstrate the application of acoustic processing in two applications: 1) ecosystems monitoring for conservation and 2) traffic monitoring.

## Data Processing

Before describing the applications, we will go through general steps in working with audio signals. These steps are descibed in the notebook `audio-processing.ipynb`. To be able to run the notebook,
do the following

1. Clone this repository and cd into it
1. Create a [virtual environment](https://docs.python.org/3/tutorial/venv.html)
`python3 -m venv audio-env`
1. Activate it
On Linux
`source audio-env/bin/activate`
On Windows
`audio-env\Scripts\activate.bat`
1. Update pip `pip install --upgrade pip`
1. Install the requirements
`pip install -r requirements.txt`


Once this is done launch the notebook.


## Acoustic Ecosytstem Monitoring


## Acoustic Road Traffic Monotoring
This work will use a data set from the [Fraunhofer Institute for Digital Media Technology](https://www.idmt.fraunhofer.de/en/publications/traffic.html) of audio recordings of vehicles driving along a road under different conditions. The dataset contains four vehicle types namely bus, car, motorcycle and truck.

We will use this dataset to train a neural network to classify vehicles based on audio recordings and deploy it on a system  based on the Raspberry Pi and a cheap USB microphone to perform classification in the field.


### Get the data
Here we are using a version of the dataset that has been converted to mono and `mp3` to save space. The dataset has been uploaded [here](https://drive.google.com/file/d/1-wvwEL766FvvpgJYi_adrxAyu2rHW77A/view?usp=sharing). Download the dataset and unzip the the files into the data folder.

To process the entire dataset and generate the melspectrograms, run the following command

```
python parallel_feature_compute.py -a data/audio-16kHz-mono-mp3/ -f data/melspec-16kHz-mp3/ -e mp3
```

This program will exploit multiple cores on your machine if they exist and use the parameters specified in `files/parameters.ini` to generate the melspectrograms.

We have prepared melspectrograms for download [here](https://drive.google.com/file/d/1ibw9jKKqx8lDWEPyOEIGqmJkXqMkvew1/view?usp=sharing) using the parameters listed in `files/parameters.ini`. Download these melspectrograms and unzip them in the data folder to produce the folder `melspec-16kHz-mp3`. Once this is done, the file structure should then look as shown below

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
