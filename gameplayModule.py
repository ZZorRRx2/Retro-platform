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
from playerSpriteClassModule import *
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
    rightModifier = False
    leftModifier = False
    upModifier = False
    downModifier = False
    jumpModifier = False
    dashModifier = False
    gunModifier = False
    swordModifier = False
    idleState = True
    
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[input_map["move right"]]:
        rightModifier = True
        idleState = False
    if pressed_keys[input_map["move left"]]:
        leftModifier = True
        idleState = False
    if pressed_keys[input_map["jump up"]]:
        jumpModifier = True
        idleState = False
    if pressed_keys[input_map["move dash"]]:
        dashModifier = True
        idleState = False
    if pressed_keys[input_map["hold up"]]:
        upModifier = True
        idleState = False
    if pressed_keys[input_map["hold down"]]:
        downModifier = True
        idleState = False
    if pressed_keys[input_map["gun attack"]]:
        gunModifier = True
        idleState = False
    if pressed_keys[input_map["sword attack"]]:
        swordModifier = True
        idleState = False
        
    if rightModifier == True and dashModifier == True:
        print("dash right")
    if rightModifier == True:
        playerSpriteClassModule.Player.rightMove(playerSpriteClassModule.player)
        
    if leftModifier == True and dashModifier == True:
        print("dash left")    
    if leftModifier == True:
        playerSpriteClassModule.Player.leftMove(playerSpriteClassModule.player)
    
    if dashModifier == True and jumpModifier == True:
        print("dash jump")
    if dashModifier == True:
        print("dash")    
        
    if jumpModifier == True:
        print("jump")
        
    if gunModifier == True:
        print("gun shot")
    
    if swordModifier == True and upModifier == True:
        print("up variation attack")
    if swordModifier == True and downModifier == True:
        print("down variation attack")
    if swordModifier == True:
        print("sword attack")
    #We need an update
    playerSpriteClassModule.all_sprites.draw(screen)
    pygame.display.update()

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
#Keybinding Variables
#--------------------------------------------------
input_map = {"move right": pygame.K_d, "move left": pygame.K_a, "jump up": pygame.K_SPACE, "move dash": pygame.K_LSHIFT, "hold up": pygame.K_w, "hold down": pygame.K_s, "gun attack": pygame.K_j, "sword attack": pygame.K_k}