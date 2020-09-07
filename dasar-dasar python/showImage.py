import cv2
import matplotlib.pyplot as plt

def showOneImage(image, title = 'Result'):
    cv2.imshow(title, image)
    cv2.waitKey(0)


def showTwoImage(image1, image2, title1 = 'Result 1', title2 = 'Result 2'):
    cv2.imshow(title1, image1)
    cv2.imshow(title2, image2)
    cv2.waitKey(0)


def showOneImagePlt(image, title = 'Result'):
    plt.imshow(image), plt.title(title)
    plt.show()


def showTwoImagePlt(image1, image2, title1 = 'Result 1', title2 = 'Result 2'):
    plt.subplot(121), plt.imshow(image1), plt.title(title1)
    plt.subplot(122), plt.imshow(image2), plt.title(title2)
    plt.show()
