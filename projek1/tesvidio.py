import cv2

# Sumber video
video_path = "windah1.mp4"
cap = cv2.VideoCapture(video_path)

# Mengecek apakah video berhasil masuk ke program
if not cap.isOpened():
    print("Could not open the video:", video_path)
else:
    while True:
        # membaca frame dari vidio
        ret, frame = cap.read()

        # mengecek apakah frame berhasiln di baca atau tidak
        if not ret:
            break

        # memunculkan frame
        cv2.imshow("windah1.mp4", frame)

        # menunggu untuk key; keluar jika 'q' di tekan
        key = cv2.waitKey(30) & 0xFF
        if key == ord('q'):
            break

    # keluar dari objek vidio dan menutup semua halaman OpenCV windows
    cap.release()
    cv2.destroyAllWindows()