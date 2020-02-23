#Python code to test result scores in progam
import unittest
import numpy as np
import ObjectDetection as ObjectClass

class TestObjectScores(unittest.TestCase):
    
    obj = ObjectClass.ObjectDetection()
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_counter_zero(self):
        classes = []
        num = np.array([0.])
        scores = [[0.56, 0 ]]
        boxes = []
        self.obj.instructions(classes, num, 0, scores, boxes)
        
    def test_counter_one(self):
        classes = []
        num = np.array([0.])
        scores = [[0.56, 0]]
        boxes = []
        self.obj.instructions(classes, num, 1, scores, boxes)
        
    def test_score_less_than_70(self):
        classes = []
        num = np.array([1.])
        scores = [[0.56, 0]]
        boxes = []
        self.obj.instructions(classes, num, 1, scores, boxes)
        
    def test_score_greater_than_70(self):
        classes = [[1]]
        num = np.array([1.])
        scores = [[0.86, 0]]
        boxes = [[[0., 0., 0., 0.]]]
        self.obj.instructions(classes, num, 1, scores, boxes)
    
if __name__ == '__main__':
    unittest.main()