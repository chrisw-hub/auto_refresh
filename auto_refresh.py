
"""
Created in 2021
author Ailis

"""

from pyautogui import *
import pyautogui #pip install pyautogui
import time
import random
import keyboard #pip install keyboard
import pygetwindow as gw

#On a aussi besoin de OpenCV (pip install opencv-python)
#Le pgramme ne prend pas en compte les golds / skystones restant. Mais lorsque les golds sont insuffisants le programme va juste tourner ds le vide sans faire n'importe quoi. Sinon les missions de déploiement lorsqu'elles pop font aussi tourner le pgramme ds le vide.
#Les images doivent être dans le même dossier que le programme

#Fonctionnalités futures : set skystones limit, deal with dispatch missions.


##Fail-Safes

#After each pyautogui instruction waits 0.35 sec
pyautogui.PAUSE = 0.35
#If you drag your mouse to the upper left will abort program
pyautogui.FAILSAFE = False

def focus_window(window_title):

    window = gw.getWindowsWithTitle(window_title)[0]
    window.activate()

    left=window.left
    width = window.width
    height = window.height
    top=window.top

    time.sleep(0.2)
    pyautogui.click(left+width//2+width*0.1,top+height//2)  # This may help in some cases to ensure focus


def locateandclick(path,conf=0.9):
    try :
        point=pyautogui.locateCenterOnScreen(path,confidence=conf)
        pyautogui.click(x=point[0], y=point[1], clicks=2, interval=0.08, button="left")
    except :
        #print("Image "+ path + " not found. Could not click" )
        pass

def getlocation(path,conf=0.9):
    try : 
        point=pyautogui.locateCenterOnScreen(path,confidence=conf)
        return point
    except :
        #print("Image "+path +" not found.")
        pass

def rdwait(a,b): #procédure qui fait attendre une valeur de tps aléatoire entre a et b (a,b des réels)
    x=random.uniform(a,b)
    time.sleep(x)

##Set-up

#number of drags
scroll_cont=0
#number of coven bought
cont_coven=0
#number of mystic bought
cont_mystic=0
#number of refresh done
cont_refresh=0
#to avoid some bugs, we can only have one cove / one mystic per refresh
intcont_coven=0
intcont_mystic=0
#focus on correct window
#focus_window("에픽세븐")
focus_window("Epic Seven")

active_window = gw.getActiveWindow()
#get the width and height of the active window
if active_window:
    width = active_window.width
    height = active_window.height
    left=active_window.left
    top=active_window.top
    center=(left+width//2,top+height//2)
 
print("active window dimension", width,height,top,left,center)

start=time.time()

##Loop

while keyboard.is_pressed('space') == False: #Long press space to stop
    
    coven_point=getlocation('covens.png',0.90)
    mystic_point=getlocation("mystics.png",0.90)

#Checks for covenant
    if intcont_coven==0 and coven_point is not None :
 
        point=getlocation('buy_cov_bis.png',0.96)
        pyautogui.click(x=point[0],y=point[1]+height//20, clicks=2, interval=0.08, button="left")
        print("Covenants located")
        time.sleep(0.2)
        locateandclick('buy_button_cov.png',0.96)

        cont_coven+=1
        intcont_coven+=1

#Checks for mystic
    if mystic_point is not None and intcont_mystic==0:
        
        point=getlocation('buy_mystic_bis.png',0.96)
        pyautogui.click(x=point[0],y=point[1]+height//20, clicks=2, interval=0.08, button="left")
        print("Mystics located")
        time.sleep(0.2)
        locateandclick('buy_button_myst.png',0.96)

        cont_mystic+=1
        intcont_mystic+=1

    coven_point=None
    mystic_point=None

    if scroll_cont>=1 :

        locateandclick("refresh.png")
        rdwait(0.2,0.3)
        locateandclick("confirm.png") 
       
        scroll_cont=0
        intcont_mystic=0
        intcont_coven=0
        rdwait(0.3,0.4)
        cont_refresh+=1

        print("Covenant Summons bought =",cont_coven)
        print("Mystic Summons bought =",cont_mystic)
        print("Refresh Done =",cont_refresh)
        print("Systones spend =", cont_refresh*3)
        print("Time Spent =", time.time()-start, "secondes")
        print("")

    else :
        pyautogui.moveTo(center[0]+width*0.1, center[1]+height*0.3, duration=0.01)
        pyautogui.dragTo(center[0]+width*0.1, center[1]-height*0.2, duration=0.15)
        scroll_cont+=1              

##Outside of the while loop
print("You exited successfuly")
                                              