import cv2 

image = cv2.imread('/home/shoarya/Desktop/open-cv/pexels-eugeniofr-30005297.jpg')

if image is not None:
    print("image load sucessfully")
else:
    print("Somting went wrong")