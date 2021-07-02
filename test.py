import cv2
import time
from imutils.video import ImageOutput

h_out = ImageOutput(screen=False) # screen=False implies HTTP output


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

try:
    print(">> starting webcam server on port 8080...")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")

        # set channels to zero...
        #frame[:, :, 0] = 0   # blue
        #frame[:, :, 1] = 0   # green
        #frame[:, :, 2] = 0   # red

        h_out.stream("Webcam", frame)
        time.sleep(1.0/30)
finally:
    print(">> releasing camera...")
    cap.release()
    print("> done!")

