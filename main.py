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

def player():
    screen.blit(playerImage,(playerX,playerY))
# Game Loop
running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player()
    pygame.display.update()