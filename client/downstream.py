import cv2
from urllib.request import urlopen
import numpy as np

###########################################################
# CONTROL CENTER - FUNGSI DOWNSTREAM
###########################################################

# catch dari server client ke 1
def downstream1(in_q):
    stream = urlopen('http://192.168.150.103:5000/video_feed')
    bytes = b''
    while True:
        bytes += stream.read(1024)
        a = bytes.find(b'\xff\xd8')
        b = bytes.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytes[a:b + 2]
            bytes = bytes[b + 2:]
            img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

            # taruh hasil catch nya di in_q untuk multi threading
            in_q.put(img)


# catch dari server client ke 2
def downstream2(in_q):
    stream = urlopen('http://192.168.150.102:5000/video_feed')
    bytes = b''
    while True:
        bytes += stream.read(1024)
        a = bytes.find(b'\xff\xd8')
        b = bytes.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytes[a:b + 2]
            bytes = bytes[b + 2:]
            img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

            # taruh hasil catch nya di in_q untuk multi threading
            in_q.put(img)
