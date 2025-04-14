import cv2
import numpy as np

# Inisialisasi kamera
cam_laptop = cv2.VideoCapture(0)  # Kamera laptop (internal)
cam_camo = cv2.VideoCapture(1)    # Como Camera (USB) atau bisa pakai URL jika pakai IP Camera
 

# Fungsi untuk menghitung peta kedalaman (depth map)
def compute_depth(frameL, frameR):
    # Samakan ukuran kedua frame
    height, width = frameL.shape[:2]
    frameR = cv2.resize(frameR, (width, height))

    # Konversi ke grayscale
    grayL = cv2.cvtColor(frameL, cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(frameR, cv2.COLOR_BGR2GRAY)

    # Inisialisasi StereoBM untuk menghitung kedalaman
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)

    # Hitung disparitas (depth map)
    disparity = stereo.compute(grayL, grayR)

