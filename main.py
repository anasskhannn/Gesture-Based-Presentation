# starting with the web cam
import os
import cv2
from cvzone.HandTrackingModule import HandDetector

# Variables
# Camera Width & Height
width,height= 1200, 720
# Folder Path
folderpath="img"


# Camera setup
cap= cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# getting Presentation Images
# We need to sort this to 10 will be at last not after 1
imgPath=sorted(os.listdir(folderpath),key=len)
# print(imgPath)

# Number of Image to show
imgNum= 0

# Small img of webcam
# These are numbers that are actual/8
hsImg,wsImg=(120*1),(213*1)


# Hand Detector
# if 80% surity of hands then detect as hands
detector = HandDetector(detectionCon=0.8,maxHands=1)


while True:
    # Import Images
    sucess,img=cap.read()

    fullimg=os.path.join(folderpath,imgPath[imgNum])
    CurrentImg=cv2.imread(fullimg)
    # Resizing because image too large for display
    CurrentImgResize=cv2.resize(CurrentImg,(width,height))

    # finding hands on img i.e webcam
    hands, img= detector.findHands(img)





    # Adding Small Webcam Image on Slide
    imgSmall=cv2.resize(img, (wsImg, hsImg))
    # We dont know the widht and height of slide thus getting them
    hsilde, wslide, _ = CurrentImgResize.shape

    # putting small webcam on right side
    # height 0 to height of web image
    # widht  (actual widht of slide - width of small img) to  width of slide
    CurrentImgResize[0:hsImg, wslide-wsImg:wslide] = imgSmall

    cv2.imshow("WEBCAM", img)
    cv2.imshow("Slides", CurrentImgResize)
    key= cv2.waitKey(1)
    # Adding if to close webcam and break the loop by pressing "Q"
    if key == ord("q"):
        break