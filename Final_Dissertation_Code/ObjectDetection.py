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

# Set up the pi camera
from picamera.array import PiRGBArray
from picamera import PiCamera

# Import the utilities
from utils import label_map_util
from utils import visualization_utils as vis_util

def main():

    print('Device setup started')

    # Width and height of window used to display video stream
    width = 1280
    height = 720

    # Directory name to the object detection model being used 
    model_name = 'ssdlite_mobilenet_v2_coco_2018_05_09'
    # Get the current directory
    os_path = os.getcwd()

    # Path to the frozen graph file that contains the model used for object detection
    path_to_graph = os.path.join(os_path, model_name, 'frozen_inference_graph.pb')

    # Label map file path
    path_to_labels = os.path.join(os_path, 'data', 'mscoco_label_map.pbtxt')

    # The number of classes the model is trained to detect
    num_of_classes = 90

    # The label map is loaded
    # Essentially, the utilities functions returns a mapping number which corresponds to a category string in the labels file
    label_map = label_map_util.load_labelmap(path_to_labels)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=num_of_classes, use_display_name=True)
    category_indx = label_map_util.create_category_index(categories)

    # The TensorFlow model is loaded here into memory
    detect_graph = tf.Graph()
    with detect_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(path_to_graph, 'rb') as fid:
            serial_graph = fid.read()
            od_graph_def.ParseFromString(serial_graph)
            tf.import_graph_def(od_graph_def, name='')
            
        session = tf.Session(graph=detect_graph)
        
    # The input image        
    imageTense = detect_graph.get_tensor_by_name('image_tensor:0')

    # The output is the bounding boxes, accuracy scores and classes
    detect_boxes = detect_graph.get_tensor_by_name('detection_boxes:0')

    # The score is the level of confidence for each object
    detect_scores = detect_graph.get_tensor_by_name('detection_scores:0')
    detect_classes = detect_graph.get_tensor_by_name('detection_classes:0')

    # The number of objects detected
    num_detect = detect_graph.get_tensor_by_name('num_detections:0')

    # Frame rate calculation
    frame_rate = 1
    freq = cv2.getTickFrequency()
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Pi Camera is setup to perform object detection
    # Reference to the raw capture gathered also
    print('Setting up camera for navigation')
    
    camera = PiCamera()
    camera.resolution = (width, height)
    camera.framerate = 60
    rawCapture = PiRGBArray(camera, size=(width, height))
    rawCapture.truncate(0)

    counter = 0
    previous_class = 0

    for frame1 in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):
        t1 = cv2.getTickCount()
        
        # Gather the frame and expand the frame dimensions
        frame = np.copy(frame1.array)
        frame.setflags(write=1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_expanded = np.expand_dims(frame_rgb, axis=0)
        
        # The object detection is carried out here by running the model and inputting the image
        (boxes, scores, classes, num) = session.run(
            [detect_boxes, detect_scores, detect_classes, num_detect],
            feed_dict={imageTense: frame_expanded})
            
        # The results of the object detection are drawn
        vis_util.visualize_boxes_and_labels_on_image_array(
            frame,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_indx,
            use_normalized_coordinates=True,
            line_thickness=8,
            min_score_thresh=0.50)
        
        if counter == 0:
            print('Ready to start navigatng')
            counter = counter + 1
            
        if previous_class != np.squeeze(classes[0][0]).astype(np.int32):
            instructions(category_indx[np.squeeze(classes[0][0]).astype(np.int32)]['name'])
            previous_class = np.squeeze(classes[0][0]).astype(np.int32)
        
        cv2.putText(frame, "FPS: {0:.2f}".format(frame_rate),(30,50),font,1,(255,255,0),2,cv2.LINE_AA)
        
        # The results drawn on the frame are displayed
        cv2.imshow('Object detector', frame)
        
        t2 = cv2.getTickCount()
        time1 = (t2-t1)/freq
        frame_rate = 1/time1
        
        # Quit the program with the key q
        if cv2.waitKey(1) == ord('q'):
            break
        
        rawCapture.truncate(0)
        
    camera.close()

def instructions(detected_object):
    print("The detected object is: " + str(detected_object))

main()