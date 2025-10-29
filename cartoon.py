import cv2
from matplotlib import pyplot as plt

img = cv2.imread("/home/shoarya/Desktop/open-cv/pexels-eugeniofr-30005297.jpg")

if img is None:
    print("There is some issue with image")
    exit()

img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_blur = cv2.medianBlur(gray,5)
edges = cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=9,C = 9)



plt.imshow()
plt.show()
