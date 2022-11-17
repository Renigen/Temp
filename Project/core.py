import pygame
import csv
import random
import time




#imported objects
from player import Player
import constants as c
from background import BG
from foodSpawner import FoodSpawner
from gameOver import TextBox

scores = [23, 16, 32]
score_count = 0

pygame.init()

#display setup
screen = pygame.display.set_mode((c.screen_size))
pygame.display.set_caption('Annakis Rocket')
clock = pygame.time.Clock()
black = (0, 0, 0)
score = 0
time_left = 600


#object setup
player = Player()
bg = BG()

bg_group = pygame.sprite.Group()
bg_group.add(bg)

sprite_group = pygame.sprite.Group()
sprite_group.add(player)

food_spawner = FoodSpawner()
text_box_group = pygame.sprite.Group()


test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

def display_score():
    score_surf = test_font.render(f'{score}', True, 'Grey')
    score_rect = score_surf.get_rect(center = (960, 30))
    screen.blit(score_surf, score_rect)

def display_time():
    time_surf = test_font.render(f'{int(time_left/60)}', True, 'Grey')
    time_rect = time_surf.get_rect(center = (320, 30))
    screen.blit(time_surf, time_rect)



while True:

    if time_left <= 0:
        scores[score_count] = score
        with open('test.csv', 'w', newline='') as csvfile:

            fieldnames = ['number', 'score']

            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

            writer.writeheader()

            for score in scores:
                score_count += 1
                writer.writerow({'number': score_count, 'score':score})
            pygame.quit()
            quit()
        


    #event handling
    for event in pygame.event.get():

        #close if hitting close button
        if event.type == pygame.QUIT:
            scores[score_count] = score
            with open('test.csv', 'w', newline='') as csvfile:

                fieldnames = ['number', 'score']

                writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

                writer.writeheader()

            for score in scores:
                score_count += 1
                writer.writerow({'number': score_count, 'score':score})
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.vely = -player.speed
                if event.key == pygame.K_DOWN:
                    player.vely = player.speed
                if event.key == pygame.K_LEFT:
                    player.velx = -player.speed
                if event.key == pygame.K_RIGHT:
                    player.velx = player.speed

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.vely = 0
                if event.key == pygame.K_DOWN:
                    player.vely = 0
                if event.key == pygame.K_LEFT:
                    player.velx = 0
                if event.key == pygame.K_RIGHT:
                    player.velx = 0



    #update objects   

    sprite_group.update()
    bg_group.update()
    food_spawner.update()


    #collision check
    #def collide(player, food_spawner):
    collided = pygame.sprite.spritecollide(player, food_spawner.food_group, True)
    for food in collided:
        score += 1



    #render display

    screen.fill(black)
    bg_group.draw(screen)
    sprite_group.draw(screen)
    food_spawner.food_group.draw(screen)
    display_score()
    display_time()
    
    
    pygame.display.update()
    time_left -= 1



    #cap fps
    clock.tick(60)