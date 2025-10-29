import cv2

image = cv2.imread("/home/shoarya/Desktop/open-cv/pexels-eugeniofr-30005297.jpg")

if image is None:
    print("somthing went wrong : exit code 203")
    exit()

print("image loaded sucessfullly")
img = cv2.resize(image,(700,500))

blur = cv2.medianBlur(img,11)

cv2.imshow('image',img)
cv2.imshow('blur image',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
