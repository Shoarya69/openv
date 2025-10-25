import cv2

image = cv2.imread("/home/shoarya/Desktop/open-cv/pexels-eugeniofr-30005297.jpg")

if image is None:
    print("image not found")
else:
    print("image load success")
    h,w = image.shape[:2]
    center_point = (w//2,h//2)
    M = cv2.getRotationMatrix2D(center_point,90,1.0)
    rotate = cv2.warpAffine(image,M,(w,h))
    cv2.imwrite("rotated_image.jpg",rotate)