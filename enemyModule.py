#--------------------------------------------------
#Details
#--------------------------------------------------
#This is the the enemy module
#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
import projectileModule
import screenModule
pygame.init()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load("graphics/Player/stand1.png").convert_alpha()
        #self.image = pygame.transform.scale(self.image, (windowLength/10.26737967914439, windowHeight/5.967365967365967))
        self.rect = pygame.Rect(100,100,100,100)
        self.image = pygame.Surface((100, 100))
        self.image.fill("white")
        self.rect.centerx = windowLength / 2
        self.rect.bottom = windowHeight - 10
        # Set the background color and set it to be transparent
        # Fetch the rectangle object that has the dimensions of the image.
        
#--------------------------------------------------
#Varibles from other python files,
#--------------------------------------------------
windowLength = screenModule.windowLength
windowHeight = screenModule.windowHeight
screen = pygame.display.set_mode((windowLength, windowHeight)) #This sets the games screen size/resolution

#--------------------------------------------------
#Class varibles
#--------------------------------------------------
all_sprites = pygame.sprite.Group()

#Enemy sprites
enemy1 = Enemy()
enemy1.rect.x = 640
enemy1.rect.y = 480

#Adds each enemy item into their lists.
all_sprites.add(enemy1)