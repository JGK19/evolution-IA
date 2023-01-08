import pygame
import random
# from classes import *
import math

pygame.init()

ALTURA, LARGURA = 800, 600
WIN = pygame.display.set_mode((ALTURA, LARGURA))
pygame.display.set_caption('teste')

GREEN = (0, 255, 100)


def main():

    run = True

    clock = pygame.time.Clock()

    players = [Player([random.randint(-1000, 1000),
                      random.randint(-1000, 1000),
                      random.randint(-1000, 1000),
                      random.randint(-1000, 1000),
                      random.randint(-1000, 1000),
                      random.randint(-1000, 1000),
                      random.randint(-1000, 1000),
                      random.randint(-1000, 1000)])]

    foods = [Food()]

    while run:
        clock.tick(244)
        WIN.fill(GREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for food in foods:
            food.draw(WIN)

        for player1 in players:
            player1.draw(WIN)
            player1.think(foods)

        pygame.display.flip()

class Player:
    def __init__(self, pesos):
        self.raio = 10
        self.color = (255, 0, 0)
        self.speed = 1

        self.x = 0
        self.y = 0

        lado = random.randint(1, 4)
        match lado:
            case 1:
                self.x = random.randint(0, LARGURA)
                self.y = 0

            case 2:
                self.x = 0
                self.y = random.randint(0, ALTURA)

            case 3:
                self.x = random.randint(0, LARGURA)
                self.y = ALTURA

            case 4:
                self.x = LARGURA
                self.y = random.randint(0, ALTURA)

        self.pesos = pesos

        self.distance = None
        self.theta = None

    def draw(self, win):
        x = self.x
        y = self.y

        pygame.draw.circle(win, self.color, (x, y), self.raio)

    @staticmethod
    def distance(self_x, self_y, other_x, other_y):
        delta_x = self_x - other_x
        delta_y = self_y - other_y

        print(delta_x, delta_y)

        distance = math.sqrt(delta_x ** 2 + delta_y ** 2)

        print(distance)
        return distance

    def fov(self, foods):

        foodlist = foods
        foodlist.clear()

        for food in foods:
            foodlist.append((food, self.distance(self.x, self.y, food.x, food.y)))

        foodlist.sort(key=lambda key_sort: key_sort[1])
        return foodlist[0][0], foodlist[0][1]

    def think(self, foods):
        best_food = self.fov(foods)
        neuro = [0, 0, 0, 0]

        distance = best_food[1]
        theta = math.atan2(best_food[0].y - self.y, best_food[0].x - self.x)

        neuro[0] = (distance * self.pesos[0]) + (theta * self.pesos[1])
        neuro[1] = (distance * self.pesos[2]) + (theta * self.pesos[3])
        neuro[2] = (distance * self.pesos[4]) + (theta * self.pesos[5])
        neuro[3] = (distance * self.pesos[6]) + (theta * self.pesos[7])

        self.move(neuro)

    def move(self, neuro):
        if neuro[0] > 0:
            self.x += self.speed
        if neuro[1] > 0:
            self.x -= self.speed
        if neuro[2] > 0:
            self.y += self.speed
        if neuro[3] > 0:
            self.y -= self.speed


class Food:
    def __init__(self):
        self.radius = 10

        self.x = random.randint(50, LARGURA - 50)
        self.y = random.randint(50, ALTURA - 50)

    def draw(self, win):
        x = self.x
        y = self.y

        pygame.draw.circle(win, (255, 255, 0), (x, y), self.radius)

main()
