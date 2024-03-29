import pygame
import constants as c
from star import Star
import random

class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        self.image = pygame.Surface(c.screen_size)
        self.color = (10, 0, 15)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.timer = random.randrange(3, 10)



    def update(self):
        self.stars.update()
        if self.timer == 0:
            new_star = Star()
            self.stars.add(new_star)
            self.timer = random.randrange(3, 10)
        self.image.fill(self.color)
        self.stars.draw(self.image)
        self.timer -= 1

        

