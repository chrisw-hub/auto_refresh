
##How to set-up the macro

#Get the program

You can either download everything from the git manually, or clone the git.

To clone the git :
In the folder you want the program to be, open a terminal (right click then "open in terminal"), then type and enter :
git clone https://github.com/chrisw-hub/auto_refresh.git
It will ask for ur github account info and you need git installed on your PC.


#Install python and packages

You need to install Python aswell as the following packages :
pyautogui
opencv-python
keyboard
pygetwindow

To install python follow this link :
https://www.python.org/downloads/

For the packages open the terminal then write and enter (after installing python):
py -m pip install pyautogui opencv-python keyboard pygetwindow


#Launching and stopping the program

You need to open E7 and go to the secret shop menu before launching.

To run the program (with the terminal), you can open the folder containing the program then open a terminal in the folder (right click in the folder then click on "open in terminal").
Afterwards, write and enter :
py auto_refresh.py

To stop the program long press SPACE, or force interrupt using Ctrl-C (in the terminal).

You can set a limit for the number of refresh you wish to make, by default it is 2000.
To do so, pass an argument when running the program. For instance, to run 5000 refresh, use py auto_refresh.py 5000 instead of py auto_refresh.py.


#Image set-up

You might need to change the images I provide depending on screen resolution and window size.

I personally set the Google Play Emulator to 1920*1080, use a 1920*1080 screen and shrink the Google Play E7 window to the smallest possible size before launching the program.

You can try with these images and configuration. But if it does not work, you will need to take your own screenshots.

During the set-up if you notice the program is about to skip a bookmark, I recommand alt-tabbing immediately to avoid it.



##Important remarks 

The program is designed to work on Google Play Emulator. It should work fine on other emulators.
However, it won't work on the PC Client as it prevents macro.

If there is a pop-up (sanctuary missions for instance), the program will continue running but won't be able to refresh or buy.
You can stop your missions if you want to refersh for a long time.

The program will print in the terminal skystones spent, refresh done etc.

