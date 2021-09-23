# Data Science Africa (DSA2021)
#### October 4th - October 8th 2021
#### Kimberley, Northern Cape, South Africa 

## TOPIC : Water Resource Monitoring and River Catchment analysis 
#### Host: Jason Kabi

![cover page image](/anomaly-detection/assets/img/snapshot.jpg)

#### Brief Bio
I am currently a Research intern at Centre for Data Science and Artificial intelligence(DSAIL) Dedan Kimathi University of Technology(DeKUT).I am also a Graduate Electrical Engineer and Data Scientist with experience in Machine Learning, IoT/Sensor systems development, IoT/Sensor systems deployment, data analysis, data visualization, and Electrical hardware (PCB) Design. In this session am  taking audiences through a river Water level Monitoring project. Data collected can be used to diagnose the status of the river catchment. 
- :link: [Linkedin](https://www.linkedin.com/in/kabi-jason-b14b68164)
- :link: Email: jason.kabi@dkut.ac.ke


#### What we intended to handle during these session

## :point_right: Anomaly detection using :link: [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)

#### :one: Materials provided
- Presentation slides 
- A water-level sample dataset (tailored for this Anomaly detection piece)
- A requirements.txt file to create a python environment 

#### :three: Requirements
- A computer with Python installed (Can be installed by installing [Anaconda](Downloads\Programs\Anaconda3-2021.05-Windows-x86_64.exe) 
- Access to Jupyter notebook

#### :two: Python Environment _ setup
To work on the notebook provided, you will need to set-up a Python environment. Below are steps on how to set it up. (the requirement.txt provided will help)

OPTION 1: :arrow_forward: Python_env - Windows 

**:computer: Windows**
1. Download Anaconda link :link:[Anaconda](Downloads\Programs\Anaconda3-2021.05-Windows-x86_64.exe) and install it (stick to the defaults and remember to link it to your command prompt )
2. Open up the Anaconda prompt on the search button 
3. This dsa2021 repositroy into your computer
4. On the Anaconda prompt, change the directory and access the repo you have just cloned.
5. To create the conda environment, start with :( name: name of the environment python: python version)
- Run `conda create -name dsa2021_anomaly python=3.7`. 
6. stick to the defaults and press YES at all steps.
- After the process is done, activate the environment you have just setup by running.
- Run `conda activate dsa2021_anomaly` or `activate dsa2021_anomaly `.
7. At this point, you can install the requirements by running.
- Run `pip install -r requirements.txt`.
8. After the requirement installation, the environment is ready to go.
- Run `jupter notebook` to open up the anomaly detection notebook on your default browser. 
:battery: **green light**

OPTION 2: :arrow_forward: Google collab 
Link :link:[Anomaly_Detection_Notebook_Link](https://colab.research.google.com/drive/1mC5q92VLj-EQHTAUGSzr8OLTv54aPQT8?usp=sharing)
:arrow_right: Loading up the dataset  
- Click on the files icon on the side bar shown below.

![cover page image](/anomaly-detection/assets/img/file1.PNG)

- Click on the upload button aned you will be prompted to upload a file.
- Select water-level dataset sample from the repo you cloned (in the static folder) and upload it.

![cover page image](/anomaly-detection/assets/img/file2.PNG)

- Right click on the dataset sample to copy the path.
- Paste it on the *package import* cell of the notebook

![cover page image](/anomaly-detection/assets/img/file2.PNG)

- Run the notebook :battery: **green light**