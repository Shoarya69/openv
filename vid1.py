import cv2
from cam import ip
import time

class Camera:
    def __init__(self, record=False, output_file="output.avi"):
        self.cap = cv2.VideoCapture(ip())
        self.record = record
        self.writer = None

        if record:
            # VideoWriter setup
            frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = int(self.cap.get(cv2.CAP_PROP_FPS)) or 20

            codec = cv2.VideoWriter_fourcc(*'XVID')
            filename = f"{int(time.time())}_{output_file}"
            self.writer = cv2.VideoWriter(filename, codec, fps, (frame_width, frame_height))
            print(f"[INFO] Recording started: {filename}")

    def frames(self):
        while True:
            success, frame = self.cap.read()
            if not success:
                print("❌ Camera read failed, exiting stream.")
                break

            # 🔹 Write to video if recording is ON
            if self.record and self.writer:
                self.writer.write(frame)

            yield frame  # live stream frame return hota rahega

        # Clean up
        self.cap.release()
        if self.writer:
            self.writer.release()
        print("[INFO] Camera & Writer released successfully.")

if __name__ == "__main__":
    cam = Camera()
    for y in cam.frames():
        cv2.imshow("gafa",y)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()