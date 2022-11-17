import pygame
import constants as c
import random


class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.width = random.randrange(1, 4)
        self.height = self.width
        self.size = (self.width, self.height)
        self.color = (255, 255, 230)
        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.screen_width)
        self.velx = 0
        self.vely = random.randrange(5, 15)

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely