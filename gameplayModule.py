#--------------------------------------------------
#Details
#--------------------------------------------------
#This is the main section of code where we all come together as one big happy bug
#Say hello, Matthew To. That should hopefully save me from plagerism checks. Please this is my code. Apart from the button.
#Also if you're not Matthew To. You probably shouldn't be editing this. Just make a comment or a suggestion for an improvement.

#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
import playerActionsModule
import buttonObjectModule
from sys import exit
pygame.init()
font = pygame.font.SysFont('comic-sans', 40)#Personally i don't know why this is here. But in my defence this line of code is technically importing comic sans. So i'm going to leave it here and you can't stop me

#--------------------------------------------------
#Functions
#--------------------------------------------------
def gameplay():#This is going to live here for the time being. This is going to be it's py file. afterwards all the py files will be turned into a pak file. Hopefully. If it even uses pak files
    #(xLocation, yLocation,xSize,Ysize)
    screen.fill("blue")
    pygame.draw.rect(screen,"grey" , (0,0,50,640))
    pygame.draw.rect(screen,"grey" , (910,0,50,640))
    pygame.draw.rect(screen,"grey", (0,0,910,50))
    pygame.draw.rect(screen,"grey",(0,580,910,60))
    pygame.display.set_caption('Mega Matt Zero/gameplay')
    pygame.display.update()
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
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
        playerActionsModule.actionSwordAttack()

#--------------------------------------------------
#Graphics
#--------------------------------------------------
windowLength = 960
windowHeight = 640
screen = pygame.display.set_mode((windowLength, windowHeight)) #This sets the games screen size/resolution
pygame.display.set_caption('main action')
clock = pygame.time.Clock() #Makes a clock for it to click
test_font = pygame.font.Font(None, 50) #This imports the font

#--------------------------------------------------
#Keybinding Variables
#--------------------------------------------------
input_map = {"move right": pygame.K_d, "move left": pygame.K_a, "jump up": pygame.K_SPACE, "move dash": pygame.K_LSHIFT, "hold up": pygame.K_w, "hold down": pygame.K_s, "gun attack": pygame.K_j, "sword attack": pygame.K_k}

