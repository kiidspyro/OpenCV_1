import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

# Mengecek apakah kamera berhasil dibuka
if not cap.isOpened():
    print("Tidak dapat membuka kamera")
    exit()

# Mendefinisikan codec dan membuat objek VideoWriter
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()

    # Jika frame berhasil dibaca, ret bernilai True
    if not ret:
        print("Tidak dapat menerima frame (akhir aliran?). Keluar ...")
        break

    # Membalikkan frame secara horizontal (flipping)
    frame = cv.flip(frame, 1)  # Menggunakan 1 untuk flipping horizontal

    # Menulis frame yang telah dibalikkan
    out.write(frame)

    # Menampilkan frame yang dibalikkan
    cv.imshow('frame', frame)

    # Menunggu penekanan tombol; keluar jika tombol 'q' ditekan
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Melepaskan penangkapan video dan objek VideoWriter
cap.release()
out.release()

# Menutup semua jendela OpenCV
cv.destroyAllWindows()