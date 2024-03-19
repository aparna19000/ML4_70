import cv2
from cvzone.HandTrackingModule import HandDetector

import pyautogui
import numpy as np
import math


width = 640
height = 480
frameR = 100
smoothening = 1


screenSize = pyautogui.size()
screenWidth = screenSize[0]
screenHeight = screenSize[1]

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

            if len(lmList) > 0:
                indexFingerTipX = lmList[8][0]
                indexFingerTipY = lmList[8][1]

                # Get the middle finger tip x and y
               

                if fingers[1] == 1 and fingers[2] == 0:

                    x3 = np.interp(indexFingerTipX,
                                   (frameR, width-frameR), (0, screenWidth))
                    y3 = np.interp(indexFingerTipY,
                                   (frameR, height-frameR), (0, screenHeight))

                    currX = prevX + (x3 - prevX)/smoothening
                    currY = prevY + (y3 - prevY) / smoothening

                    pyautogui.moveTo(currX, currY)

                    cv2.circle(cameraFeedImg, (indexFingerTipX, indexFingerTipY),
                               15, (0, 255, 0), cv2.FILLED)

                    prevX = currX
                    prevY = currY

                # If index finger & middle finger both are up
                

                    # Get the center point of the two fingers
                  
                    # Draw the line between two fingers
                  
                    # If both fingers are really close to each other
                   
                        # Perform Click
                        

    except Exception as e:
        print(e)

    cv2.imshow("Virtual Mouse", cameraFeedImg)
    cv2.waitKey(1)
