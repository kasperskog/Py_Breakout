#Importera moduler
import pygame
import random

#Skapa klass för block
class block:
    def __init__ (self, size_x, size_y, color, position_x, position_y):
        self.size_x = size_x
        self.size_y = size_y
        colors = ["red", "blue", "green", "purple"]
        self.color = random.choice(colors)
        self.position_x = position_x
        self.position_y = position_y
    
    #Skapa funktion för att rita upp blocken
    def drawBlock(self, surface):
        pygame.draw.rect(surface, self.color, (self.position_x, self.position_y, self.size_x, self.size_y))