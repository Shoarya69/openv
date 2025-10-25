import cv2

image = cv2.imread("/home/shoarya/Desktop/open-cv/pexels-eugeniofr-30005297.jpg")

if image is None:
    print("Image not Found")
else:
    print("Image found successfully")
    fliped =cv2.flip(image,1)
    cv2.imwrite("fliped.jpg",fliped)