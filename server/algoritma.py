import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt
import csv
import time
import pymysql
from time import gmtime, strftime
fieldnames  = ['time','count']
filelog     = 'cars_count.csv'

def reset():
    with open(filelog, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

def write(time, count):
    with open(filelog, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({fieldnames[0]: time, fieldnames[1]: count})

def algoritma(image):

    db = pymysql.connect("127.0.0.1","root","op3nk3y","dbmulticam" )
    cursor = db.cursor()

    # Resize
    image = imutils.resize(image, width=720)
    ncars = 0
    cars_cascade = cv2.CascadeClassifier('cars.xml')
    img = image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Draw Rectangle
    cars = cars_cascade.detectMultiScale(gray, 1.1, 1)
    cv2.rectangle(img, (0,0), (200,200), (0,255,0), 3)
    cv2.rectangle(img, (250,0), (405,200), (255,0,0),3)
    cv2.rectangle(img, (410,0), (610,200), (0,0,255),3)

    c1 = [0,0,0,0,0,0]
    c2 = [0,0,0,0,0,0]
    # Detect Cars
    for (x, y, w, h) in cars :
        if ((x>0 and y>0) and ((x+w)<200 and (y+h)<200)):
           print("Slot 1 = ada mobil")
           c1[0] = 1
           c1[0] = 1
        if ((x>250 and y>0) and ((x+w)<405 and (y+h)<200)):
           print("Slot 2 = ada mobil")
           c1[1] = 1
           c2[1] = 1
        if ((x>410 and y>0) and ((x+w)<610 and (y+h)<200)):
           print("Slot 3 = ada mobil")
           c1[2] = 1
           c2[2] = 1
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    try:
        waktu = strftime("%H:%M:%S", time.localtime(7))
        cursor.execute("INSERT INTO OUTPUT(waktu, c11, c12, c13, c14, c15, c16, c21, c22, c23, c24, c25, c26) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (waktu,c1[0],c1[1],c1[2],c1[3],c1[4],c1[5],c2[0],c2[1],c2[2],c2[3],c2[4],c2[5]))
        db.commit()
        print("SUCCESS")
    except:
        print("ERROR")
        db.rollback()
    db.close()
    print(ncars) 
    return img
    
