import cv2
from cvzone.HandTrackingModule import HandDetector

import pyautogui
import numpy as np


# Declare variable for width, height

# Width of Camera

# Height of Camera

# Frame Rate


# Smoothening Factor


# Delecare the variables to store the screen sizes


# Previous coordinates


# Current coordinates


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)


while True:

    try:
        check, cameraFeedImg = cap.read()
        cameraFeedImg = cv2.flip(cameraFeedImg, 1)

        handsDetector = detector.findHands(cameraFeedImg, flipType=False)
        hands = handsDetector[0]
        cameraFeedImg = handsDetector[1]

        if hands:
            hand1 = hands[0]
            lmList = hand1["lmList"]
            handType = hand1["type"]

            fingers = detector.fingersUp(hand1)

            # Get the index finger tip x and y
           

                # If index finger is up and middle finger is down
               

                    # Get the points between two known data points using interpolation technique
                    

                    
                    # Move the cursor
                   

                    # Draw the circle on the tip of index finger
                   
    except Exception as e:
        print(e)

    cv2.imshow("Virtual Mouse", cameraFeedImg)
    cv2.waitKey(1)
