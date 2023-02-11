#--------------------------------------------------
#Details
#--------------------------------------------------
#This is the function code for my buttons.
#If I press a button the data and the code is sent to here

#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
#import playerSpriteClassModule
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
    global endGameRun
    menuRun = True
    optionsRun = False
    scoreRun = False
    gameRun = False
    bindsRun = False
    endGameRun = False

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
    '''
    playerSpriteClassModule.player.rect.x = 75
    playerSpriteClassModule.player.rect.y = 480    
    '''
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
def endGame():
    global endGameRun
    global gameRun
    endGameRun = True
    gameRun = False
def killGame():
    pygame.quit()
    exit()
#--------------------------------------------------
#Game state checks
#These boolean values are to change screens and stages in the game.
#--------------------------------------------------
menuRun = True
optionsRun = False
scoreRun = False
gameRun = False
bindsRun = False
endGameRun = False
#For right now we're having the gameRun varible set to True to immediately boot to the game for testing.