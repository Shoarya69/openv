import cv2
from cam import ip
from circluar_img import circle

cap = cv2.VideoCapture(ip())

while True:
    ret, frame = cap.read()
    if not ret:
        print("Could not read fram")
        break
    cir = circle(frame)
    rotated_90 = cv2.rotate(cir, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("webcam Feed",cir)
    cv2.imshow("per ",rotated_90)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("quting")
        break

cap.release()
cv2.destroyAllWindows()