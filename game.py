import random
import time
import pygame
import sys
import os

from pygame import draw

pygame.init()


#
# DEFINITIONS 
#
pos = None

#COLORS :)
BLUE = [0,0,255]
BLACK = [0,0,0]
WHITE = [255,255,255]
RED = [255, 0, 0]

#FRAMERATE AND WHAT NOT
fps = 30
animationCycle = 4 #Idk what this is for, i'll get to it later :)
clock = pygame.time.Clock()


# WINDOW DEFS: MOVE TO NEW FILE LATER, FIGURE OUT IMPORTING FROM SEPERATE FILE AGAIN
windowy = 500
windowx = 500
gameFont= pygame.font.SysFont("Arial", 20)
win = pygame.display.set_mode((windowx, windowy),0, 32)

background = pygame.Surface((windowx,windowy))



class Button:
    def __init__(self, color, width, height, x, y, text = ''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, surface):

        drawButton = pygame.Rect(self.x, self.y, self.width, self.height) #Rectangle to act as button, just takes dimensions and location. 

        #Takes parameters: Surface(Whatever surface you end up using), color, and the rectangle, created above. 
        pygame.draw.rect(surface, self.color, drawButton)# Drawing the button :)
        
        #Create text offset in relation to the button rectangle?? maybe something to do later. 
        if self.text != '':
            #Renders the text. 
            text = gameFont.render(self.text, 1, BLACK)
            surface.blit(text, (self.x + (self.width / 2) , self.y + (self.height / 2) ) )#Places text in the middle of the button. 

        

    def isOver(self, pos):
        pos = pygame.mouse.get_pos()
        #checking for whetehr you're over the button
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
        #how to make it so that it does something
                return True
        return False

main = True
intro = True
game = False


#Button(Color, WIDTH, HEIGHT, POSITION, TEXT)



quitButton = Button([100,255,0],300, 100, 100, 350, 'QUIT')

startButton = Button(RED, 300, 100, 100, 100, 'START')


#
# MAIN GAME LOOP
#
win.fill(BLUE)


quitButton.draw(background)

startButton.draw(background)

pygame.display.flip()


while main:
    while quitButton.isOver(pos):
        quitButton.color = RED

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
        elif event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if quitButton.isOver(pos):
                quitButton.color = RED
                main = False
            else:
                quitButton.color = WHITE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if startButton.isOver(pos):
                intro = True
    while intro:
        print("introduction works")
        intro = False