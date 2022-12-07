#--------------------------------------------------
#Details
#--------------------------------------------------
#This is just a python file to store a varible
#It's pretty funny actually
#With this I don't have to state the same varibles again.
#This is slowly turning into a graphics module

#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame

#--------------------------------------------------
#Graphics texts
#--------------------------------------------------
def draw_text(text, font, text_col, x, y): #This function imports text
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
    
#--------------------------------------------------
#Graphic data
#--------------------------------------------------
windowLength = 960
windowHeight = 640
screen = pygame.display.set_mode((windowLength, windowHeight)) #This sets the games screen size/resolution