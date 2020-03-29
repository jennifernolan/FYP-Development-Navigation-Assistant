'''
Developer Name: Jennifer Nolan (C16517636)
Program Description: These set of test cases test the detected object distance retrieved by the RangeSensor program.
This program tests for short, middle and long distances.

'''

#Python code to test distance detection
import unittest
from RangeSensor import get_distance

class TestSensorDistance(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_long_distance_sensor(self):
        distance = get_distance()
        print(distance)
        if distance >= 60:
            self.assertTrue(distance >= 60)
        else:
            self.assertFalse(distance >= 60)
        
    def test_medium_distance_sensor(self):
        distance = get_distance()
        print(distance)
        if distance < 60 and distance >= 20:
            self.assertTrue(distance < 60 and distance >= 20)
        else:
            self.assertFalse(distance < 60 and distance >= 20)
        
        
    def test_short_distance_sensor(self):
        distance = get_distance()
        print(distance)
        if distance < 20:
            self.assertTrue(distance < 20)
        else:
            self.assertFalse(distance < 20)
        
    
if __name__ == '__main__':
    unittest.main()