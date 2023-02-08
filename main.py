# import pygame

import pygame



# defined the RGB color code for the background

background_colour = (139,0,0)



# defined the size of the screen (width, height)

screen = pygame.display.set_mode((600, 300))

import pygame

# Initialize the pygame
pygame.init()

# create  the screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImage = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImage,(x,y))
# Game Loop
running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check wheter its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change     
    player(playerX,playerY)
    pygame.display.update()