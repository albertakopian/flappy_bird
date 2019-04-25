from Tools import *


class Background:
    def __init__(self):
        self.background_night_image = pygame.image.load('images/background-night.png')
        self.base_image = pygame.image.load('images/base.png')
        self.game_over_image = pygame.transform.scale(pygame.image.load('images/gameover.png'), (288, 63))
        self.field_for_score = pygame.font.SysFont(None, 42)

    def draw_back(self):
        screen.blit(self.background_night_image, (0, 0))
        screen.blit(self.background_night_image, (288, 0))
        screen.blit(self.background_night_image, (576, 0))

    def draw_base(self):
        screen.blit(self.base_image, (0, 400))
        screen.blit(self.base_image, (336, 400))
        screen.blit(self.base_image, (672, 400))

    def draw_score(self, current_score):
        text = self.field_for_score.render('Score:' + str(current_score // 2), True, (180, 180, 180))
        screen.blit(text, (0, 0))

    def draw_game_over_menu(self, current_score):
        self.draw_back()
        self.draw_base()
        screen.blit(self.game_over_image, (270, 60))
        f = pygame.font.SysFont(None, 40)
        score = f.render('Your score is: ' + str(current_score // 2), True, (180, 180, 180))
        text = f.render('Press enter to restart or escape to quit', True, (180, 180, 180))
        screen.blit(score, (310, 215))
        screen.blit(text, (150, 255))