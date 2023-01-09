import math
import random


def distance(self_x, self_y, other_x, other_y):
    delta_x = self_x - other_x
    delta_y = self_y - other_y

    distance_result = math.sqrt(delta_x ** 2 + delta_y ** 2)

    return distance_result


def get_angle(thing_x, thing_y, self_x, self_y):
    theta = math.atan2(thing_y - self_y, thing_x - self_x)

    return theta


def mutation(neuros_input):
    list_tax_mutation = range(0, 1000, 50)

    neuros = neuros_input

    for i in range(len(neuros)):
        tax = random.choice(list_tax_mutation)
        list_mutation = [neuros[i] + tax, neuros[i] - tax]
        neuros[i] = random.choice(list_mutation)

    return neuros

