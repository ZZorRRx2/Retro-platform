#--------------------------------------------------
#Details
#--------------------------------------------------

#This section module of my code is about the inputs into the game. Such as keyboard inputs.
#tutorial for having different keybinds is from https://stackoverflow.com/questions/47855725/pygame-how-can-i-allow-my-users-to-change-their-input-keys-custom-keybinding

#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((300,200))
input_map = {'move right': pygame.K_d, 'move left': pygame.K_a}

while True:
        for event in pygame.event.get(): #This goes through a loop to check every input in the game
                if event.type == pygame.QUIT: #This is when someone tries to exit the game
                        pygame.quit() #Stops pygame
                        exit() #Ends the loop
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[input_map['move right']]:
                #print("move right")
                right_function
        elif pressed_keys[input_map['move left']]:
                #print("move left)
                left_function
        print(combined_list)