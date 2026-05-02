#Importera moduler
import pygame
from const import *

#Skapa klass för paddel
class bat:
    def __init__ (self, speed, size_x, size_y, position_x, position_y):
        self.speed = speed
        self.size_x = size_x
        self.size_y = size_y
        self.position_x = position_x
        self.position_y = position_y
    
    #Skapa funktion för att rita upp paddeln
    def drawBat(self, surface):
        pygame.draw.rect(surface, "white", (self.position_x, self.position_y, self.size_x, self.size_y))

    #Skapa funktion för att röra paddeln, skapad med hjälp av Claude-Sonnet
    def moveBat(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.position_x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.position_x += self.speed
        
        if self.position_x < 0:
            self.position_x = 0
        if self.position_x + self.size_x > screenWidth:
            self.position_x = screenWidth - self.size_x