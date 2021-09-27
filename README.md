# IoT Data Processing - DSA 2021

This repo contains material to be used for the DSAIL session at DSA 2021. During the session we will discuss the acquisition and processing of data from internet of things (IoT) devices. In particular we will focus on:
* Acoustic data processing
* Anomaly detection for time series data
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
* [Audio traffic recordings](https://drive.google.com/file/d/1-wvwEL766FvvpgJYi_adrxAyu2rHW77A/view?usp=sharing)
* [Melspectrograms from the recordings](https://drive.google.com/file/d/1ibw9jKKqx8lDWEPyOEIGqmJkXqMkvew1/view?usp=sharing)
* [Birds melspectrograms](https://drive.google.com/file/d/1BATJ6R6yTpEArAdD61l9i7u1WiTvf5cg/view?usp=sharing)

Extract the audio and melspectrogam folders within the data subfolder in the acoustic-processing folder. The directory structure should look as follows
```
├── acoustic-processing
│   ├── acoustic-traffic-monitoring.ipynb
│   ├── audio-processing.ipynb
│   ├── audio-samples
│   │   ├── examples
│   │   │   └── piano-C6.wav
│   │   └── vehicle-samples
│   │       ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_1272258_M_D_BR_ME_CH12.mp3
│   │       ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_1272258_M_D_BR_SE_CH34.mp3
│   ├── data
│   │   ├── melspec-16kHz-mp3
│   │   │   ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_10077440_SE_CH34-BG.npy
│   │   │   ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_10173440_SE_CH34-BG.npy
│   │   ├── audio-16kHz-mono-mp3
│   │   │   ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_10077440_SE_CH34-BG.npy
│   │   │   ├── 2019-10-22-08-40_Fraunhofer-IDMT_30Kmh_10173440_SE_CH34-BG.npy
|   |   ├──birds-melspectrograms
|   |   |   ├──grey-backed camaroptera0.npy
|   |   |   ├──grey-backed camaroptera1.npy
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
Link :link:[Anomaly_Detection_Notebook_Link](https://colab.research.google.com/drive/1Oe9kWt-88ehHAL_Plq5euHh2ekDiXWO5?usp=sharing)

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
