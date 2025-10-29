import cv2

img = cv2.imread("/home/shoarya/Desktop/open-cv/pexels-eugeniofr-30005297.jpg",cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img,(700,500))

ret, img3 = cv2.threshold(img2,120,225,cv2.THRESH_BINARY)

cv2.imshow("black white",img2)
cv2.imshow("threshold image",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()