import pygame
from food import Food
import random

class FoodSpawner:
    def __init__(self):
        self.food_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 120)

    def update(self):
        self.food_group.update()
        if self.spawn_timer == 0:
            self.spawn_food()
            self.spawn_timer = random.randrange(30, 120)
        else:
            self.spawn_timer -= 1



    def spawn_food(self):
        new_food = Food()
        self.food_group.add(new_food)

