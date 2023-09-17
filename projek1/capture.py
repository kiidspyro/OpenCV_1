import numpy as np
import cv2 as cv

# Inisialisasi penangkapan dengan properti yang diubah
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)  # Ubah lebar frame
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)  # Ubah tinggi frame
cap.set(cv.CAP_PROP_FPS, 60)  # Ubah frame rate menjadi 15 fps

if not cap.isOpened():
    print("Tidak dapat membuka kamera")
    exit()

while True:
    # Mengambil frame satu per satu
    ret, frame = cap.read()

    # Jika frame berhasil dibaca, ret bernilai True
    if not ret:
        print("Tidak dapat menerima frame (akhir aliran?). Keluar ...")
        break

    # Konversi frame ke citra grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Menampilkan frame hasil konversi
    cv.imshow('frame', gray)

    # Menunggu penekanan tombol; keluar jika tombol 'q' ditekan
    if cv.waitKey(1) == ord('q'):
        break

# Setelah selesai, lepaskan penangkapan video dan tutup jendela
cap.release()
cv.destroyAllWindows()