import cv2
import numpy as np
import imutils
from algoritma import algoritma
# from skimage.morphology import opening

###########################################################
# CLIENT KAMERA - INITIALISASI OBJECT
###########################################################
# Image processingnya di taroh di sini
class VideoCamera(object):


    # Fungsi untuk inisialisasi kamera client
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    # Fungsi untuk melepas koneksi camera client bila sudah tidak digunakan
    def __del__(self):
        self.video.release()

    # menggisi object dengan hasil capture dari kamera untuk di upstream
    def get_frame(self):
   
        # succes capture video
        success, image = self.video.read()

        # algoritma image processingnya
        hasil = algoritma(image)
        
        # conver gambar untuk di upstream
        ret, jpeg = cv2.imencode('.jpg', hasil)

        # balikin hasil nya ke object untuk di upstream
        return jpeg.tobytes()