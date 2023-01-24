#--------------------------------------------------
#Details
#--------------------------------------------------
#This module of my code will be used for the dynamic ranking system
#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
import screenModule
from sys import exit
font = pygame.font.SysFont('comic-sans', 40)
pygame.init()

#--------------------------------------------------
#Functions
#--------------------------------------------------
def scoreUp(amountScore):
    global currentScore
    currentScore = currentScore + amountScore
    print(currentScore)
def scoreDown(amountScore):
    global currentScore
    currentScore = currentScore - amountScore
    print(currentScore)
    
def rankCheck():
    global currentScore
    if currentScore <= 10:
        currentRank = "E"
        draw_text(currentRank, font, "Blue", 30, 50)
    elif currentScore >= 10:
        currentRank = "D"
        draw_text(currentRank, font, "blue", 30, 50)
    elif currentScore >= 20:
        currentRank = "C"
        draw_text(currentRank, font, "blue", 30, 50)
    elif currentScore >= 30:
        currentRank = "B"
        draw_text(currentRank, font, "blue", 30, 50)
    elif currentScore >= 45:
        currentRank = "A"
    elif currentScore >= 60:
        currentRank = "S"
    elif currentScore >= 75:
        currentRank = "SS"
    elif currentScore >= 90:
        currentRank = "SSS"
        
    
#--------------------------------------------------
#Graphics texts
#--------------------------------------------------
def draw_text(text, font, text_col, x, y): #This function prints text
    img = font.render(text, True, text_col)
    windowSizeModule.screen.blit(img, (x,y))
    
#--------------------------------------------------
#Variables
#--------------------------------------------------
currentScore = 0
currentRank = "E"
rankIndicatorLocation = (0,0)
#--------------------------------------------------
#Main program
#--------------------------------------------------