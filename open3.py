import cv2

image = cv2.imread("/home/shoarya/Desktop/open-cv/pexels-eugeniofr-30005297.jpg")

if  image is None:
    print("Image not found")
else:
    print("image is loaded")
    resized = cv2.resize(image,(400,200))
    cv2.imshow("reized image",resized)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite("resized_output",resized)
    