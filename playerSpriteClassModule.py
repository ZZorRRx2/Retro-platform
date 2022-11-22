#--------------------------------------------------
#Details
#--------------------------------------------------
#This is the player sprite class
#I'm following this tutorial https://www.101computing.net/creating-sprites-using-pygame/

#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
from sys import exit
pygame.init()

#--------------------------------------------------
#Imports
#--------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("graphics/Player/stand1.jpg").convert_alpha()
        ship_pos_x = 100
        self.rect = self.image.get_rect(topleft = (ship_pos_x,375))        
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0        
    
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        # Draw the car (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.image = pygame.image.load("graphics/Player/stand1.jpg").convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
