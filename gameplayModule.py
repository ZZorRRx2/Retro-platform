#--------------------------------------------------
#Details
#--------------------------------------------------
#This is the game section of code where it's actually really horrible. I hate it here.

#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
import enemyModule
import healthModule
import dynamicRankingModule
import playerSpriteClassModule
import windowSizeModule
from playerSpriteClassModule import *
from sys import exit
pygame.init()
font = pygame.font.SysFont('comic-sans', 40)

#--------------------------------------------------
#Functions
#--------------------------------------------------     
def gameplay():#This is going to live here for the time being. This is going to be it's py file. afterwards all the py files will be turned into a pak file. Hopefully. If it even uses pak files
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit    
    pygame.display.set_caption('Mega Matt Zero/gameplay')
    screen.fill("black")
    for item in furnitureObjects:
        pygame.draw.rect(screen,"grey", item)
    
    #This checks user inputs
    rightModifier = False
    leftModifier = False
    upModifier = False
    downModifier = False
    jumpModifier = False
    dashModifier = False
    gunModifier = False
    swordModifier = False
    
    #User states
    global idleState 
    global collideWallState 
    global jumpAccel
    global faceRightState
    global swordState
    global jumpState
    global gravity
    global playerV
    
    #This checks for user inputs 
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
    
    #Right and left movement on the floor
    if rightModifier == True:
        playerSpriteClassModule.Player.playerMove(character, 10, 0)
    if leftModifier == True:
        playerSpriteClassModule.Player.playerMove(character, -10, 0)
    
    #Jumping control
    #Instead of binding the time the user can jump into the air. I'm going to bind it to acceleration. A side effect of this is that this is that the jump height could essentially be binded to the clock speed of the program. But I don't really care at this point. This is going to be a permenant temporary fix.
    if jumpModifier == True:
        if jumpState == True:
            if jumpAccel >= -30:
                jumpAccel -= 2.5
                playerSpriteClassModule.Player.playerMove(character, 0, jumpAccel)
            else:
                jumpAccel = 0
                jumpState = False            
                
    if player.rect.colliderect(rightWall):
            playerSpriteClassModule.Player.playerMove(character, -10, 0)
            
    if player.rect.colliderect(leftWall):
            playerSpriteClassModule.Player.playerMove(character, 10, 0)
            
    #Gravity works only when we are in the air        
    if player.rect.colliderect(floor):
        jumpState = True
    else:
        if player.rect.colliderect(rightWall):
            faceRightState = False
            playerSpriteClassModule.Player.playerMove(character, 0, 5)
        elif player.rect.colliderect(leftWall):
            faceRightState = True
            playerSpriteClassModule.Player.playerMove(character, 0, 5)
        else:
            playerSpriteClassModule.Player.playerMove(character, 0, 5)
        
    #We need an update
    playerSpriteClassModule.all_sprites.draw(screen)
    healthModule.drawHealth
    pygame.display.update()

#--------------------------------------------------
#Graphics
#--------------------------------------------------
windowLength = windowSizeModule.windowLength
windowHeight = windowSizeModule.windowHeight
screen = windowSizeModule.screen

#Furniture Object
leftWall = pygame.Rect((0,0,windowLength/18.2,windowHeight))
rightWall = pygame.Rect((windowLength/1.05,0,windowLength/18.2,windowHeight))
ceiling = pygame.Rect((0,0,windowLength,windowHeight/10.67))
floor = pygame.Rect((0,windowHeight/1.09,windowLength,windowHeight/10.6))
furnitureObjects = [leftWall, rightWall, ceiling, floor]
#character furniture
character = playerSpriteClassModule.player

pygame.display.set_caption('game')
clock = pygame.time.Clock() #Makes a clock for it to click
test_font = pygame.font.Font(None, 50) #This imports the font

#User states
idleState = True
collideWallState = False
faceRightState = True
jumpState = False
jumpAccel = 0
locationState = 0 #Where 0 is on the floor, 1 is in the air, and 2 is at the wall
swordState = 0
playerHealth = healthModule.playerHealth

#--------------------------------------------------
#Keybinding Variables
#--------------------------------------------------
input_map = {"move right": pygame.K_d, "move left": pygame.K_a, "jump up": pygame.K_SPACE, "move dash": pygame.K_LSHIFT, "hold up": pygame.K_w, "hold down": pygame.K_s, "gun attack": pygame.K_j, "sword attack": pygame.K_k}