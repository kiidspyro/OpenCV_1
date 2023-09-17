import numpy as np
import cv2 as cv

# Menampilkan semua atribut yang mengandung 'EVENT' dari modul cv
events = [event for event in dir(cv) if 'EVENT' in event]
print(events)

# mouse callback function
def draw_circle(event, x, y, flags, param):
    global img  # Menambahkan deklarasi global img di dalam fungsi
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)

# Membuat gambar hitam, jendela, dan mengaitkan fungsi dengan jendela
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while(1):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:  # Tekan Esc (kode ASCII 27) untuk keluar
        break

cv.destroyAllWindows()
