# starting with the web cam
import os

import cv2

# Variables
# Camera Width & Height
width,height= 720, 480
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
imgNum= 3

while True:
    # Import Images
    sucess,img=cap.read()

    fullimg=os.path.join(folderpath,imgPath[imgNum])
    CurrentImg=cv2.imread(fullimg)
    CurrentImgResize=cv2.resize(CurrentImg,(720,480))

    cv2.imshow("WEBCAM", img)
    cv2.imshow("Slides", CurrentImgResize)
    key= cv2.waitKey(1)
    # Adding if to close webcam and break the loop by pressing "Q"
    if key == ord("q"):
        break