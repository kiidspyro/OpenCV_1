import cv2  # Diperlukan OpenCV untuk pengolahan citra

# Membaca citra RGB
img_rgb = cv2.imread('megagengar.jpg')

# Menampilkan citra RGB
cv2.imshow('Citra RGB', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()