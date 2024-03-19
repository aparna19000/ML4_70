Click the Cursor
=======================

In this activity, you will learn to click the cursor using the virtual mouse.



<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/2071954/images/10502657/Slide_8_GIF_B.gif" width = "480" height = "320">






Follow the given steps to complete this activity:


1. Check finger position


* Check if the index finger and middle finger are up using the condition.
     
        ` if fingers[1] == 1 and fingers[2] == 1:`
                     


* Calculate the distance between the index finger and middle finger.


    `distance = math.dist(lmList[8], lmList[12])`


* Find the tip of the index finger and middle finger from the `lmList`.  


    `indexFingerTipX = lmList[8][0]`


    `indexFingerTipY = lmList[8][1]`
   




    `middleFingerTipX = lmList[12][0]`


    `middleFingerTipY = lmList[12][1]`


* Find the center point of the two fingers.
   
    `cx = (indexFingerTipX + middleFingerTipX) // 2`


    `cy = (indexFingerTipY + middleFingerTipY) // 2`


* Use the `cv2.line()` and pass `cameraFeedImg`, index finger tips and middle finger tips to it to draw a line.


  `cv2.line(cameraFeedImg, (indexFingerTipX, indexFingerTipY), (middleFingerTipX, middleFingerTipY), (255, 0, 255), 2)`


2. Perform Click


* Check if the distance is less than 20.


  `if distance < 20:`


* Use the `cv2.circle` to create a circle in the camera feed.  
                       
  `cv2.circle(cameraFeedImg, (cx, cy), 15, (0, 255, 0), cv2.FILLED)`


* Use the `pyautogui.click()`  to perform the click.


  `pyautogui.click()`
 
* Save and run the code to check the output.