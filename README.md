# 2020-3D-Object-Detection

## Abstract

3D Object Detection with CenterPoint The purpose of this research is to do 3D object detection from a photo using machine learning. The goal is a working model that can detect multiple 3D objects and provide their dimensions and orientation given a photo. There are many ways to implement this, but this project uses center-based 3D object detection and tracking, where the model predicts the physical, three-dimensional center of detected objects, which is regressed to predict the dimensions and orientation of the object. This output can be tracked over time to predict the velocity of objects and visualize their movement using a GIF. The model was found to have a high level of accuracy in detecting and tracking 3D objects. This model can be used to detect and track objects in a plethora of applications including surveillance, autonomous vehicles, and augmented reality.

## Short video about our project

https://www.youtube.com/watch?v=9qhR76ZDG2c&feature=youtu.be

## File descriptions

### checker

- data-checker--file-output-MASTER.txt: has list of data files used in validation
- data-checker--file-output.py: script used to create MASTER file
- validation.sh: script used to run validation

### data

- empty folder where the data will be put

### environment

- requirements.txt: list of all the packages needed to download

### processor

- download.sh: script for downloading the data

### configs/centerpoint

- has 3 different models that you can pick from for training

### tools

- This folder contains utilities for the demo/testing like visualizing and turning pictures into a gif

### det3d

- This folder is the framework used in our project

### work_dirs/centerpoint_pillar_512_demo

- last.pth: pretrained weights used for the demo and can be used for testing

## Training

### For instructions on how to get training started go to this google colab

- https://colab.research.google.com/drive/1wWRuPgwtnL-14x3sR8drzBgmCRET21k1?usp=sharing


## Citations

@article{Yin2020Centerbased3O,
  title={Center-based 3D Object Detection and Tracking},
  author={Tianwei Yin and Xingyi Zhou and Philipp Kr{\"a}henb{\"u}hl},
  journal={ArXiv},
  year={2020},
  volume={abs/2006.11275}
}

@article{zhou2018voxelnet,
   title={VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection},
   journal={CVPR},
   author={Zhou, Yin and Tuzel, Oncel},
   year={2018},
}
