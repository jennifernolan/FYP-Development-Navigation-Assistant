import RPi.GPIO as GPIO
import time
import numpy as np
import os
import sys

def get_distance():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
            
        TRIG = 23
        ECHO = 24
        
        #os.system('espeak -s150 "Distance Measurement In Progress." --stdout | aplay 2>/dev/null')

        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        
        GPIO.output(TRIG, False)
        #os.system('espeak -s150 "Waiting For Sensor To Settle." --stdout | aplay 2>/dev/null')
        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
            
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
            
        pulse_duration = pulse_end - pulse_start

        distance = (pulse_duration * 17150) / 2.54

        distance = round(distance, 2)

        #os.system('espeak -s150 "Distance: {0} inches" --stdout | aplay 2>/dev/null'.format(np.squeeze(distance).astype(np.int32)))
        
        GPIO.cleanup()
        
        return distance
    except RuntimeError as e:
        pass
