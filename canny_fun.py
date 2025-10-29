import cv2
from cam import ip
cap = cv2.VideoCapture(ip())

while True:
    load, ved = cap.read()
    if not load:
        print("Somting went wrong \n quttng ...")
        break
    gry = cv2.cvtColor(ved,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gry,50,150)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("quit")
        break
    cv2.imshow("gray",edges)

cap.release()
cv2.destroyAllWindows