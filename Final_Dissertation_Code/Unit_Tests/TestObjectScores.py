'''
Developer Name: Jennifer Nolan (C16517636)

Program Description: These set of test cases test the that only classified object with a certainty 
score of 70 or greater are used to generate navigation instructions provided to the user. If a detected 
object has a certainty score of less than 70 then it cannot guarenteed to the same degree that it is 
accurate and therefore is not included in the instructions provided to the user.

Program Change History:
Feb 2020 - Second test iteration
Feb 2020 - Third iteration of tests - checking classification (Ensuring the object detection model is classifying objects correctly)

'''

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