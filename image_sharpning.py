import cv2
import numpy as np
from cam import ip
cap = cv2.VideoCapture(ip())

while True:
    load,ved = cap.read()
    if not load:
        print("Somthing went terriblley wrong")
        break
    sharp =np.array([
        [0,-1,0],
        [-1,5,-1],
        [0,-1,0]
    ])
    temp = cv2.filter2D(ved,cv2.CV_32F,sharp)
    sharpend = cv2.convertScaleAbs(temp)
    cv2.imshow("Vedio",sharpend)
    cv2.imshow("real",ved)
    if cv2.waitKey(1) &  0xFF == ord('q'):
        print("qutting ....")
        break

cap.release()
cv2.destroyAllWindows()