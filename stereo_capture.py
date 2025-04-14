import cv2

# Sesuaikan indeks sesuai hasil pengecekan sebelumnya
cam_laptop = cv2.VideoCapture(0)  # Kamera laptop
cam_camo = cv2.VideoCapture(1)    # Kamera Como Camera (USB)

while True:
    retL, frameL = cam_laptop.read()
    retR, frameR = cam_camo.read()

    if not retL or not retR:
        print("Error capturing video")
        break

    # Tampilkan hasil kamera stereo
    cv2.imshow("Laptop Camera", frameL)
    cv2.imshow("Como Camera (USB)", frameR)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam_laptop.release()
cam_camo.release()
cv2.destroyAllWindows()