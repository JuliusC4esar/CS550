
# Kai Joseph and Ethan Chapman

# November 12, 2018

# Description: Avoid the red enemies! More and more of them keep coming in varying size and speed. Use the left and right arrow keys to move and the spacebar to jump. You can jump through the white platforms but not the blue one! Press the down arrow key to fall through a white platform. Like jumping, you cannot fall through the blue platform, only the white ones by pressing the Down arrow key. Survive for as long as you can!


# Citations: https://www.pygame.org/docs/

import pygame
from pygame.locals import *
import random
from player import Player
from enemy import Enemy
from wall import Wall

screen_size = 400, 400
fps = 60

pygame.init() # Start the pygame window

window = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

player = Player(100, screen_size[1] - 20, 20, 20) # create new player
enemies = [] #instantiate enemies array

walls = [] #Create platforms
walls += [Wall(screen_size[0] * 0.333, screen_size[1] - 150, screen_size[0] * 0.333, 7, True)]
walls += [Wall(50, 300, 300, 7, False)]
walls += [Wall(50, 150, 300, 7, True)]
walls += [Wall(50, 150, 130, 7, True)]
walls += [Wall(50, 50, 130, 7, True)]
walls += [Wall(250, 50, 130, 7, True)]

running = True  # Game Running loop
game_over = False  # Game over caller

high_score = 0
new_high = False

frames = 0
frameCount = 0

while running:

    for event in pygame.event.get():  # Loop get the pyGame events
            if event.type == QUIT:
                running = False  # Quit if the window is closed

    if game_over == False:
        font = pygame.font.SysFont(None,25)

        window.fill(pygame.color.Color("BLACK"))  # Clear the window

        t = round(frameCount / fps)  # Time Count

        if t > high_score:
            new_high = True  # Set High score
            high_score = t

        text = font.render("Time Survived: "+str(t)+" seconds",True,(255,255,255))  # High score text

        window.blit(text,(10,10))  #Display high score text

        dt = fps * (clock.tick(fps) / 1000)  # Calculate dt

        frames += 1  # Increase frame count.
        frameCount += 1

        if frames >= (60 / dt) * 4:   #Create new enemy every four seconds
            frames = 0

            size = random.randint(5, 15)  # Random size

            x = random.sample([-size, screen_size[0] + size], 1)[0]  # Random enemy position
            y = random.randint(-size, screen_size[1] + size)

            enemies.append(Enemy(x, y, (1/size)*8, size))   # Create new enemy

        screen_size = pygame.display.get_surface().get_size()  # Get the screen size (in case of resize)

        # Calculate player movement and draw player
        player.movement(screen_size, dt, walls)   # Player class functions
        player.graphics(screen_size, window)

        for x in range(len(enemies)):   # Run class functions for all enemies in enemies array
            enemies[x].movement(screen_size, dt, player)
            enemies[x].graphics(screen_size, window)
            if enemies[x].run == False:

                game_over = True   # Set gameover to true if collided

                break

        [i.graphics(screen_size, window) for i in walls]

        # Display window and change title
        pygame.display.flip()
        pygame.display.set_caption(f"T: {round(frameCount / fps)}")


    else:
        #window.fill(pygame.color.Color("BLACK"))  # Clear the window

        screen_size = pygame.display.get_surface().get_size()  # Get the screen size (in case of resize)

        # Display window and change title
        pygame.display.flip()
        pygame.display.set_caption(f"T: {round(frameCount / fps)}")

        font = pygame.font.SysFont(None,40)  # Change font size

        text = font.render("Time Survived: "+str(t)+" seconds",True,(255,255,255))   # Game over text
        text2 = font.render("Press the SPACEBAR",True,(255,255,255))
        text3 = font.render("High Score:" + str(high_score), True, (255, 255, 255))
        text4 = font.render("New High Score!",True,(255,255,255))
        text5 = font.render("No new high score...",True,(255,255,255))

        window.blit(text,(10,200))
        window.blit(text2,(10,300))
        window.blit(text3,(10,100))

        if new_high:
            window.blit(text4,(10,70))

        else:
            window.blit(text5,(10,70))

        key = pygame.key.get_pressed()  # Get the keys pressed

        if key[K_SPACE]:   # If space key is pressed
            player = Player(100, screen_size[1] - 20, 20, 20)  # Make new player
            enemies = []  # Clear enemies
            frameCount = 0
            new_high = False
            game_over = False