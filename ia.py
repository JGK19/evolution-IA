import pygame
import random
import classes
import math

import functions

pygame.init()

ALTURA, LARGURA = 800, 600
WIN = pygame.display.set_mode((ALTURA, LARGURA))
pygame.display.set_caption('teste')

GREEN = (0, 255, 100)

FONT0 = pygame.font.SysFont("comicsans", 16, bold=True, italic=True)


def main():

    x = 0

    run = True

    end = False

    clock = pygame.time.Clock()

    creatures = []
    foods = []

    restart = classes.Restart()


    a = 100
    for i in range(a):
        creatures.append(classes.Creature())

    creatures2 = creatures[:]

    y = 20
    for i in range(y):
        foods.append(classes.Food())

    while run:
        clock.tick(244)
        WIN.fill(GREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                end = True
            else:
                end = False

        for food in foods:
            food.draw(WIN)
        for creature in creatures:
            creature.do_all(WIN, foods, creatures, creatures2)

        x += 1
        print(len(creatures), len(creatures2), x)
        if len(foods) == 0 or len(creatures2) == len(creatures) or x > 2000:
            x = 0
            restart.restarting(creatures, foods, creatures2)

        chesh = FONT0.render(f"generation: {restart.generation}", True, (0, 0, 0))
        WIN.blit(chesh, (100, 10))

        pygame.display.flip()


main()
