import cv2
from cam import ip


cap = cv2.VideoCapture(ip())

while True:
    ret, frame = cap.read()

    if not ret:
        print("Somting went wrong")
        break
    filp = cv2.flip(frame,1)
    blur = cv2.GaussianBlur(filp,(5,5),0)
    cv2.imshow("Camera",blur)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("quting")
        break

cap.release()
cv2.destroyAllWindows()

