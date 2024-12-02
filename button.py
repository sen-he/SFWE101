import pygame
import sys

class Button():
    def __init__(self, x, y, image,scale,ai_game):
        #resize image based on scale
        self.screen = ai_game.screen

        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        #positions the image
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
        #every button starts unclicked
        self.clicked = False
    
    def draw(self):
        action = False
        #get position of mouse
        pos = pygame.mouse.get_pos()

        #Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            # 0  is left click 1 is middle mouse button and 2 is right mouse button
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                #this variable allows it to only register one click at a time
                self.clicked = True
                action = True

        # If mouse isn't pressed it unclicks the mouse
        if pygame.mouse.get_pressed()[0] ==0:
            self.clicked = False

        #draw button on screen
        self.screen.blit(self.image,(self.rect.x,self.rect.y))

        return action

        
