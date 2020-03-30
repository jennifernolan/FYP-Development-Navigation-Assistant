# FYP-Development-Navigation-Assistant
## Project Name
Navigation Assistant: An Investigation into Obstacle Avoidance for the Visually Impaired using the Raspberry Pi

## Developer
Jennifer Nolan C16517636

## Submission Date
11th April 2020

## Description of Folders
### Coding files
An empty file directory made as part of the inital repository commit.

### Codingfiles
This folder contain the prototype code for the prototype system demonstarted as part of the Interim submission. This folder contains the following files:
- Test -> which was used to test whether the Pi camera module was working correctly.
- Images -> where any images taken by the Pi camera module were stored.
- mrcnn -> contains the files required to deploy the Mask RCNN model on the Raspberry Pi.
- MaskRCNN.ipynb -> the Mask RCNN model running on Google Colab
- MaskRCNNModelCamera.py -> this is the program that was used to deemonstrate the running of the Mask RCNN model on the Raspberry Pi as part of the Interim demonstration. It involves the use of the Mask RCNN model on the Raspberry Pi to detect objects within an image taken by the Pi camera.

### Dataset
This folder contains files from the initial project plan to create a custom dataset to train an object detection model with.

### Final_Dissertation_Code
This folder contains the final code used for this project. This folder contains the programs used to run the MobileNet SSDLite object detection model on the Raspberry Pi. It also contains the unit tests conducted during the development phase of this project and their results.

### User_Evaluation_Results
This file contains both the interview answers and questionnaire answers provided by the users as part of the user testing of this project.

### mrcnn
This folder contains the files needed to run the Mask RCNN model on the Raspberry Pi. 

### DissertationReport.docx
The completed dissertation report for this project.

### InterimReport.docx
The completed interim report for this project.

## MobileNet SSDLite model files
[MobileNet SSDLite model files needed to run object detection for this project](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md)

## How to setup and run Navigation Assistant on the Raspberry Pi
1. Connect the Raspberry Pi camera module and HC-SR04 ultrasonic distance sensor to the Raspberry Pi device.
2. Install Raspbian OS on the Raspberry Pi.
3. Install OpenCV and Tensorflow onto the Raspberry Pi using the following commands:
'''
sudo install opencv-python
'''
'''
sudo install tensorflow
'''
4. Download the MobileNet SSDLite model from the [Tensorflow detection model zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) using the following command:
'''
wget http://download.tensorflow.org/models/object_detection/ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz
'''
Then extract the model files using:
'''
tar -xzvf ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz
'''
5. Place the object detection program, ObjectDetection.py, and the range sensor program, RangeSensor.py, into the research/object_detection file.
6. Run the object detection program using the following command:
'''
python3 ObjectDetection.py
'''
