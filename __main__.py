#--------------------------------------------------
#Details
#--------------------------------------------------
#I'm going to through each python file and rework on them because right now this whole entire project is in such a mess
#Once we're done "pyinstaller your_program.py"
#This is the main section of code where we all come together as one big happy bug
#Say hello, Matthew To. That should hopefully save me from plagerism checks. Please this is my code. Apart from the button.
#Also if you're not Matthew To. You probably shouldn't be editing this. Just make a comment or a suggestion for an improvement.

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