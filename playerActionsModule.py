#--------------------------------------------------
#Details
#--------------------------------------------------
#This module of my code will be used for moving the player around

#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
from sys import exit
pygame.init()

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
    upModifier = True
    print("hold up")
    print(upModifier)
    
def actionHoldDown():
    print("hold down")
    
def actionGunAttack():
    print("Gun shot")

def actionSwordAttack():
    print("Sword Attack")

#--------------------------------------------------
#State Variables
#--------------------------------------------------
upModifier = False
DownModifier = False
inAirModifier = False
dashModifier = False
