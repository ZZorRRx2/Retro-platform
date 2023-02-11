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
        
        hero_pos_x = 75
        hero_pos_y = 480
        self.faceRight = 1
        self.jumpState = 1
        self.timeJump = 0
        
        self.image = pygame.image.load("graphics/Player/stand1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (windowLength/10, windowHeight/6))
        #orginal seize (34x39)
        #scale up is 2.75 to achieve 93.5 and 107
        #full resolution is 960, 640
        self.rect = self.image.get_rect(topleft = (hero_pos_x,hero_pos_y))        
        self.rect.centerx = windowLength / 2
        self.rect.bottom = windowHeight - 10
        
        self.hitboxImage= pygame.image.load("graphics/Player/stand1.png").convert_alpha()
        self.hitboxImage = pygame.transform.scale(self.hitboxImage, (windowLength/10, windowHeight/6))
        self.attackRect = self.hitboxImage.get_rect(topleft = (hero_pos_x,hero_pos_y))
        #original size (74,42)
        #scale up is 2.75 to achieve 204 and 116
        #dividing factor = 5 and 5.52
        
        self.speedx = 0
        self.speedy = 0                
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def playerMove(self, x , y):
        self.rect.x += x
        self.rect.y += y
        self.attackRect.x += x
        self.attackRect.y += y
    '''   
    def faceRightFunc(self):
        self.image = pygame.image.load("graphics/Player/stand1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (windowLength/10, windowHeight/6))
    
    def faceLeftFunc(self):
        self.image = pygame.image.load("graphics/Player/stand1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (windowLength/10, windowHeight/6))
        self.image = pygame.transform.flip(self.image, True, False)
    '''   
    def attackMove(self):
        if self.faceRight == 1:
            self.hitboxImage = pygame.image.load("graphics/Player/zeroSlash.png").convert_alpha()
            self.hitboxImage = pygame.transform.scale(self.hitboxImage, (windowLength/4.71, windowHeight/5.52))
            self.image = pygame.image.load("graphics/Player/zeroSlash.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (windowLength/4.71, windowHeight/5.52))
            
            self.attackRect = self.hitboxImage.get_rect(topleft = (self.rect.x,self.rect.y))
        else:
            self.hitboxImage = pygame.image.load("graphics/Player/zeroSlash.png").convert_alpha()
            self.hitboxImage = pygame.transform.scale(self.hitboxImage, (windowLength/4.71, windowHeight/5.52))
            self.hitboxImage = pygame.transform.flip(self.hitboxImage, True, False)
            self.attackRect = self.hitboxImage.get_rect(topleft = (self.rect.x - 38,self.rect.y))
            self.image = pygame.image.load("graphics/Player/zeroSlash.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (windowLength/4.71, windowHeight/5.52))
            self.image = pygame.transform.flip(self.image, True, False)
    def noAttack(self):
        if self.faceRight == 1:
            self.hitboxImage= pygame.image.load("graphics/Player/stand1.png").convert_alpha()
            self.hitboxImage = pygame.transform.scale(self.hitboxImage, (windowLength/10, windowHeight/6))
            self.attackRect = self.hitboxImage.get_rect(topleft = (self.rect.x,self.rect.y))
            self.image = pygame.image.load("graphics/Player/stand1.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (windowLength/10, windowHeight/6))      
        else:
            self.hitboxImage = pygame.image.load("graphics/Player/stand1.png").convert_alpha()
            self.hitboxImage = pygame.transform.scale(self.hitboxImage, (windowLength/10, windowHeight/6))
            self.hitboxImage = pygame.transform.flip(self.hitboxImage, True, False)
            self.attackRect = self.hitboxImage.get_rect(topleft = (self.rect.x,self.rect.y))
            self.image = pygame.image.load("graphics/Player/stand1.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (windowLength/10, windowHeight/6))
            self.image = pygame.transform.flip(self.image, True, False)
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