Move the cursor
===============


In this activity, you will learn to move the cursor with the tip of the index finger.



<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/2071954/images/10502659/Slide_8.gif" width = "480" height = "320">




Follow the given steps to complete this activity:
1. Import the libraries


* Open file main.py.


* Import `pyautogui` to use to control the mouse.

* Import `time` module to use the time.

* Import `numpy` to deal with the data.

    `import pyautogui`
    `import time`
    `import numpy as np`
`
       
* Declare variables `width` with value `640`, `height` with value `480`.

    `width = 640`

    `height = 480`
   


 2. Check finger position

*  Check if the coordinates are in the `lmList` by cheking if its lenght is greater than 0.

    `if len(lmList) > 0:`

*  Store the cooridnates of the index finger in `indexFingerTipX` and `indexFingerTipY` variables.

    `indexFingerTipX = lmList[8][0]`

    `indexFingerTipY = lmList[8][1]`

* Check if the index finger is up and middle finger is down using the if condition.
     
    ` if fingers[1] == 1 and fingers[2] == 0:`
                     


* Use the `np.interp()` function for interpolation of `x3` and `y3` points.


    `x3 = np.interp(indexFingerTipX, (frameR,width-frameR), (0,screenWidth))`
    `y3 = np.interp(indexFingerTipY, (frameR, height-frameR), (0, screenHeight))`


* Smoothen the values of current X and current Y points to smoothen the video.  


  `currX = prevX + (x3 - prevX)/smoothening`
  `currY = prevY + (y3 - prevY) / smoothening`
   
* Use `pyautogui.moveTo()` and pass `currX, currY` to move the cursor.


    `pyautogui.moveTo(currX, currY)`
   
* Draw the circle on the tip of index finger.

    `cv2.circle(cameraFeedImg, (indexFingerTipX, indexFingerTipY),15, (0, 255, 0), cv2.FILLED)`

* Save and run the code to check the output.
Follow the given steps to complete this activity:
1. Import the libraries


* Open file main.py.


* Import `pyautogui` to use to control the mouse.
* Import `time` module to use the time.
* Import `numpy` to deal with the data.
    `import pyautogui`
    `import time`
    `import numpy as np`
`
       
* Declare variables `width` with value `640`, and `height` with value `480`
    `width = 640`
    `height = 480`
   


 2. Check finger position


*  Check if the coordinates are in the lmList by checking if its length is greater than 0.

    `if len(lmList) > 0:`

* Store the coordinates of the index finger in `indexFingerTipX` and `indexFingerTipY` variables.

    `indexFingerTipX = lmList[8][0]`

    `indexFingerTipY = lmList[8][1]`

* Check if the index finger is up and the middle finger is down using the if condition.
     
    ` if fingers[1] == 1 and fingers[2] == 0:`
                     


* Use the `np.interp()` function for interpolation of `x3` and `y3` points.


    `x3 = np.interp(indexFingerTipX, (frameR,width-frameR), (0,screenWidth))`
    `y3 = np.interp(indexFingerTipY, (frameR, height-frameR), (0, screenHeight))`


* Smoothen the values of current X and current Y points to smoothen the video.  


  `currX = prevX + (x3 - prevX)/smoothening`
  `currY = prevY + (y3 - prevY) / smoothening`
   
* Use `pyautogui.moveTo()` and pass `currX, currY` to move the cursor.

    `pyautogui.moveTo(currX, currY)`

* Draw the circle on the tip of your index finger.

    `cv2.circle(cameraFeedImg, (indexFingerTipX, indexFingerTipY),15, (0, 255, 0), cv2.FILLED)`


* Save and run the code to check the output.




