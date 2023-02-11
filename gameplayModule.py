#--------------------------------------------------
#Details
#--------------------------------------------------
#This is the game section of code where it's actually really horrible. I hate it here.

#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
import buttonFunctionModule
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
    bgm = pygame.mixer.Sound("audio/bgm.wav")
    bgm.play(10)

    pygame.display.set_caption('Mega Matt Zero/gameplay')
    screen.fill("black")
    for item in furnitureObjects:
        pygame.draw.rect(screen,"grey", item)
    inputModule.checkInput()
    
    #Moves the player 
    if inputModule.rightModifier == True:
        playerVelX += 10
        playerSpriteClassModule.player.faceRight = 1
    if inputModule.leftModifier == True:
        playerVelX += -10
        playerSpriteClassModule.player.faceRight = 0
    if inputModule.jumpModifier == True:
        if playerSpriteClassModule.player.jumpState == 1:
            playerVelY += -30
            playerSpriteClassModule.player.timeJump += 5
    print(playerSpriteClassModule.player.jumpState, playerSpriteClassModule.player.timeJump)
    if playerSpriteClassModule.player.timeJump == 70:
        playerSpriteClassModule.player.jumpState = 0
        playerSpriteClassModule.player.timeJump = 0
        
    if inputModule.swordModifier == True:
        playerSpriteClassModule.player.attackMove()
    else:
        playerSpriteClassModule.player.noAttack()
    
    #gravity 
    if player.rect.colliderect(floor):
        playerVelY -= playerVelY*0.5
        playerSpriteClassModule.player.jumpState = 1
    else:
        playerVelY += 10
    
    if player.rect.colliderect(rightWall):
        playerSpriteClassModule.player.rect.x = playerSpriteClassModule.player.rect.x - 15
    if player.rect.colliderect(leftWall):
        playerSpriteClassModule.player.rect.x = playerSpriteClassModule .player.rect.x +15
    
    #collision with enemy
    if player.rect.colliderect(enemyModule.enemy1.rect):
        healthModule.playerHealth = healthModule.playerHealth - 10
        
    if player.attackRect.colliderect(enemyModule.enemy1.rect):
        dynamicRankingModule.currentScore = dynamicRankingModule.currentScore + 10
    
    if healthModule.playerHealth == 0:
        buttonFunctionModule.endGame()
        playerSpriteClassModule.player.rect.x = 75
        enemyModule.enemy1.rect.x = 640
    
    #enemy movement
    if playerSpriteClassModule.player.rect.x >= enemyModule.enemy1.rect.x:
        print("do this")
        enemyModule.enemy1.rect.x += 1
    else:
        enemyModule.enemy1.rect.x -= 1
        print("do that")
    
    #We need an update
    playerSpriteClassModule.Player.playerMove(player, playerVelX, playerVelY)
    playerSpriteClassModule.all_sprites.draw(screen)
    enemyModule.all_sprites.draw(screen)
    #show health
    score_font = pygame.font.SysFont("Times New Roman", 30)
    health_Display = score_font.render(str(healthModule.playerHealth), 1, (255,255,255))
    screen.blit(health_Display, (0,0))
    #show score
    score_Display = score_font.render(str(dynamicRankingModule.currentScore), 1, (255,255,255))
    screen.blit(score_Display, (0,30))
    '''
    Not going to be implemented for the time being
    #show rank
    rank_Display = score_font.render(str(dynamicRankingModule.currentRank),1,(255,255,255))
    screen.blit(score_Display, (630,0))
    pygame.display.update()
    '''

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