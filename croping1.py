import cv2

image = cv2.imread("/home/shoarya/Desktop/open-cv/pexels-eugeniofr-30005297.jpg")

if image is None:
    print("Image is not found")
else:
    print("Image load successfully")
    cropped = image[1000:2000, 1000:1400]
    cv2.imshow("cropped imaae",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()