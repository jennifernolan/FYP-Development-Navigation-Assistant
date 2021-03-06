'''
Developer Name: Jennifer Nolan (C16517636)

Program Description: This program uses the pretrained MobileNet SSDLite object detction model and the Raspberry Pi camera
module to detect objects in the users path. This program starts begins with setting up the pre trained object detection
model and the Raspbery Pi camera. Once these are set up the Pi camera is set to take in a continuous video input. This
video input is then sent to the model to detect objects in the users path. The results from the object detection model
are then calculated into instructions, along with the distance calculation from the RangeSensor program, that are provided
to the user through an attached audio device, i.e. headphones.

Program Change History:
Jan 2020 - Object detection on video program (Object detection model detecting objects from camera video input)
Feb 2020 - Started to compile instructions (Results from model were compiled into instructions provided to the user through text)
Feb 2020 - Warnings of upcoming objects (Instructions provided to the user using resuts from object detection were finalised)
Feb 2020 - Distance from object attempted with single lens camera
Feb 2020 - Distance from closest object implemented (using the ultrasonic distance sensor and then included in instructions)
Feb 2020 - Audio warning of detected objects (Instructions converted from text to audio output)
March 2020 - Project made portable (Object detection program run on device, Raspberry Pi, start up)

'''

# PiCamera Object Detection Program
# Program uses a TensorFlow classifier to perform object detection using a video stream
# Using the inputted video stream boxes and scores are given to the objects of interest in the frame.

# Source code inspiration from:
# https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi/blob/master/Object_detection_picamera.py
#Elements of this code was left out and changed for this project.

# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
import sys
import time

# Import sensor program
import RangeSensor

# Import the pi camera
from picamera.array import PiRGBArray
from picamera import PiCamera

# Import the utilities
from utils import label_map_util
from utils import visualization_utils as vis_util

# Directory name to the object detection model being used 
model_name = 'ssdlite_mobilenet_v2_coco_2018_05_09'
# Get the current directory
os_path = os.getcwd()

# Path to the frozen graph file that contains the model used for object detection
path_to_graph = os.path.join(os_path, model_name, 'frozen_inference_graph.pb')

# Label map file path used to classify detected objects 
path_to_labels = os.path.join(os_path, 'data', 'mscoco_label_map.pbtxt')

# The number of classes the model is trained to detect
num_of_classes = 90

# The label map is loaded
# Essentially, the utilities functions returns a mapping number which corresponds to a category string in the labels file which classifies the detected object 
label_map = label_map_util.load_labelmap(path_to_labels)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=num_of_classes, use_display_name=True)
category_indx = label_map_util.create_category_index(categories)
         
