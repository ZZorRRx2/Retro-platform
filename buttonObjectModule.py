#--------------------------------------------------
#Details
#--------------------------------------------------
#This module is for the buttons class

#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
import buttonFunctionModule
import windowSizeModule
from sys import exit
pygame.init()
font = pygame.font.SysFont('comic-sans', 40)#Personally i don't know why this is here. But in my defence this line of code is technically importing comic sans. So i'm going to leave it here and you can't stop me

#--------------------------------------------------
#Button functions
#--------------------------------------------------
#I've just made some edits to it make it suit better for my program
class Button(): # This code is taken from = https://www.thepythoncode.com/article/make-a-button-using-pygame-in-python
    #I've just made some edits to it make it suit better for my program
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
                    'normal': "red",
                'hover': '#666666',
            'pressed': '#333333',
                }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

    def process(self):

        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
                    self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
                self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
                ])
        screen.blit(self.buttonSurface, self.buttonRect)
        
#--------------------------------------------------
#Button Variables
#--------------------------------------------------
toGameButton = Button(30, 175, 225, 60, 'Enter game', buttonFunctionModule.openGame)
toOptionButton = Button(30, 250, 225, 60, 'Options', buttonFunctionModule.openOptions)
toScoresButton = Button(30, 325, 225, 60, 'Scores', buttonFunctionModule.openScores)
toExitGameButton = Button(30, 575, 225, 60, 'Exit Game', buttonFunctionModule.killGame)

keyBindButton = Button(285, 250, 225, 60, 'Keybindings', buttonFunctionModule.openBinds)
backToOptions = Button(30, 250, 225, 60, 'Back To Options', buttonFunctionModule.openOptions)
backToMenu = Button(30, 400, 225, 60, 'Back', buttonFunctionModule.openMenu)

menuObjects = [toGameButton, toOptionButton, toScoresButton, toExitGameButton]
optionObjects = [toGameButton, toOptionButton, toScoresButton, toExitGameButton, keyBindButton, backToMenu]
scoreObjects = [toGameButton, toOptionButton, toScoresButton, toExitGameButton, backToMenu]
bindObjects = [toGameButton, toOptionButton, toScoresButton, toExitGameButton, backToMenu]

#--------------------------------------------------
#Window varibles
#--------------------------------------------------
windowLength = windowSizeModule.windowLength
windowHeight = windowSizeModule.windowHeight
screen = windowSizeModule.screen