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
import buttonObjectModule
import buttonFunctionModule
import gameplayModule
import windowSizeModule
from buttonObjectModule import Button
from sys import exit
pygame.init()
font = pygame.font.SysFont('comic-sans', 40)#Personally i don't know why this is here. But in my defence this line of code is technically importing comic sans. So i'm going to leave it here and you can't stop me

#--------------------------------------------------
#Graphics texts
#--------------------------------------------------
def draw_text(text, font, text_col, x, y): #This function imports text
        img = font.render(text, True, text_col)
        windowSizeModule.screen.blit(img, (x,y))
        
#--------------------------------------------------
#Menu functions
#--------------------------------------------------
def menu():
        screen.fill("red")
        pygame.display.set_caption('Mega Matt Zero')
        draw_text("C:Mega Matt Zero/", font, 'black', 30, 50)
        for object in buttonObjectModule.menuObjects:
                object.process()
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
        
def options():
        screen.fill("red")
        pygame.display.set_caption('Mega Matt Zero/options_menu')
        draw_text("C:Mega Matt Zero/options_menu", font, 'black', 30, 50)
        for object in buttonObjectModule.optionObjects:
                object.process()        
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

def changeKeyBinds():
        screen.fill("red")
        pygame.display.set_caption("Mega Matt Zero/options_menu/keybind_menu")
        draw_text("C:Mega Matt Zero/options_menu/keybind_menu", font, "black", 30, 50)
        for object in buttonObjectModule.bindObjects:
                object.process()
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

def scores():
        screen.fill("red")
        pygame.display.set_caption("Mega Matt Zero/score_menu")
        draw_text("C:Mega Matt Zero/score_menu", font, 'black', 30, 50)
        for object in buttonObjectModule.scoreObjects:
                object.process()
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
def killGame():
        pygame.quit()
        exit()
        
#--------------------------------------------------
#Graphics
#--------------------------------------------------
screen = windowSizeModule.screen
pygame.display.set_caption('main action')
clock = pygame.time.Clock() #Makes a clock for it to click

#--------------------------------------------------
#Main loop
#--------------------------------------------------
while True: #This manages where the game is going to run. Menu, options or the game.
        pygame.display.update() #This will constantly update the screen
        clock.tick(60) #Sets the frame rate to 60 
        for event in pygame.event.get(): #This goes through a loop to check every input in the game
                if event.type == pygame.QUIT: #This is when someone tries to exit the game
                        pygame.quit() #Stops pygame
                        exit() #Ends the loop    
        if buttonFunctionModule.menuRun == True:
                menu()
                
        if buttonFunctionModule.optionsRun == True:
                options()
                
        if buttonFunctionModule.scoreRun == True:
                scores()
                
        if buttonFunctionModule.gameRun == True:
                gameplayModule.gameplay()
                
        if buttonFunctionModule.bindsRun == True:
                changeKeyBinds()