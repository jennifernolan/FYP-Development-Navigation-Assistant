'''
Developer Name: Jennifer Nolan (C16517636)

Program Description: This program uses the HC-SR04 ultrasonic distance sensor attached to the Raspberry Pi to
calculate the distance between the Raspberry Pi attached to the user and the closest detected object in the
users path. This calculated distance is then used within the audio navigation instructions provided to the user
later in the system.

Program Change History:
Feb 2020 - Distance from closest object implemented (using the ultrasonic distance sensor and then included in instructions)
Feb 2020 - Audio warning of detected objects (Instructions converted from text to audio output)
March 2020 - Project made portable (Object detection program run on device, Raspberry Pi, start up)

'''

# Import relevant libraries needed to run the distance sensor 
import RPi.GPIO as GPIO
import time
import numpy as np
import os
import sys

def get_distance():
    try:
        # Set up GPIO pin numbering
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
          
        # Name the input and output pins
        TRIG = 23
        ECHO = 24
        
        #os.system('espeak -s150 "Distance Measurement In Progress." --stdout | aplay 2>/dev/null')

        # Set up GPIO ports
        GPIO.setup(TRIG, GPIO.OUT) # output
        GPIO.setup(ECHO, GPIO.IN) # input
        
        # Set trigger pi to low
        GPIO.output(TRIG, False)
        #os.system('espeak -s150 "Waiting For Sensor To Settle." --stdout | aplay 2>/dev/null')
        time.sleep(2)

        # Trigger a pulse to start sensor
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        # Record the low timestamp before signal is received
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
          
        # Record the high timestamp when signal is received
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
        
        # The difference between the two timestamps
        pulse_duration = pulse_end - pulse_start

        # Calculate the distance between the closest detected object and the user
        distance = (pulse_duration * 17150) / 2.54

        # Round to 2 decimal places
        distance = round(distance, 2)

        #os.system('espeak -s150 "Distance: {0} inches" --stdout | aplay 2>/dev/null'.format(np.squeeze(distance).astype(np.int32)))
        
        # Clean GPIO pins to reset all inputs and outputs
        GPIO.cleanup()
        
        return distance
    except RuntimeError as e:
        pass
