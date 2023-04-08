import vec2d
from vec2d import *
import pygame
from pygame.locals import *
class Player:
    def __init__(self,ipos):
        #todo, fix this damn mess.
        self.facing = 0
        self.upkeydown = False
        self.downkeydown = False
        self.rightkeydown = False
        self.leftkeydown = False
        self.spriteloop = 0
        self.speed = 10 
        self.pos = ipos 
        self.vel = vec2d(0,0)
        #update these textures 
        self.img = pygame.image.load('dev.png')

    def getImage(self):
        return self.img.subsurface(Rect(32*(self.spriteloop%4),64*self.facing,32,64))

    def act(self):
        if self.upkeydown:
            self.vel = self.vel + vec2d(0,-self.speed)
        if self.downkeydown:
            self.vel = self.vel + vec2d(0, self.speed)
        if self.leftkeydown:
            self.vel = self.vel + vec2d(-self.speed,0)
        if self.rightkeydown:
            self.vel = self.vel + vec2d( self.speed,0)
        
        self.vel = vec2d(self.vel.x * 0.70, self.vel.y * 0.70) 
        
        if self.vel.get_length() > 0.2:
            self.spriteloop += 1
        else:
            self.spriteloop = 0
        
        self.move()
    
    def move(self):
        self.pos = self.pos + self.vel
    
    def onEvent(self, event):
        if event.type == KEYDOWN:
            self.onKeyDown(event)
        elif event.type == KEYUP:
            self.onKeyUp(event)

    def onKeyDown(self,event):
        if event.key == K_w:
            self.facing = 0
            self.upkeydown = True 
        if event.key == K_a:
            self.facing = 1
            self.leftkeydown = True 
        if event.key == K_s:
            self.facing = 2
            self.downkeydown = True
        if event.key == K_d:
            self.facing = 3
            self.rightkeydown = True 
    
    def onKeyUp(self, event):
        if event.key == K_w:
            self.upkeydown = False 
        if event.key == K_a:
            self.leftkeydown = False 
        if event.key == K_s:
            self.downkeydown = False
        if event.key == K_d:
            self.rightkeydown = False 
    
