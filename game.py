#Importera moduler
import pygame
import ball
import bat
import block
import os
from const import *

#Initiera pygame
pygame.init()
gameBoard = pygame.display.set_mode((screenWidth, screenHeight))
gameClock = pygame.time.Clock()
gameRunning = True

#Rensa terminalen och ge status
os.system('cls')
print("GAME STARTED")

#Skapa objekt
ballCenterHeight = ((screenHeight / 2) + (ballSize / 2))
ballCenterWidth = ((screenWidth / 2) + (ballSize / 2))
boll = ball.ball(ballSpeedX, ballSpeedY, ballSize, ballCenterWidth, ballCenterHeight)
batCenterWidth = ((screenWidth / 2) - (batWidth / 2))
bat1 = bat.bat(batSpeed, batWidth, batHeight, batCenterWidth, (600 - batHeight))

#Rita upp och skapa block, skapad med hjälp av Claude-Sonnet
blocks = []
for row in range(blockRows):
    for col in range(blockColumns):
        pos_x = col * (blockWidth + blockPadding) + blockPadding
        pos_y = row * (blockHeight + blockPadding) + blockPadding + 50  # +50 to add some top margin
        newBlock = block.block(blockWidth, blockHeight, "white", pos_x, pos_y)
        blocks.append(newBlock)


#Spelets loop
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    #Anropa funktioner för spelets komponenter
    boll.position_x += boll.speed_x
    boll.position_y += boll.speed_y
    boll.ballColission()
    boll.batColission(bat1)
    boll.blockColission(blocks)
    bat1.moveBat()

    #Rita upp allt i fönstret
    gameBoard.fill("black")
    boll.drawBall(gameBoard)
    bat1.drawBat(gameBoard)
    
    for b in  blocks:
        b.drawBlock(gameBoard)

    pygame.display.flip()
    gameClock.tick(60)

    #Kontroller om spelaren har vunnit
    if len(blocks) == 0:
        gameRunning = False
        print("YOU WIN!")

pygame.quit()
