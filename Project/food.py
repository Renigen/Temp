import pygame
import constants as c
import random


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super(Food, self).__init__()
        self.width = 15
        self.height = 15
        self.size = (self.width, self.height)
        self.color = (255, 155, 75)
        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randrange(0, c.screen_width - self.rect.width)
        self.rect.y = random.randrange(0, c.screen_height -self.rect.height)
        self.velx = random.randrange(-3, 3)
        self.vely = random.randrange(-3, 3)


    def update(self):
        self.rect.x += self.velx
        if self.rect.x <= 0 or self.rect.x >= c.screen_width - self.rect.width:
            self.velx *= -1    
        self.rect.y += self.vely
        if self.rect.y <= 0 or self.rect.y >= c.screen_height - self.rect.height:
            self.vely *= -1
