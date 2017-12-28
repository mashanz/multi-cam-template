from queue import Queue
from threading import Thread

from downstream import *


###########################################################
# CONTROL CENTER - FUNGSI MULTI THREAD
###########################################################

# nampilin hasil dari downstream
def showdownstream(in_q):
    # ngambil data dari multi thread
    img = in_q.get()

    # tampilin datanya
    cv2.imshow('Video', img)
    if cv2.waitKey(1) == 27:
        exit(0)


if __name__ == "__main__":
    # initialisasi antrian thread
    q1 = Queue()
    q2 = Queue()

    # initialisasi fungsi thread
    t1 = Thread(target=downstream1, args=(q1,))
    t2 = Thread(target=downstream2, args=(q2,))

    # jalanin sub sub thread yang sudah di inisialisasi
    t1.start()
    t2.start()

    ######################################################
    # THREAD UTAMA
    ######################################################
    while True:
        # panggil fungsi showdownstream(in_q)
        showdownstream(q1)
        showdownstream(q2)
