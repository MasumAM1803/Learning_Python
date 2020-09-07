import cv2
import showImage

image = cv2.imread('./image/me.png')

numberofrows = image.shape[0]
numberofcolumns = image.shape[1]
xCenter = numberofcolumns // 2
yCenter = numberofrows // 2

cv2.line(image, (xCenter, 0), (xCenter, numberofrows - 1), [128, 128, 128], 5)
cv2.line(image, (0, yCenter), (numberofcolumns - 1, yCenter), [128, 128, 128], 5)

showImage.showOneImage(image)