import cv2

path = './image/'

# Reading image
image = cv2.imread(path+'example.jpg')

row = 300
coloumn = 450
# processing
image = cv2.resize(image, (row, coloumn))

# show
cv2.imshow('result', image)
cv2.waitKey(10000)