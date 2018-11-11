import pygame
from pygame.locals import *
import random
from player import Player
from enemy import Enemy
from wall import Wall

screen_size = 400, 400
fps = 60

pygame.init()

window = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

player = Player(100, screen_size[1] - 20, 20, 20, 8)
enemies = []

walls = []
walls += [Wall(screen_size[0] * 0.333, screen_size[1] - 150, screen_size[0] * 0.333, 7, True)]
walls += [Wall(50, 300, 300, 7, False)]
walls += [Wall(50, 150, 300, 7, True)]
walls += [Wall(50, 150, 130, 7, True)]
walls += [Wall(50, 50, 130, 7, True)]
walls += [Wall(250, 50, 130, 7, True)]

running = True
gameover = False

frames = 0
frameCount = 0


while running:

    for event in pygame.event.get():  # Loop get the pyGame events
            if event.type == QUIT:
                running = False  # Quit if the window is closed

    if gameover == False:

        font = pygame.font.SysFont(None,25)

        window.fill(pygame.color.Color("BLACK"))  # Clear the window

        t = round(frameCount / fps)

        text = font.render("Time Survived: "+str(t)+" seconds",True,(255,255,255))

        window.blit(text,(10,10))

        dt = fps * (clock.tick(fps) / 1000)  # Calculate dt

        frames += 1
        frameCount += 1

        if frames >= (60 / dt) * 4:
            frames = 0

            size = random.randint(5, 15)

            x = random.sample([-size, screen_size[0] + size], 1)[0]
            y = random.randint(-size, screen_size[1] + size)

            enemies.append(Enemy(x, y, (1/size)*8, size))

        screen_size = pygame.display.get_surface().get_size()  # Get the screen size (in case of resize)

        # Calculate player movement and draw player
        player.movement(screen_size, dt, walls)
        player.graphics(screen_size, window)

        for x in range(len(enemies)):
            enemies[x].movement(screen_size, dt, player)
            enemies[x].graphics(screen_size, window)
            if enemies[x].run == False:

                gameover = True

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

        font = pygame.font.SysFont(None,40)

        text = font.render("Time Survived: "+str(t)+" seconds",True,(255,255,255))

        text2 = font.render("Press the SPACEBAR",True,(255,255,255))

        window.blit(text,(10,200))

        window.blit(text2,(10,300))

        key = pygame.key.get_pressed()  # Get the keys pressed

        if key[K_SPACE]:

        	player = Player(100, screen_size[1] - 20, 20, 20, 8)

        	enemies = []

        	frameCount = 0

        	gameover = False


















