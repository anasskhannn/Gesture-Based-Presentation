# starting with the web cam
import cv2

# Variables
width,height= 1200, 720

# Camera setup

cap= cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)


while True:
    sucess,img=cap.read()
    cv2.imshow("Image", img)
    key= cv2.waitKey(1)
    # Adding if to close webcam and break the loop by pressing "Q"
    if key == ord("q"):
        break