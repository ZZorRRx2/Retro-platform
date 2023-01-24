#--------------------------------------------------
#Details
#--------------------------------------------------
#I'm going to through each python file and rework on them because right now this whole entire project is in such a mess
#Once we're done "pyinstaller your_program.py"
#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
import screenModule
import buttonFunctionModule
import gameplayModule
from sys import exit
pygame.init()

#--------------------------------------------------
#Graphics
#This sets the bare skeleton for the screen to  operate in.
#--------------------------------------------------
clock = pygame.time.Clock() #Makes a clock for it to click
screen = screenModule.screen
pygame.display.set_caption('main action')

#--------------------------------------------------
#Main loop
#In this main loop we check when to run the different screens
#--------------------------------------------------
while True:
        pygame.display.update() #Updates the screen
        clock.tick(screenModule.fpsSet) #Fps is set
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT: #This is when someone tries to exit the game
                        pygame.quit() 
                        exit()   
        if buttonFunctionModule.menuRun == True:
                screenModule.menu()              
        if buttonFunctionModule.optionsRun == True:
                screenModule.options()                
        if buttonFunctionModule.scoreRun == True:
                screenModule.scores()
        if buttonFunctionModule.gameRun == True:
                gameplayModule.gameplay()                
        if buttonFunctionModule.bindsRun == True:
                screenModule.changeKeyBinds()
        if buttonFunctionModule.endGameRun == True:
                screenModule.gameOverScreen()