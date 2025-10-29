import cv2
from cam import ip

cap = cv2.VideoCapture(ip())

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_hight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

file_name = "my_video.avi"

codec = cv2.VideoWriter_fourcc(*'XVID')
recorded = cv2.VideoWriter(file_name,codec,50,(frame_width,frame_hight))

while True:
    sucess,image = cap.read()

    if not sucess:
        print("somting wrong with this video")
        break
    flip = cv2.flip(image,1)    
    recorded.write(flip)
    cv2.imshow("Record live ...",flip)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(f"File save as:-{file_name}\n")
        print("Quting ...")
        break




cap.release()
recorded.release()
cv2.destroyAllWindows()