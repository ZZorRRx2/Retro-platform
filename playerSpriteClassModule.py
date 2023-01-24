#--------------------------------------------------
#Details
#--------------------------------------------------
#This is the player sprite class

#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
import screenModule
import inputModule
from sys import exit
pygame.init()

#--------------------------------------------------
#Player Class
#--------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("graphics/Player/stand1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (windowLength/10.26737967914439, windowHeight/5.967365967365967))
        self.hitboxImage = pygame.image.load("graphics/Player/zeroSlash.png").conver_alpha()
        hero_pos_x = 75
        hero_pos_y = 480
        self.rect = self.image.get_rect(topleft = (hero_pos_x,hero_pos_y))        
        self.rect.centerx = windowLength / 2
        self.rect.bottom = windowHeight - 10
        self.speedx = 0
        self.speedy = 0
        #orginal seize (34x39)
        #full resolution is 960, 640
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def playerMove(self, x , y):
        self.rect.x += x
        self.rect.y += y
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
players = pygame.sprite.Group() 
player = Player()
player.rect.x = 75
player.rect.y = 480
players.add(player) 
all_sprites.add(player)