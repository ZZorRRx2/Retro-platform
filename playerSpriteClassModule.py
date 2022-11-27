#--------------------------------------------------
#Details
#--------------------------------------------------
#This is the player sprite class
#I'm following this tutorial https://www.101computing.net/creating-sprites-using-pygame/
#Well some of that tutorial. not anymore actually.

#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
import windowSizeModule
from sys import exit
pygame.init()

#--------------------------------------------------
#Player Class
#--------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #orginal seize (34x39). We're scalling it to (93.5, 107.25)
        #full resolution is 960, 640
        self.image = pygame.image.load("graphics/Player/stand1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (windowLength/10.26737967914439, windowHeight/5.967365967365967))
        hero_pos_x = 100
        self.rect = self.image.get_rect(topleft = (hero_pos_x,375))        
        self.rect.centerx = windowLength / 2
        self.rect.bottom = windowHeight - 10
        self.speedx = 0        
    
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([windowLength, windowHeight])
        self.image.fill("white")
        self.image.set_colorkey("white")
        
        #orginal seize (34x39)
        #full resolution is 960, 640
        self.image = pygame.image.load("graphics/Player/stand1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (windowLength/10.26737967914439, windowHeight/5.967365967365967))
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()  

    def actionRight():
        print("go right")
    def actionLeft():
        print("go left")
    def actionDash():
        print("dash")
    def actionJump():
        print("jump")
    def actionHoldUp():
        print("hold up")
    def actionHoldDown():
        print("hold down")
    def actionGunAttack():
        print("gun shot")
    def actionSwordAttack():
        print("sword attack")
    rightModifier = False
    LeftModifier = False
    upModifier = False
    DownModifier = False
    jumpModifier = False
    dashModifier = False
    gunModifier = False
    swordModifier = False        
#--------------------------------------------------
#Varibles from other python files,
#Need to find a way to import varibles from other python files more efficently
#News Flash. I did find a way.
#--------------------------------------------------
windowLength = windowSizeModule.windowLength
windowHeight = windowSizeModule.windowHeight
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