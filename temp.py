# -*- coding: utf-8 -*-
"""
Spyder-Editor

Dies ist eine temporäre Skriptdatei.
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
from matplotlib import image 

r = 28.3 #cm
d = 21.5 # cm
B = 20 #cm

theta = np.arctan(r / (2*d))

print(f"theta = {theta} radians")

theta_deg = np.rad2deg(theta)

print(f"theta = {theta_deg} degrees")

plt.close('all')
fig = plt.figure()
img_L = image.imread('C:/Users/schnebli/Pictures/IMG_0901.JPG')
plt.plot(2450, 1650,marker = 'o', color="white")
plt.imshow(img_L)
plt.title("image left")
plt.show() 


plt.close('all')
fig = plt.figure()
img_L = image.imread('C:/Users/schnebli/Pictures/IMG_0902.JPG')
plt.plot(850, 1650,marker = 'o', color="white")
plt.imshow(img_R)
plt.title("image right")
plt.show() 

width = img_L.shape[1]
x_0 = width
print(f"x_0 = {x_0}")

x_left = 2450 - (width/2)
x_right = (width/2) - 850
x_right = x_right*(-1)

print(f"x_1 = {x_left}")
print(f"x_2 = {x_right}")

D = (B*x_0) / (2 * np.tan(theta) * (x_left - x_right))

print(f"Distance to säuli = {D}")
