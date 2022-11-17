import pygame
import constants as c



class TextBox(pygame.sprite.Sprite):
    def __init__ (self, message):
        super(TextBox, self).__init__()
        self.font = pygame.font.Font('font/Pixeltype.ttf', 50)
        self.color = (75, 255, 75)
        self.message = message
        self.image = self.font.render(self.message, 0, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = c.screen_width //2 - self.rect.width //2
        self.rect.y = c.screen_height //2 - self.rect.height //2
        self.velx = 0
        self.vely = 0


    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely