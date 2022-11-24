#--------------------------------------------------
#Details
#--------------------------------------------------
#This is the function code for my buttons.
#If I press a button the data and the code is sent to here

#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
from sys import exit

#--------------------------------------------------
#Navigation functions
#--------------------------------------------------
def openMenu():
    global menuRun
    global optionsRun
    global scoreRun
    global gameRun
    global bindsRun
    menuRun = True
    optionsRun = False
    scoreRun = False
    gameRun = False
    bindsRun = False

def openOptions():
    global menuRun
    global optionsRun
    global scoreRun
    global gameRun
    global bindsRun
    menuRun = False
    optionsRun = True
    scoreRun = False
    gameRun = False
    bindsRun = False

def openScores():
    global menuRun
    global optionsRun
    global scoreRun
    global gameRun
    global bindsRun
    menuRun = False
    optionsRun = False
    scoreRun = True
    gameRun = False
    bindsRun = False

def openGame():
    global menuRun
    global optionsRun
    global scoreRun
    global gameRun
    global bindsRun
    menuRun = False
    optionsRun = False
    scoreRun = False
    gameRun = True
    bindsRun = False

def openBinds():
    global menuRun
    global optionsRun
    global scoreRun
    global gameRun
    global bindsRun
    menuRun = False
    optionsRun = False
    scoreRun = False
    gameRun = False
    bindsRun = True

def killGame():
    pygame.quit()
    exit()
#--------------------------------------------------
#Game state checks
#--------------------------------------------------
menuRun = True
optionsRun = False
scoreRun = False
gameRun = False
bindsRun = False