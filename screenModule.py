#--------------------------------------------------
#Details
#--------------------------------------------------
#This file is used to store all the different menus in the game.
#This file will also be used to store graphical data. Until I know how to use .config files
#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
from sys import exit
pygame.init()

#--------------------------------------------------
#Graphics text
#This function is used to draw text on demand
#--------------------------------------------------
font = pygame.font.SysFont('comic-sans', 40)
def draw_text(text, font, text_col, x, y):
    #This function will draw the text required, in the font, in the color in the x and y location specified
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
    
#--------------------------------------------------
#Menu functions
#--------------------------------------------------
def menu():
    #This is the main menu. We fill the screen, change the caption, display the discription, and render the objects
    screen.fill("red")
    pygame.display.set_caption('Menu screen')
    draw_text("Platformer Tech Demo", font, 'black', 30, 50)
    for object in buttonObjectModule.menuObjects:
        object.process()
    pygame.display.update()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def options():
    screen.fill("red")
    pygame.display.set_caption("Option menu")
    draw_text("Option menu", font, 'black', 30, 50)
    for object in buttonObjectModule.optionObjects:
        object.process()        
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def changeKeyBinds():
    screen.fill("red")
    pygame.display.set_caption("Keybind menu")
    draw_text("Keybind Menu", font, "black", 30, 50)
    for object in buttonObjectModule.bindObjects:
        object.process()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def scores():
    screen.fill("red")
    pygame.display.set_caption("Score menu")
    draw_text("Score menu", font, 'black', 30, 50)
    for object in buttonObjectModule.scoreObjects:
        object.process()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
def gameOverScreen():
    screen.fill("red")
    pygame.display.set_caption("Game over")
    draw_text("GAME OVER", font, "black", 20, 20)
    for object in buttonObjectModule.gameOverObjects:
        object.process()
    pygame.display.update()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    #displays the button to go back to the menu
    #displays the game over screen

#--------------------------------------------------
#Graphic data
#--------------------------------------------------
windowLength = 960
windowHeight = 640
screen = pygame.display.set_mode((windowLength, windowHeight)) #This sets the games screen size/resolution
fpsSet = 60