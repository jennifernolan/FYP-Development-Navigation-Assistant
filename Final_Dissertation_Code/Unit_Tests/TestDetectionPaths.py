#Python code to test file paths in progam
import unittest
import os

from models.research.object_detection.ObjectDetection import path_to_graph
from models.research.object_detection.ObjectDetection import path_to_labels

os_path = os.getcwd()
path = os.path.join(os_path, 'models/research/object_detection')
test_graph_path = os.path.join(path, path_to_graph)
test_labels_path = os.path.join(path, path_to_labels)


class TestDetectionPaths(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_part_graph_file_path(self):
        self.assertIn('frozen_inference_graph', test_graph_path)
        
    def test_full_graph_file_path(self):
        self.assertEqual(test_graph_path, path_to_graph)
        
    def test_part_labels_file_path(self):
        self.assertIn('mscoco_label_map', test_labels_path)
        
    def test_full_labels_file_path(self):
        self.assertEqual(test_labels_path, path_to_labels)

    
if __name__ == '__main__':
    unittest.main()