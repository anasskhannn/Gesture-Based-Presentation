# starting with the web cam
import os

import cv2

# Variables
# Camera Width & Height
width,height= 1200, 720
# Folder Path
folderpath="img"


# Camera setup
cap= cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

# getting Presentation Images
# We need to sort this to 10 will be at last not after 1
imgPath=sorted(os.listdir(folderpath),key=len)
print(imgPath)

while True:
    # Import Images
    sucess,img=cap.read()
    cv2.imshow("Image", img)
    key= cv2.waitKey(1)
    # Adding if to close webcam and break the loop by pressing "Q"
    if key == ord("q"):
        break