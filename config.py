import pygame
from PIL import Image
pygame.init()


background_image = Image.open('background.jpg')

background_image = background_image.resize((390, 620))
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (390, 620))


home_icon = pygame.image.load('image.png')

volume_on_icon = pygame.image.load('volume.jpg')
volume_on_icon = pygame.transform.scale(volume_on_icon, (50, 50))

volume_off_icon = pygame.image.load('volume off.png')
volume_off_icon = pygame.transform.scale(volume_off_icon, (50, 50))


screen = pygame.display.set_mode((390, 620))
pygame.display.set_caption("Space Shooter")


pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1, 0.0)


game_over_music = "gameover_music.mp3"

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


clock = pygame.time.Clock()