class ObjectDetection:
    
    def main(self):
        
        os.system('espeak -s150 "Device setup started." --stdout | aplay 2>/dev/null')
        #print('Device setup started')

        # Width and height of window used for video stream
        width = 1280
        height = 720

        # The TensorFlow model is loaded here into memory
        detect_graph = tf.Graph()
        with detect_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.io.gfile.GFile(path_to_graph, 'rb') as fid:
                serial_graph = fid.read()
                od_graph_def.ParseFromString(serial_graph)
                tf.import_graph_def(od_graph_def, name='')
                        
            session = tf.Session(graph=detect_graph)
                    
        # The input image        
        imageTense = detect_graph.get_tensor_by_name('image_tensor:0')

        # The output from the model is the bounding boxes, accuracy scores and classes
        detect_boxes = detect_graph.get_tensor_by_name('detection_boxes:0')

        # The score is the level of confidence/certainty for each object
        detect_scores = detect_graph.get_tensor_by_name('detection_scores:0')
        detect_classes = detect_graph.get_tensor_by_name('detection_classes:0')

        # The number of objects detected
        num_detect = detect_graph.get_tensor_by_name('num_detections:0')
        
        # Pi Camera is setup to perform object detection
        # Reference to the raw capture gathered also
        os.system('espeak -s150 "Setting up camera for navigation." --stdout | aplay 2>/dev/null')
        #print('Setting up camera for navigation')
        
        camera = PiCamera()
        camera.resolution = (width, height)
        camera.framerate = 60
        rawCapture = PiRGBArray(camera, size=(width, height))
        rawCapture.truncate(0)

        counter = 0

        # For loop used to continuously gather video stream from camera
        for frame1 in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):
            # Gather the frame and expand the frame dimensions
            frame = np.copy(frame1.array)
            frame.setflags(write=1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_expanded = np.expand_dims(frame_rgb, axis=0)
                    
            # The object detection is carried out here by running the model and inputting the image
            (boxes, scores, classes, num) = session.run(
                [detect_boxes, detect_scores, detect_classes, num_detect],
                feed_dict={imageTense: frame_expanded})
            
            # Go to the instructions function to calculate instructions provided to the user 
            self.instructions(classes, num, counter, scores, boxes)
            counter = counter + 1
            
            rawCapture.truncate(0)
               
        camera.close()
    
    def instructions(self, classes, num, counter, scores, boxes):
        # If the device has just started to run the object detection program then inform the user when it is possible to start navigating
        if counter == 0:
            os.system('espeak -s150 "Ready to start navigating." --stdout | aplay 2>/dev/null')
            #print('Ready to start navigating')
        
        # Ensure all objects detected in the frame are accounted for in the instructions
        for i in range(0, num[0].astype(np.int32)):
            # Ensure only detected objects with a certainty score greater than 60 are included in instructions provided to the user
            if np.squeeze((scores[0][i])*100).astype(np.int32) > 60:
                # Because only the closest detected object is detected by the sensor only the first returned result from the model, which is the closest, has a distance included in its instructions
                if i == 0:
                    dist = RangeSensor.get_distance()
                else:
                    dist = 0
                
                # Gather the coordinates/location of the detected ojects within the frame
                x1 = (np.squeeze(boxes[0][i][1])*100).astype(np.int32)
                x2 = (np.squeeze(boxes[0][i][3])*100).astype(np.int32)
                
                # If there is no distance to provide for this detected object to the user don't include it in the instructions provided to the user
                if dist == 0 or dist is None:
                    #print("The detected object is: " + str(category_indx[classes[0][i]]['name']) + " \nWith the score of: " + str(np.squeeze((scores[0][i])*100).astype(np.int32)))
                    os.system('espeak -s150 "The detected object {0}." --stdout | aplay 2>/dev/null'.format(category_indx[np.squeeze(classes[0][i]).astype(np.int32)]['name']))
                # If a distance was detected for this object include it in the instruction provided to the user
                else:
                    #print("The detected object is: " + str(category_indx[classes[0][i]]['name']) + " \nWith the score of: " + str(np.squeeze((scores[0][i])*100).astype(np.int32)) + " is " + str(np.squeeze(dist).astype(np.int32)) + " inches away")
                    os.system('espeak -s150 "The detected object {0} is {1} inches away." --stdout | aplay 2>/dev/null'.format(category_indx[np.squeeze(classes[0][i]).astype(np.int32)]['name'], np.squeeze(dist).astype(np.int32)))

                # Depending on where in the frame the object is located depends on where the user is told the object is located in their path, i.e. to their left, right or straight ahead of them
                if x1 in range(0, 40) and x2 in range(0, 40):
                    os.system('espeak -s150 "to the left." --stdout | aplay 2>/dev/null')
                    #print("to the left")
                elif x1 in range(60, 100) and x2 in range(60, 100):
                    os.system('espeak -s150 "to the right." --stdout | aplay 2>/dev/null')
                    #print("to the right")
                else:
                    os.system('espeak -s150 "straight ahead." --stdout | aplay 2>/dev/null')
                    #print("straight ahead")
                time.sleep(2)
         
    
if __name__ == '__main__':
    obj = ObjectDetection()
    obj.main()