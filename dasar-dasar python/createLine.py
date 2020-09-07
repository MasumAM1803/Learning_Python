import cv2
import numpy as np
import showImage

image = cv2.imread('./image/me.png')

# GARIS LURUS
numberofrows = image.shape[0]
numberofcolumns = image.shape[1]
xCenter = numberofcolumns // 2
yCenter = numberofrows // 2

cv2.line(image, (xCenter, 0), (xCenter, numberofrows - 1), (128, 128, 128), 5)
cv2.line(image, (0, yCenter), (numberofcolumns - 1, yCenter), (128, 128, 128), 5)
showImage.showOneImage(image)


# LINGKARAN
cv2.circle(image, (xCenter, yCenter), 100, [255, 255, 255], 10)
showImage.showOneImage(image)


# ELIPS
cv2.ellipse(image, (xCenter, yCenter), (100, 50), 0, 0, 360, (255, 255, 255), 5)
showImage.showOneImage(image)

# PERSEGI
cv2.rectangle(image, (10, 10), (128, 128), [255, 255, 255], 5)
showImage.showOneImage(image)

# POLIGON
point = np.array([[10, 128], [200, 10], [180, 120], [220, 240]], np.int32)
cv2.polylines(image, [point], True, (0, 0, 0), 3)
showImage.showOneImage(image)