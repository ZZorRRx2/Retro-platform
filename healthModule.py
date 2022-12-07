#--------------------------------------------------
#Details
#--------------------------------------------------
#This will be our health manager
#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
import buttonFunctionModule
import dynamicRankingModule
import windowSizeModule
from buttonObjectModule import Button

#--------------------------------------------------
#Functions
#--------------------------------------------------
def healthMinus(healthDeduction):
    global playerHealth
    print("minus health")
    #A function to lower the dynamic ranking
    playerHealth = playerHealth - healthDeduction
    
    
def healthGone():
    if playerHealth <=  0:
        print("gameOver")
        #directs me to the game over screen
        buttonFunctionModule.endGameRun
        
def drawHealth():
    windowSizeModule.draw_text(playerHealth, font, "green", 30, 50)

#--------------------------------------------------
#Varibles
#--------------------------------------------------
playerHealth = 100