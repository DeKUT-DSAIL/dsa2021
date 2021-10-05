# IoT Data Processing - DSA 2021

This repo contains material to be used for the DSAIL session at DSA 2021. During the session we will discuss the acquisition and processing of data from internet of things (IoT) devices. In particular we will focus on:
* Anomaly detection for time series data
* Acoustic data processing
* Camera trap image processing

The introductory slides for the session are [here](https://docs.google.com/presentation/d/1YEe4n4gkYo-EjgHpaq--zeufmJvlE1FsUclJfDsqnqU/edit?usp=sharing)

## Session Preparation

### Software Environment
 To be able to run the notebooks in this session, do the following

1. Clone this repository and cd into it
1. Create a [virtual environment](https://docs.python.org/3/tutorial/venv.html)
On Linux `python3 -m venv iot-env` or On Windows `python -m venv iot-env`
1. Activate it
On Linux
`source iot-env/bin/activate`
On Windows
`iot-env\Scripts\activate.bat`
1. Update pip `pip install --upgrade pip`
1. Install the requirements
`pip install -r requirements.txt`


### Data
For the acoustic processing session, download the following data
* [Birds melspectrograms](https://drive.google.com/file/d/1bVf7IreZDy0gPxYah8_4j0KIfEhe_5M3/view?usp=sharing)
* [Audio traffic recordings](https://drive.google.com/file/d/1-wvwEL766FvvpgJYi_adrxAyu2rHW77A/view?usp=sharing)
* [Melspectrograms from the recordings](https://drive.google.com/file/d/1bVf7IreZDy0gPxYah8_4j0KIfEhe_5M3/view?usp=sharing)

Extract the audio and melspectrogam folders within the data subfolder in the acoustic-processing folder. The directory structure should look as follows
```
├── acoustic-processing
│   ├── audio-samples
|   |   ├── bird-samples
|   |   |   ├── grey-backed camaroptera.wav
|   |   |   ├── hartlaub's turaco.wav
|   |   ├── birds-test-data
|   |   |   ├── grey-backed camaroptera
|   |   |   |   ├── grey-backed camaroptera22.mp3
|   |   |   |   ├── grey-backed camaroptera32.mp3
|   |   |   ├── hartlaub's turaco
|   |   |   |   ├── hartlaub's turaco4.mp3
|   |   |   |   ├── hartlaub's turaco9.mp3
|   |   |   ├── tropical boubou
|   |   |   |   ├── tropical boubou9.mp3
|   |   |   |   ├── tropical boubou21.mp3
│   │   ├── examples
|   |   |   ├── piano-C6.wav
|   |   ├── noise
|   |   |   ├── grey-backed camaroptera0.wav
|   |   |   ├── grey-backed camaroptera6.wav
│   │   ├── vehicle-samples
│   │       ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_1272258_M_D_BR_ME_CH12.mp3
│   │       ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_1272258_M_D_BR_SE_CH34.mp3
│   ├── data
│   │   ├── audio-16kHz-mono-mp3
│   │   │   ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_10077440_SE_CH34-BG.npy
│   │   │   ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_10173440_SE_CH34-BG.npy
|   |   ├── birds-melspectrograms
|   |   |   ├── grey-backed camaroptera0.npy
|   |   |   ├── grey-backed camaroptera1.npy
│   │   ├── melspec-16kHz-mp3
│   │   │   ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_10077440_SE_CH34-BG.npy
│   │   │   ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_10173440_SE_CH34-BG.npy
│   ├── files
│   │   │   ├── eusipco_2021_test.csv
│   │   │   ├── eusipco_2021_train.csv
│   ├── acoustic-traffic-monitoring.ipynb
│   ├── acoustic-ecosystems-monitoring.ipynb
│   ├── audio_noise_separation.py
│   ├── audio-processing.ipynb
│   ├── features_generation.py
│   ├── parallel_feature_compute.py
│   ├── README.md
│   ├── utility_functions.py
```
## Acoustic data processing
[Details here](acoustic-processing/)

## Anomaly detection

### What we intended to handle during these session

## :point_right: Anomaly detection using :link: [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)

#### :one: Materials provided
- Presentation slides
- A water-level sample dataset (tailored for this Anomaly detection piece)
- Rainfall dataset from TAHMO
- River Muringato daily water level figures dataset from 11th Feb 2021 to 25th Sept 2021

#### :two: How to run the notebook _ setup

OPTION 1: :arrow_forward: Python_environment
- You can use the environment set up for acoustic processing

OPTION 2: :arrow_forward: Google collab
Link :link:[Anomaly_Detection_Notebook_Link](https://colab.research.google.com/drive/1bwZrGOH0iHLxnymcJF7hNrlXdFgVsi1Q?usp=sharing)

:arrow_right: Loading up the dataset

- Click on the files icon on the side bar shown below.

![cover page image](/anomaly-detection/assets/img/file1.PNG)

- Click on the upload button aned you will be prompted to upload a file.
- Select the three datasets from the repo you cloned (in the data folder) and upload it.

![cover page image](/anomaly-detection/assets/img/file2.PNG)

- Right click on the dataset samples to copy the path.
- Paste it on the *dataset import slots* cell of the notebook

![cover page image](/anomaly-detection/assets/img/file3.PNG)

- Run the notebook :battery: **green light**

#### :three: water-level data visualization webapp.
- The following is a link to the water level data webapp.

Link :link:[waterlevel_webapp](https://water-monitoring-258811.wl.r.appspot.com)

## Camera trap image processing
We will go through the notebook in the `cameratrap-data-analysis` folder where we will use a pretrained model to classify the animals in our dataset.
