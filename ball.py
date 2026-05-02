#Importera moduler
import pygame
from const import *
from bat import *
from block import *


#Skapa klass för boll
class ball:
    def __init__ (self, speed_x, speed_y, size, position_x, position_y):
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.size = size
        self.position_x = position_x
        self.position_y = position_y

    #Skapa funktion för kollision med fönstret
    def ballColission(self):
        if self.position_x > screenWidth:
            self.speed_x *= -1
        elif self.position_x <= 0:
            self.speed_x *= -1
        if self.position_y <= 0:
            self.speed_y *= -1
        elif self.position_y > screenHeight:
            exit()

    #Skapa funktion för kollision med paddel, skapad med hjälp av Claude-Sonnet
    def batColission(self, bat):
        if self.position_x + self.size >= bat.position_x and self.position_x - self.size <= bat.position_x + bat.size_x:
            if self.position_y + self.size >= bat.position_y and self.speed_y > 0:
                self.speed_y *= -1

    #Skapa funktion för att rita upp bollen
    def drawBall(self, surface):
        pygame.draw.circle(surface, "white", (self.position_x, self.position_y), self.size)

    #Skapa funktion för att kolla om bollen kolliderar med blocken, skapad med hjälp av Claude-Sonnet
    def blockColission(self, blocks):
        for block in blocks:
            if self.position_x + self.size >= block.position_x and self.position_x - self.size <= block.position_x + block.size_x:
                if self.position_y - self.size <= block.position_y + block.size_y and self.position_y + self.size >= block.position_y:
                    self.speed_y *= -1
                    blocks.remove(block)
                    break