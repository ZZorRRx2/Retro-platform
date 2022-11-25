#--------------------------------------------------
#Details
#--------------------------------------------------
#This is the game section of code where it's actually really horrible. I hate it here.

#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
import playerSpriteClassModule
import windowSizeModule
from playerSpriteClassModule import Player
from sys import exit
pygame.init()

#--------------------------------------------------
#Functions
#--------------------------------------------------     
def gameplay():#This is going to live here for the time being. This is going to be it's py file. afterwards all the py files will be turned into a pak file. Hopefully. If it even uses pak files
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit    
    #(xLocation, yLocation,xSize,Ysize)
    #full resolution is 960, 640
    pygame.display.set_caption('Mega Matt Zero/gameplay')
    screen.fill("black")
    pygame.draw.rect(screen,"grey" , (0,0,windowLength/18.2,windowHeight))#left Wall
    pygame.draw.rect(screen,"grey" , (windowLength/1.05,0,windowLength/18.2,windowHeight))#right Wall
    pygame.draw.rect(screen,"grey", (0,0,windowLength,windowHeight/10.67))#ceiling
    pygame.draw.rect(screen,"grey",(0,windowHeight/1.09,windowLength,windowHeight/10.6))#floor
    #This checks user inputs
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[input_map["move right"]]:
        actionRight()
    if pressed_keys[input_map["move left"]]:
        actionLeft()
    if pressed_keys[input_map["jump up"]]:
        actionJump()
    if pressed_keys[input_map["move dash"]]:
        actionDash()
    if pressed_keys[input_map["hold up"]]:
        actionHoldUp()
    if pressed_keys[input_map["hold down"]]:
        actionHoldDown()
    if pressed_keys[input_map["gun attack"]]:
        actionGunAttack()
    if pressed_keys[input_map["sword attack"]]:
        actionSwordAttack
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
windowLength = windowSizeModule.windowLength
windowHeight = windowSizeModule.windowHeight
screen = windowSizeModule.screen
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