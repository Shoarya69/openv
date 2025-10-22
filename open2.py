import cv2 

image = cv2.imread('/home/shoarya/Desktop/open-cv/pexels-eugeniofr-30005297.jpg')

if image is not None:
    print("image load sucessfully")
    # gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # inverted = cv2.bitwise_not(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(image, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cv2.imwrite("abc.jpg",edges)
else:
    print("Somting went wrong")
