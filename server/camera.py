import cv2
import numpy as np
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

        """Greyscale"""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        """MOG"""
        fgbg = cv2.createBackgroundSubtractorMOG2()
        fgmask = fgbg.apply(gray)
        
        """GMMM"""
        
        """Threshold"""
        #src = cv2.imread(fgmask, cv2.IMREAD_GRAYSCALE)
        # Basic threshold example
        th, dst = cv2.threshold(fgmask, 0, 128, cv2.THRESH_BINARY)
        
        
        """Dilatasi-Erosi"""
        kernel = np.ones((7, 7), np.uint8)
        opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        
        """Counting car"""
        
        # conver gambar untuk di upstream
        ret, jpeg = cv2.imencode('.jpg', opening)

        # balikin hasil nya ke object untuk di upstream
        return jpeg.tobytes()
