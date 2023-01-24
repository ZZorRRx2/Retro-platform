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
import screenModule
import inputModule
from playerSpriteClassModule import *
from sys import exit
pygame.init()
font = pygame.font.SysFont('comic-sans', 40)

#--------------------------------------------------
#Functions
#--------------------------------------------------     
def gameplay():
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
    playerVelX = 0
    playerVelY = 0

    pygame.display.set_caption('Mega Matt Zero/gameplay')
    screen.fill("black")
    for item in furnitureObjects:
        pygame.draw.rect(screen,"grey", item)
    inputModule.checkInput()
    
    #Moves the player 
    if inputModule.rightModifier == True:
        playerVelX += 10
    if inputModule.leftModifier == True:
        playerVelX += -10
    
    #gravity 
    if player.rect.colliderect(floor):
        playerVelY -= playerVelY
    else:
        playerVelY += 10
        
    #collision with enemy
    if player.rect.colliderect(enemyModule.enemy1.rect):
        print("collide")
    #We need an update
    playerSpriteClassModule.Player.playerMove(player, playerVelX, playerVelY)
    playerSpriteClassModule.all_sprites.draw(screen)
    enemyModule.all_sprites.draw(screen)
    healthModule.drawHealth
    pygame.display.update()

#--------------------------------------------------
#Graphics
#--------------------------------------------------
windowLength = screenModule.windowLength
windowHeight = screenModule.windowHeight
screen = screenModule.screen

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

faceRightState = True
playerHealth = healthModule.playerHealth