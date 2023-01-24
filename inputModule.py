#--------------------------------------------------
#Details
#--------------------------------------------------
#This module checks for imports and returns values.
#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
pygame.init()

#--------------------------------------------------
#Keybinding Variables
#--------------------------------------------------
input_map = {"move right": pygame.K_d, "move left": pygame.K_a, "jump up": pygame.K_SPACE, "move dash": pygame.K_LSHIFT, "hold up": pygame.K_w, "hold down": pygame.K_s, "gun attack": pygame.K_j, "sword attack": pygame.K_k}

rightModifier = False
leftModifier = False
upModifier = False
downModifier = False
jumpModifier = False
dashModifier = False
gunModifier = False
swordModifier = False

#This checks for user inputs 
def checkInput():
    global rightModifier
    global leftModifier
    global upModifier
    global downModifier
    global jumpModifier
    global dashModifier
    global gunModifier
    global swordModifier
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[input_map["move right"]]:
        rightModifier = True
    else:
        rightModifier = False
        
    if pressed_keys[input_map["move left"]]:
        leftModifier = True
    else:
        leftModifier = False
        
    if pressed_keys[input_map["jump up"]]:
        jumpModifier = True
    else:
        jumpModifier = False
        
    if pressed_keys[input_map["move dash"]]:
        dashModifier = True
    else:
        dashModifier = False
        
    if pressed_keys[input_map["hold up"]]:
        upModifier = True
    else:
        upModifier = False
        
    if pressed_keys[input_map["hold down"]]:
        downModifier = True
    else:
        downModifier = False
    
    if pressed_keys[input_map["gun attack"]]:
        gunModifier = True
    else:
        gunModifier = False
        
    if pressed_keys[input_map["sword attack"]]:
        swordModifier = True
    else:
        swordModifier = False