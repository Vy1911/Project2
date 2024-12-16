import pygame
import random
from utils import screen, RED



class Button:
    def __init__(self, x, y, image):
        self.rect = image.get_rect(topleft=(x, y))
        self.image = image

    def draw(self):
        screen.blit(self.image, self.rect)

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def is_clicked(self):
        return self.is_hovered() and pygame.mouse.get_pressed()[0]


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("rocket.png").convert_alpha()


        self.image = pygame.transform.scale(self.image, (80, 80))


        self.rect = self.image.get_rect()


        self.rect.center = (390 // 2, 550)


        self.speed = 5

    def update(self):

        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed


        if keys[pygame.K_RIGHT] and self.rect.right < 390:
            self.rect.x += self.speed


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 7

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

#Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()

        self.image = pygame.image.load("enemy.png").convert_alpha()


        self.image = pygame.transform.scale(self.image, (60, 60))


        self.rect = self.image.get_rect()


        self.rect.x = random.randint(0, 330)
        self.rect.y = random.randint(-50, -10)

        self.speed = speed

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > 620:
            self.kill()