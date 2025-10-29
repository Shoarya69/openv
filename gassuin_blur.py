import cv2

image = cv2.imread("/home/shoarya/Desktop/open-cv/pexels-eugeniofr-30005297.jpg")
img1 = cv2.resize(image,(500,500))
blur = cv2.GaussianBlur(img1,(499,499),0)

cv2.imshow("Image is showing ...",img1)
cv2.imshow("Blured image ...",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()