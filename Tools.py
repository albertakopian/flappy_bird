import pygame

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
l_c = 4
b_c = 8
screen__width = 512
screen__length = 864
screen = pygame.display.set_mode((864, 512))

sounds_effects = {'wing': pygame.mixer.Sound('sound/wing.ogg'),
                  'point': pygame.mixer.Sound('sound/point.ogg'),
                  'hit': pygame.mixer.Sound('sound/hit.ogg')}

background_image = pygame.image.load('images/background-night.png')
base_image = pygame.image.load('images/base.png')

bird_image = pygame.image.load('images/redbird.png')

pipe_down = pygame.image.load('images/pipe.png').convert_alpha()
pipe_up = pygame.transform.flip(pygame.image.load('images/pipe.png'), False, True)
