import cv2
import showImage

image = cv2.imread('./image/me.png')
result = image.copy() # copy image

thick = 20
black = 0

numberofrows = result.shape[0]
numberofcolumns = result.shape[1]

# top
for rows in range(thick):
    for columns in range(numberofcolumns):
        result[rows, columns] = black
# under
for rows in range(numberofrows - thick - 1, numberofrows):
    for columns in range(numberofcolumns):
        result[rows, columns] = black
# left
for rows in range(thick, numberofrows - thick - 1):
    for columns in range(thick):
        result[rows, columns] = black
# right
for rows in range(thick, numberofrows - thick - 1):
    for columns in range(numberofcolumns - thick - 1, numberofcolumns):
        result[rows, columns] = black

showImage.showOneImage(result)
