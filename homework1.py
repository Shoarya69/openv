import cv2

image = cv2.imread("/home/shoarya/Desktop/open-cv/pexels-eugeniofr-30005297.jpg")

if image is None:
    print("Somthing went wrong")
else:
    print("imae load sucessfully")
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("1abc.jpg",gray)