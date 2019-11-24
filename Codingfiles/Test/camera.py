from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(10)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

from skimage.io import imread
import numpy as np

im = imread('image.jpg')

from skimage.transform import resize

im_resize = resize(im, (32,32), mode='constant')

from keras.models import load_model
model = load_model('/home/pi/Desktop/modelkeras_cifar10_model.h5')

im_final = im.reshape(1,32,32,3)

ans = model.predict(im_final)
print(ans)

