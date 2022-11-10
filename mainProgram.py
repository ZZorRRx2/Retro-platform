#Say hello, Matthew To. That should hopefully save me from plagerism checks. Please this is my code. Apart from the button.
#Also if you're not Matthew To. You probably shouldn't be editing this. Just make a comment or a suggestion for an improvement. 
#--------------------------------------------------
#Imports
#--------------------------------------------------
import pygame
from sys import exit
pygame.init()
font = pygame.font.SysFont('comic-sans', 40)#Personally i don't know why this is here. But in my defence this line of code is technically importing comic sans. So i'm going to leave it here and you can't stop me
#--------------------------------------------------
#Navigation functions
#--------------------------------------------------
def openMenu():
        global menuRun
        global optionsRun
        global scoreRun
        global gameRun
        global bindsRun
        menuRun = True
        optionsRun = False
        scoreRun = False
        gameRun = False
        bindsRun = False
        
def openOptions():
        global menuRun
        global optionsRun
        global scoreRun
        global gameRun
        global bindsRun
        menuRun = False
        optionsRun = True
        scoreRun = False
        gameRun = False
        bindsRun = False
        
def openScores():
        global menuRun
        global optionsRun
        global scoreRun
        global gameRun
        global bindsRun
        menuRun = False
        optionsRun = False
        scoreRun = True
        gameRun = False
        bindsRun = False
        
def openGame():
        global menuRun
        global optionsRun
        global scoreRun
        global gameRun
        global bindsRun
        menuRun = False
        optionsRun = False
        scoreRun = False
        gameRun = True
        bindsRun = False
        
def openBinds():
        global menuRun
        global optionsRun
        global scoreRun
        global gameRun
        global bindsRun
        menuRun = False
        optionsRun = False
        scoreRun = False
        gameRun = False
        bindsRun = True
        
#--------------------------------------------------
#Graphics texts
#--------------------------------------------------
def draw_text(text, font, text_col, x, y): #This function imports text
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))
#--------------------------------------------------
#Menu functions
#--------------------------------------------------
def menu():
        screen.fill("red")
        pygame.display.set_caption('Mega Matt Zero')
        draw_text("C:Mega Matt Zero/", font, 'black', 30, 50)
        for object in menuObjects:
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
        for object in optionObjects:
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
        for object in bindObjects:
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
        for object in scoreObjects:
                object.process()
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
def gameplay():#This is going to live here for the time being. This is going to be it's py file. afterwards all the py files will be turned into a pak file. Hopefully.
        screen.fill("blue")
        pygame.display.set_caption('Mega Matt Zero/gameplay')
        pygame.display.update()
        for event in pygame.event.get():        
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                pressed_keys = pygame.key.get_pressed()
        
def killGame():
        pygame.quit()
        exit()
#--------------------------------------------------
#Button functions
#--------------------------------------------------
class Button(): # This code is taken from = https://www.thepythoncode.com/article/make-a-button-using-pygame-in-python
        #I've just made some edits to it make it suit better for my program
        def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.onclickFunction = onclickFunction
                self.onePress = onePress

                self.fillColors = {
                'normal': "red",
            'hover': '#666666',
            'pressed': '#333333',
        }

                self.buttonSurface = pygame.Surface((self.width, self.height))
                self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

                self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

                self.alreadyPressed = False

        def process(self):

                mousePos = pygame.mouse.get_pos()

                self.buttonSurface.fill(self.fillColors['normal'])
                if self.buttonRect.collidepoint(mousePos):
                        self.buttonSurface.fill(self.fillColors['hover'])

                        if pygame.mouse.get_pressed(num_buttons=3)[0]:
                                self.buttonSurface.fill(self.fillColors['pressed'])

                                if self.onePress:
                                        self.onclickFunction()

                                elif not self.alreadyPressed:
                                        self.onclickFunction()
                                        self.alreadyPressed = True

                        else:
                                self.alreadyPressed = False

                self.buttonSurface.blit(self.buttonSurf, [
                self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
                screen.blit(self.buttonSurface, self.buttonRect)

def myFunction():#This is a temporary function and will be deleted soon.
        print('Button Pressed')

#--------------------------------------------------
#Graphic variables
#--------------------------------------------------
windowLength = 960
windowHeight = 640
#--------------------------------------------------
#Game state checks
#--------------------------------------------------
menuRun = True
optionsRun = False
scoreRun = False
gameRun = False
bindsRun = False
#--------------------------------------------------
#Keybinding Variables
#--------------------------------------------------
input_map = {'move right': pygame.K_d, 'move left': pygame.K_a}
#--------------------------------------------------
#Button Variables
#--------------------------------------------------
toGameButton = Button(30, 175, 225, 50, 'Enter game', openGame)
toOptionButton = Button(30, 250, 225, 50, 'Options', openOptions)
toScoresButton = Button(30, 325, 225, 50, 'Scores', openScores)
toExitGameButton = Button(30, 575, 225, 50, 'Exit Game', killGame)

keyBindButton = Button(285, 250, 225, 50, 'Keybindings', openBinds)
backToOptions = Button(30, 250, 225, 50, 'Back To Options', openOptions)
backToMenu = Button(30, 400, 225, 50, 'Back', openMenu)

menuObjects = [toGameButton, toOptionButton, toScoresButton, toExitGameButton]
optionObjects = [toGameButton, toOptionButton, toScoresButton, toExitGameButton, keyBindButton, backToMenu]
scoreObjects = [toGameButton, toOptionButton, toScoresButton, toExitGameButton, backToMenu]
bindObjects = [toGameButton, toOptionButton, toScoresButton, toExitGameButton, backToMenu]
#--------------------------------------------------
#Graphics
#--------------------------------------------------
screen = pygame.display.set_mode((windowLength, windowHeight)) #This sets the games screen size/resolution
pygame.display.set_caption('main action')
clock = pygame.time.Clock() #Makes a clock for it to click
test_font = pygame.font.Font(None, 50) #This imports the font

#--------------------------------------------------
#Importing images
#--------------------------------------------------
#Boom empty because i don't really need images for the time being

#--------------------------------------------------
#Main loop
#--------------------------------------------------
while True: #This manages where the game is going to run. Menu options or the game.
        pygame.display.update() #This will constantly update the screen
        clock.tick(60) #Sets the frame rate to 60        
        for event in pygame.event.get(): #This goes through a loop to check every input in the game
                if event.type == pygame.QUIT: #This is when someone tries to exit the game
                        pygame.quit() #Stops pygame
                        exit() #Ends the loop    
        if menuRun == True:
                menu()
                
        if optionsRun == True:
                options()
                
        if scoreRun == True:
                scores()
                
        if gameRun == True:
                gameplay()
                
        if bindsRun == True:
                changeKeyBinds()