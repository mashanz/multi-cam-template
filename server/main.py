import cv2
from matplotlib import pyplot as plt

ncars = 0

car_cascade = cv2.CascadeClassifier('cars.xml')
img = cv2.imread('car1.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect cars
cars = car_cascade.detectMultiScale(gray, 1.1, 1)

# Draw border
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
    ncars += 1

# Show image
while True:
    cv2.imshow("img", img)
    if cv2.waitKey(1) == 27:
        exit(0)
