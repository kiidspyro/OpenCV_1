import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
# mendefinisikan kode dan membuat objek video writer
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (352, 288))
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # menangkap frame per frame
    ret, frame = cap.read()
    # jika frame benar terbaca ret nya akan true
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
    break
    # operasj kita pada frame dimulai dari sini
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # menampilkan hasil dari frame 
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# jika semua nya selesai, keluar dari capture 
cap.release()
cv.destroyAllWindows()