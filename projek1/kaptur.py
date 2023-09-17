import cv2

# Inisialisasi penangkapan kamera
cap = cv2.VideoCapture(0)  # Angka 0 mengacu pada kamera utama, 1 untuk kamera sekunder

# Periksa apakah penangkapan kamera berhasil dibuka
if not cap.isOpened():
    print("Tidak dapat membuka kamera.")
    exit()

while True:
    # Baca frame dari kamera
    ret, frame = cap.read()

    # Periksa apakah frame berhasil dibaca
    if not ret:
        print("Tidak dapat menerima frame (akhir aliran?). Keluar ...")
        break

    # Tampilkan frame dalam jendela
    cv2.imshow('Kamera', frame)

    # Tekan tombol 'q' untuk keluar dari loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Setelah selesai, lepaskan penangkapan kamera dan tutup jendela
cap.release()
cv2.destroyAllWindows()