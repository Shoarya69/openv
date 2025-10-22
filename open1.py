import cv2

image = cv2.imread("/home/shoarya/Desktop/open-cv/pexels-eugeniofr-30005297.jpg")

if image is None:
    print("somting went wrong")
else:
    print("image load suessfully")
    h,w,c = image.shape
    print(f"image hight {h} and image width is {w} colorr chanle:- {c}")
    # cv2.imshow("My image",image)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()

