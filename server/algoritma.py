import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt

def algoritma(image):
    # resize
    image = imutils.resize(image, width=720)

    # """Greyscale"""
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # """MOG"""
    # fgbg = cv2.createBackgroundSubtractorMOG2()
    # fgmask = fgbg.apply(gray)
    
    # """GMMM"""
    
    # """Threshold"""
    # #src = cv2.imread(fgmask, cv2.IMREAD_GRAYSCALE)
    # # Basic threshold example
    # th, dst = cv2.threshold(fgmask, 0, 128, cv2.THRESH_BINARY)
    
    # """Dilatasi-Erosi"""
    # kernel = np.ones((7, 7), np.uint8)
    # opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    
    # """Counting car"""

    # # iseng
    # blurred = cv2.GaussianBlur(image, (5, 5), 0) #(7,7)
    # edged = cv2.Canny(blurred, 50, 2000, apertureSize=5) #10 ,250

    ncars = 0
    car_cascade = cv2.CascadeClassifier('cars.xml')
    img = image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect cars
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    # Draw border
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
        ncars += 1

    print(ncars)

    return img