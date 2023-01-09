import pygame
import random
import functions

ALTURA, LARGURA = 800, 600


class Food:
    def __init__(self, color=(255, 255, 0), radius=5):

        self.x = random.randint(50, LARGURA - 50)
        self.y = random.randint(50, ALTURA - 50)

        self.color = color

        self.radius = radius

    def draw(self, win):
        x = self.x
        y = self.y

        pygame.draw.circle(win, self.color, (x, y), self.radius)


class Creature:
    def __init__(self, x=100, y=100, color=(255, 0, 0), radius=10, neuros=None):
        if neuros is None:
            self.neuros = [random.randint(-1000, 1000),
                           random.randint(-1000, 1000),
                           random.randint(-1000, 1000),
                           random.randint(-1000, 1000),
                           random.randint(-1000, 1000),
                           random.randint(-1000, 1000),
                           random.randint(-1000, 1000),
                           random.randint(-1000, 1000)]
        else:
            self.neuros = neuros

        self.alive = True

        self.x = x
        self.y = y

        self.color = color
        self.radius = radius
        self.speed = 2

        self.food_eat = 0

        self.steps = 0
        self.max_steps = 1000

    def do_all(self, win, foods, creatures, creatures2):
        self.draw_agent(win)
        self.eat(foods)
        self.brain(foods)
        self.dead(creatures2)

    def draw_agent(self, win):
        x = self.x
        y = self.y

        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def fov(self, foods):
        field_of_view = []

        for food in foods:
            distance_for_food = functions.distance(self.x, self.y, food.x, food.y)
            field_of_view.append((food.x, food.y, distance_for_food))

        field_of_view.sort(key=lambda key_sort: key_sort[1])

        return str(field_of_view[0][0]), str(field_of_view[0][1]), str(field_of_view[0][2])

    def eyes(self, foods):
        var = self.fov(foods)

        best_distance = float(var[2])

        angle = functions.get_angle(float(var[0]), float(var[1]), self.x, self.y)

        return best_distance, angle

    def move(self, up, right, left, down):
        if up > 0:
            self.y -= self.speed
            self.steps += 1
        if down > 0:
            self.y += self.speed
            self.steps += 1
        if right > 0:
            self.x += self.speed
            self.steps += 1
        if left > 0:
            self.x -= self.speed
            self.steps += 1

    def brain(self, foods):
        receptors = self.eyes(foods)

        times = self.neuros

        neurons = [0, 0, 0, 0]

        neurons[0] = (receptors[0] * times[0]) + (receptors[1] * times[1])
        neurons[1] = (receptors[0] * times[2]) + (receptors[1] * times[3])
        neurons[2] = (receptors[0] * times[4]) + (receptors[1] * times[5])
        neurons[3] = (receptors[0] * times[6]) + (receptors[1] * times[7])

        self.move(neurons[0], neurons[1], neurons[2], neurons[3],)

    def eat(self, foods):
        for food in foods:
            distance = functions.distance(self.x, self.y, food.x, food.y)
            if self.radius + food.radius >= distance:
                foods.remove(food)
                self.food_eat += 1

    def dead(self, creatures2):
        if self.steps >= self.max_steps:
            if self.alive:
                self.alive = False
                creatures2.append(self)
                self.speed = 0
            else:
                pass


class Restart:
    def __init__(self, generation=0):
        self.generation = generation

    def restarting(self, creatures, foods, creatures2):
        self.generation += 1
        best = self.take_the_best(creatures)
        creatures.clear()
        foods.clear()

        self.respawn_food(10, foods)

        x = 100
        for i in range(x):
            valor = functions.mutation(best.neuros)
            creatures.append(Creature())

        creatures2.clear()

    @staticmethod
    def take_the_best(creatures):
        best = creatures[0]
        bigger = 0
        for creature in creatures:
            if creature.food_eat > bigger:
                bigger = creature.food_eat
                best = creature

        return best

    @staticmethod
    def respawn_food(how_much, foods):

        for i in range(how_much):
            foods.append(Food())
