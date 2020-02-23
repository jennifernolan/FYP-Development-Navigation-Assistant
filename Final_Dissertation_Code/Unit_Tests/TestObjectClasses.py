import unittest
import numpy as np
import ObjectDetection as ObjectClass

class TestObjectClasses(unittest.TestCase):
    
    obj = ObjectClass.ObjectDetection()
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_class_person(self):
        classes = [[1]]
        num = np.array([1.])
        score = [[0.92, 0]]
        boxes = [[[0., 0., 0., 0.]]]
        self.obj.instructions(classes, num, 1, score, boxes)
        
    def test_class_chair(self):
        classes = [[62]]
        num = np.array([1.])
        score = [[0.92, 0]]
        boxes = [[[0., 0., 0., 0.]]]
        self.obj.instructions(classes, num, 1, score, boxes)
        
    def test_class_handbag(self):
        classes = [[31]]
        num = np.array([1.])
        score = [[0.92, 0]]
        boxes = [[[0., 0., 0., 0.]]]
        self.obj.instructions(classes, num, 1, score, boxes)
        
    def test_class_suitcase(self):
        classes = [[33]]
        num = np.array([1.])
        score = [[0.92, 0]]
        boxes = [[[0., 0., 0., 0.]]]
        self.obj.instructions(classes, num, 1, score, boxes)
        
    def test_class_keyboard(self):
        classes = [[76]]
        num = np.array([1.])
        score = [[0.92, 0]]
        boxes = [[[0., 0., 0., 0.]]]
        self.obj.instructions(classes, num, 1, score, boxes)
        
    def test_class_bottle(self):
        classes = [[44]]
        num = np.array([1.])
        score = [[0.92, 0]]
        boxes = [[[0., 0., 0., 0.]]]
        self.obj.instructions(classes, num, 1, score, boxes)
        
    def test_class_teddybear(self):
        classes = [[88]]
        num = np.array([1.])
        score = [[0.92, 0]]
        boxes = [[[0., 0., 0., 0.]]]
        self.obj.instructions(classes, num, 1, score, boxes)
        
    def test_class_phone(self):
        classes = [[77]]
        num = np.array([1.])
        score = [[0.92, 0]]
        boxes = [[[0., 0., 0., 0.]]]
        self.obj.instructions(classes, num, 1, score, boxes)
        
if __name__ == '__main__':
    unittest.main()