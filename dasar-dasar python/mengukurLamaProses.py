import cv2
import showImage

image = cv2.imread('./image/me.png')

# process 1
startTime = cv2.getTickCount()

# processing
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold, binerImage = cv2.threshold(grayImage, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)

showImage.showOneImage(binerImage)

endTime = cv2.getTickCount()
duration = (endTime - startTime) / cv2.getTickFrequency()

print('Processiong Time : ', duration, ' second')