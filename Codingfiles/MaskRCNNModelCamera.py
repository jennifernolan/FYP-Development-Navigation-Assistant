from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Documents/images/image.jpeg', use_video_port = True)
camera.stop_preview()

import os
import cv2
import sys
import random
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt

ROOT_DIR = os.path.abspath("../Documents/")

sys.path.append(ROOT_DIR)
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize

import mscoco

MODEL_DIR = os.path.join(ROOT_DIR, 'logs')

COCO_MODEL_PATH = os.path.join('', 'mask_rcnn_coco.h5')

IMAGE_DIR = os.path.join(ROOT_DIR, 'images')

class InferenceConfig(mscoco.MSCocoConfig):
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()
config.display()

model = modellib.MaskRCNN(mode = 'inference', model_dir = MODEL_DIR, config = config)

model.load_weights(COCO_MODEL_PATH, by_name = True)

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

image = cv2.imread(os.path.join(IMAGE_DIR, 'image.jpeg'))

results = model.detect([image], verbose = 1)

r = results[0]
visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])