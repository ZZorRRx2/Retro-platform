#--------------------------------------------------
#Details
#--------------------------------------------------
#This is the game section of code where it's actually really horrible. I hate it here.

#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
import playerSpriteClassModule
from playerSpriteClassModule import Player
from sys import exit
pygame.init()
font = pygame.font.SysFont('comic-sans', 40)#Personally i don't know why this is here. But in my defence this line of code is technically importing comic sans. So i'm going to leave it here and you can't stop me

#--------------------------------------------------
#Functions
#--------------------------------------------------     
def gameplay():#This is going to live here for the time being. This is going to be it's py file. afterwards all the py files will be turned into a pak file. Hopefully. If it even uses pak files
    #(xLocation, yLocation,xSize,Ysize)
    #full resolution is 960, 640
    #this will display the images
    screen.fill("black")
    pygame.draw.rect(screen,"grey" , (0,0,windowLength/18.2,windowHeight))#left Wall
    pygame.draw.rect(screen,"grey" , (windowLength/1.05,0,windowLength/18.2,windowHeight))#right Wall
    pygame.draw.rect(screen,"grey", (0,0,windowLength,windowHeight/10.67))#ceiling
    pygame.draw.rect(screen,"grey",(0,windowHeight/1.10344,windowLength,windowHeight/10.67))#floor
    pygame.display.set_caption('Mega Matt Zero/gameplay')
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
    #This checks user inputs
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[input_map["move right"]]:
        playerActionsModule.actionRight()
    if pressed_keys[input_map["move left"]]:
        playerActionsModule.actionLeft()
    if pressed_keys[input_map["jump up"]]:
        playerActionsModule.actionJump()
    if pressed_keys[input_map["move dash"]]:
        playerActionsModule.actionDash()
    if pressed_keys[input_map["hold up"]]:
        playerActionsModule.actionHoldUp()
    if pressed_keys[input_map["hold down"]]:
        playerActionsModule.actionHoldDown()
    if pressed_keys[input_map["gun attack"]]:
        playerActionsModule.actionGunAttack()
    if pressed_keys[input_map["sword attack"]]:
        playerActionsModule.actionSwordAttack
    #We need an update
    playerSpriteClassModule.all_sprites.draw(screen)
    pygame.display.update()

#--------------------------------------------------
#UserInputs
#--------------------------------------------------
def actionRight():
    print("Go right")

def actionLeft():
    print("Go left")
    
def actionDash():
    print("Dash")

def actionJump():
    print("Jump")
    
def actionHoldUp():
    print("hold up")
    
def actionHoldDown():
    print("hold down")
    
def actionGunAttack():
    print("Gun shot")

def actionSwordAttack():
    print("Sword Attack")

#--------------------------------------------------
#State Variables
#--------------------------------------------------
rightModifier = False
LeftModifier = False
upModifier = False
DownModifier = False
jumpModifier = False
dashModifier = False
gunModifier = False
swordModifier = False

#--------------------------------------------------
#Graphics
#--------------------------------------------------
windowLength = 960
windowHeight = 640
screen = pygame.display.set_mode((windowLength, windowHeight)) #This sets the games screen size/resolution
display = pygame.display.get_surface()
pygame.display.set_caption('main action')
clock = pygame.time.Clock() #Makes a clock for it to click
test_font = pygame.font.Font(None, 50) #This imports the font

#--------------------------------------------------
#Hero class varibles
#--------------------------------------------------

#--------------------------------------------------
#Keybinding Variables
#--------------------------------------------------
input_map = {"move right": pygame.K_d, "move left": pygame.K_a, "jump up": pygame.K_SPACE, "move dash": pygame.K_LSHIFT, "hold up": pygame.K_w, "hold down": pygame.K_s, "gun attack": pygame.K_j, "sword attack": pygame.K_k}