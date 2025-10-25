import cv2
import os
from dotenv import load_dotenv

load_dotenv()

cap = cv2.VideoCapture(os.getenv("ip_video"))

while True:
    ret, frame = cap.read()

    if not ret:
        print("Somting went wrong")
        break
    filp = cv2.flip(frame,1)
    cv2.imshow("Camera",filp)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("quting")
        break

cap.release()
cv2.destroyAllWindows()

