import pygame
import constants as c



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.width = 20
        self.height = 20
        self.size = (self.width, self.height)
        self.color = (155, 155, 255)
        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (c.screen_width/2, c.screen_height/2)
        self.velx = 0
        self.vely = 0
        self.speed = 5

    def update(self):
        self.rect.x += self.velx
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= c.screen_width - self.rect.width:
            self.rect.x = c.screen_width - self.rect.width
        self.rect.y += self.vely
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= c.screen_height - self.rect.height:
            self.rect.y = c.screen_height - self.rect.height
