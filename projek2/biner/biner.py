import cv2

# Membaca citra Grayscale
img_gray = cv2.imread('kumolonimbus.jpg', cv2.IMREAD_GRAYSCALE)

# Mengaplikasikan thresholding untuk membuat citra biner
_, img_binary = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)  # Nilai threshold diubah menjadi 150

# Menampilkan citra Biner
cv2.imshow('Citra Biner', img_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
