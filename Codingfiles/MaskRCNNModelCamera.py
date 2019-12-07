#Set up the Pi camera module
from picamera import PiCamera
from time import sleep

camera = PiCamera()

#Preview of what the Pi camera is seeing
camera.start_preview()
sleep(5)
#Capture the picture and save to the specified directory
camera.capture('/home/pi/Documents/images/image.jpeg', use_video_port = True)
camera.stop_preview()

#import the following libraries required to run the Mask R-CNN model
import os
import cv2
import sys
import random
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt

#get the root directory of the project
#this will be used later to get the directory of specific files in the project directory
ROOT_DIR = os.path.abspath("../Documents/")

#import the Mask R-CNN model files
sys.path.append(ROOT_DIR)
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize

import mscoco

MODEL_DIR = os.path.join(ROOT_DIR, 'logs')

#get the trained weights file path and the captured image path
COCO_MODEL_PATH = os.path.join('', 'mask_rcnn_coco.h5')

IMAGE_DIR = os.path.join(ROOT_DIR, 'images')

#configure the model to run inference one image at a time
class InferenceConfig(mscoco.MSCocoConfig):
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

#display the models configuration
config = InferenceConfig()
config.display()

#create a model object and load it with the pretrained weights
model = modellib.MaskRCNN(mode = 'inference', model_dir = MODEL_DIR, config = config)

model.load_weights(COCO_MODEL_PATH, by_name = True)

#the classes from MSCOCO that the model is trained on
#the only objects the model has been trained to detect
class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck',
               'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
               'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack',
               'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
               'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
               'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich',
               'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
               'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
               'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator',
               'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

#read the captured image from the file path
image = cv2.imread(os.path.join(IMAGE_DIR, 'image.jpeg'))

#detect the objects in the image
results = model.detect([image], verbose = 1)

#display the detected image objects to the screen
r = results[0]
visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])