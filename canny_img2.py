import cv2

img = cv2.imread("/home/shoarya/Desktop/open-cv/pexels-eugeniofr-30005297.jpg",cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img,(700,500))
edges = cv2.Canny(img1,50,150)

cv2.imshow("img0",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()