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
`python3 -m venv iot-env`
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
```
## Acoustic data processing
[Details here](acoustic-processing/)

## Anomaly detection


## Camera trap image processing
