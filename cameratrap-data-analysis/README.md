# Camera trap Image Processing

# Background
Having up to date information about the location and behaviour of animals in the wild will improve our ability to study and better conserve natural ecosystems. It will also help us mange and protect these ecosystems. 

Motion sensor cameras in natural habitats offer an inexpensive opportunity to gather data on animals.

Deep neural networks can be used to automatically extract invaluable information from these data as opposed to having humans analyse these data which would be too expensive, time consuming and too manual.

# Introduction

This project has been deployed in Dedan Kimathi University's conservancy in Kenya. 
The camera trap is being used to collect images of animals in the conservancy with the aim of identifying predators, which is a problem the rangers have.
It is based on a passive infrared (PIR) MOTION sensor and a raspberry pi with a pi camera, running on a python program. 
It is set in such a way that once motion is detected, the camera captures images and saves them in an SD card. 
A solar panel is used to recharge batteries. Our current powering system enables our camera trap to stay in the field for a week, after which batteries are recharged and SD cards changed. We currently have 3 camera traps in the conservancy.

![21Jul09_17_49_24-2](https://user-images.githubusercontent.com/74656615/134635155-9b8b6b24-b332-453f-801c-2ae9e726c07a.jpg)



# Our Data
Our data is in the form of images saved in jpg format. They are saved in the format YY-MM-DD-H-M-S.
The animals included in our dataset are Impalas, monkeys, warthogs, bushbucks, waterbucks and zebras.

# Image Processing and Classification
The file `Camera-trap-image-processing.ipynb` shows the steps used to classify a sample of the data we collected.


