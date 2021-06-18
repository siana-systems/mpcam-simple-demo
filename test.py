import cv2
import time
from imutils.video import ImageOutput

h_out = ImageOutput(screen=False) # screen=False implies HTTP output

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print(">> start webcam server...")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")

    h_out.stream("Webcam", frame)
    time.sleep(1.0/30)
