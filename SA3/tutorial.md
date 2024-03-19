Scroll and Take Screenshots using Fingers
==========================================


In this activity, you will learn to scroll down and take screenshots using finger movements.




<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/2071954/images/10502651/Slide_8_GIF_C.gif" width = "480" height = "320">






Follow the given steps to complete this activity:


1. Scroll down the screen


* Check if the other fingers are up except the thumb .
     
    `if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:`


* Use `time.sleep(.1)` to hold the screen for a millisecond.
     
    `time.sleep(.1)`


* Use  `pyautogui.scroll(300)` to scroll the screen by value 300.


    `pyautogui.scroll(300)`
                     
                    
3. Take the screen shot


* Check if all the fingers are down.


    `if fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:`


* Declare a `screenshotPath` variable and save the screenshot path in it.
    ` screenshotPath = f'screenshots/screenshot_{screenshotNum}.png'
                   
   
* Use `pyautogui.screenshot(screenshotPath)` to take and save the screenshot.


    ` pyautogui.screenshot(screenshotPath)`




* Increase the `screenshotNum` count by `1`.
   
    `screenshotNum += 1`


* Print the saved screenshot path.


    `print(f'Screenshot saved at {screenshotPath}')`


* Use `time.sleep(1)` to show the screenshot on the screen for a second.


    `time.sleep(1)`


* Save and run the code to check the output.