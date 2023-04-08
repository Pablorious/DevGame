import sys
import pygame
import vec2d
from pygame import *
from player import Player
from vec2d import *

class Game:
    def __init__(self):
        self.running = True
        self.fps = 30
        self.displaysurf = pygame.display.set_mode((800,600),0,32)
        self.p = Player(vec2d(5,5)) 
        self.fpsclock = pygame.time.Clock()
        self.tile = pygame.image.load('stonetile-64x32.png')

    def onEvent(self,event):
        if event.type == pygame.QUIT:
            self.running = False
        self.p.onEvent(event) 
    
    def onLoop(self):
        self.p.act()
    
    def onRender(self):
        self.displaysurf.fill((200,200,200))
        for i in range(30):
            for j in range(25):
                self.displaysurf.blit(self.tile,(i*32-32,j*32+16*(i%2)-32))
        
        pos = self.p.pos 
        self.displaysurf.blit(self.p.getImage(),pos
        
        pygame.display.update()
        self.fpsclock.tick(self.fps)
    
    def onCleanup(self):
        print("Goodbye!")
    
    def onExecute(self):
        while(self.running):
            for event in pygame.event.get():
                self.onEvent(event) 
            self.onLoop()
            self.onRender()
        self.onCleanup()

g = Game()
g.onExecute()
