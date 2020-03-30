'''
Developer Name: Jennifer Nolan (C16517636)

Program Description: These set of test cases test the file paths of the files required to run the
object detection model, MobileNet SSDLite. 

Program Change History:
Feb 2020 - Start to unit testing begun
Feb 2020 - Initial unit test conducted (Test for file paths conducted)

'''

#Python code to test file paths in progam
import unittest
import os

from ObjectDetection import path_to_graph
from ObjectDetection import path_to_labels
from ObjectDetection import model_name

path = os.getcwd()

incorrect_graph_path = os.path.join(path, 'frozen_inference_graph.pb')
incorrect_labels_path = os.path.join(path, 'mscoco_label_map.pbtxt')

test_graph_path = os.path.join(path, model_name, 'frozen_inference_graph.pb')
test_label_path = os.path.join(path, 'data', 'mscoco_label_map.pbtxt')

class TestDetectionPaths(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    
    def test_incorrect_graph_path(self):
        test = incorrect_graph_path == path_to_graph
        self.assertFalse(test)
    
    def test_part_graph_file_path(self):
        self.assertIn('frozen_inference_graph', path_to_graph)
        
    def test_full_graph_file_path(self):
        self.assertEqual(test_graph_path, path_to_graph)
        
    def test_full_graph_upper(self):
        self.assertFalse(path_to_graph.isupper())
        
    def test_full_graph_lower(self):
        self.assertFalse(path_to_graph.islower())    
        
        
        
    def test_incorrect_labels_path(self):
        test = incorrect_labels_path == path_to_graph
        self.assertFalse(test)
    
    def test_part_labels_file_path(self):
        self.assertIn('mscoco_label_map', path_to_labels)
        
    def test_full_labels_file_path(self):
        self.assertEqual(test_label_path, path_to_labels)
        
    def test_full_labels_upper(self):
        self.assertFalse(path_to_labels.isupper())
        
    def test_full_labels_lower(self):
        self.assertFalse(path_to_labels.islower())  

    
if __name__ == '__main__':
    unittest.main()