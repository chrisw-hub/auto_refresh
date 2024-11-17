
"""
Created in 2021
author Ailis

"""

from pyautogui import *
import pyautogui #pip install pyautogui
import time
import random
import keyboard #pip install keyboard

#On a aussi besoin de OpenCV (pip install opencv-python)
#Pré-conditions : E7 doit être en full screen, sur le menu du shop, en français (sinon il faut adapter certaines images), accessible d'un simple alt-tab, la résolution de l'écran doit être 1920x1080 (de même il faudra adapter certaines images et certaines valeurs sinon), doit avoir créer des contrôles bluestacks adaptés (pour appuyer sur rafraîchir et confirmer)
#Le pgramme ne prend pas en compte les golds / skystones restant. Mais lorsque les golds sont insuffisants le programme va juste tourner ds le vide sans faire n'importe quoi. Sinon les missions de déploiement lorsqu'elles pop font aussi tourner le pgramme ds le vide.
#Les images doivent être dans Ce PC / -- / Utilisateurs / --

##Fail-Safes

#After each pyautogui instruction waits 0.35 sec
pyautogui.PAUSE = 0.35
#If you drag your mouse to the upper left will abort program
pyautogui.FAILSAFE = True

def focus_window(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        window.activate()
        pyautogui.click()  # This may help in some cases to ensure focus
    except IndexError:

focus_window("Bluestacks")

##Set-up

#Get screen res
pantalla=pyautogui.size()
#Move to center of the screen instantly
pyautogui.moveTo(pantalla[0]/2+150, pantalla[1]/2, duration=random.uniform(0.01,0.03))
#number of drags
cont=0
#number of coven bought
cont_coven=0
#number of mystic bought
cont_mystic=0
#number of refresh done
cont_refresh=0
#to avoid some bugs
intcont_coven=0
intcont_mystic=0

def rdwait(a,b): #procédure qui fait attendre une valeur de tps aléatoire entre a et b (a,b des réels)
    x=random.uniform(a,b)
    time.sleep(x)

##Loop

while keyboard.is_pressed('space') == False: #Long press space to stop
    
    try : 
        Coven_pos=pyautogui.locateOnScreen('covens.PNG',confidence=0.95)
        print('image found')
    
    except :
        Coven_pos = None
        pass

#Search for the price and quantity image of mystic summon
    try :
        Mystic_pos=pyautogui.locateOnScreen('mystics.PNG',confidence=0.90)
        
    except :
        Mystic_pos = None
        pass              

#Checks for covenant
    if (Coven_pos) != None and intcont_coven==0:
        Coven_point=pyautogui.center(Coven_pos)
        pyautogui.click(x=Coven_point[0]+800, y=Coven_point[1]+20, clicks=2, interval=0.05, button='left')
        rdwait(0.55,0.6)#wait for confirm button

        try : 
            Buy_button_Covenant_pos=pyautogui.locateOnScreen('Buy_button_Covenant.PNG')
        except :
            print("Bouton non trouvé")
            break

        Buy_button_Covenant_point=pyautogui.center(Buy_button_Covenant_pos)
        pyautogui.click(x=Buy_button_Covenant_point[0], y=Buy_button_Covenant_point[1], clicks=2, interval=0.05, button='left')
        cont_coven+=1
        intcont_coven+=1

#Checks for mystic
    if (Mystic_pos) != None and intcont_mystic==0:
        Mystic_point=pyautogui.center(Mystic_pos)
        pyautogui.click(x=Mystic_point[0]+800, y=Mystic_point[1]+30, clicks=2, interval=0.05, button='left')
        rdwait(0.55,0.6)#wait for confirm button

        try :
            Buy_button_Mystic_pos=pyautogui.locateOnScreen('Buy_button_Mystic.PNG')
        except :
            print("Bouton non trouvé")
            break
            

        Buy_button_Mystic_point=pyautogui.center(Buy_button_Mystic_pos)
        pyautogui.click(x=Buy_button_Mystic_point[0], y=Buy_button_Mystic_point[1], clicks=2, interval=0.05, button='left')
        cont_mystic+=1
        intcont_mystic+=1

    Coven_pos=None  
    Mystic_pos=None

    if cont>=1 :
        rdwait(0.1,0.15)
        pyautogui.press('q')
        rdwait(0.05,0.07)
        pyautogui.press('q')#raccourci bluestacks qui appuie sur le bouton raffraichir
        rdwait(0.4,0.45)#wait for confirm to appear
        pyautogui.press('s')
        rdwait(0.05,0.07)
        pyautogui.press('s')#raccourci bluestacks qui appuie sur le bouton confirmer
        cont=0
        intcont_mystic=0
        intcont_coven=0
        rdwait(1.0,1.05)
        cont_refresh+=1

    else :
        pyautogui.moveTo(pantalla[0]/2+random.uniform(125,220), pantalla[1]/2+random.uniform(145,165), duration=random.uniform(0.02,0.04))
        #Drag upward 360-400 pixels in 0.15-0.2 seconds
        pyautogui.dragTo(pantalla[0]/2+random.uniform(125,220), pantalla[1]/2-random.uniform(370,410), duration=random.uniform(0.15,0.2))
        rdwait(0.8,0.85)
        cont+=1

##Outside of the while loop
print("You exited successfuly")
print("Covenant Summons bought=",cont_coven)
print("Mystic Summons bought=",cont_mystic)
print("Refresh Done=",cont_refresh) #Ce nombre est faux qd le prgramme finit par tourner dans le vide
