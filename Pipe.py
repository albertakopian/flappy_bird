from Tools import *
from random import randint


class column:
    def __init__(self):
        self.x_coord = 864
        self.window_coord = randint(30, 270)

        self.width = 50
        self.height = 500
        self.x_coord_new = 864 + 864 // 2 + self.width // 2
        self.window_coord_new = randint(30, 270)
        self.space = 100
        self.pipe_speed = 3
        self.pipe_down = pygame.transform.scale(pipe_down, (self.width, self.height))
        self.pipe_up = pygame.transform.scale(pipe_up, (self.width, self.height))

    def draw_column(self):
        screen.blit(self.pipe_up, (self.x_coord, self.window_coord - self.height))
        screen.blit(self.pipe_down, (self.x_coord, self.window_coord + self.space))
        screen.blit(self.pipe_up, (self.x_coord_new, self.window_coord_new - self.height))
        screen.blit(self.pipe_down, (self.x_coord_new, self.window_coord_new + self.space))

    def moving(self):
        self.x_coord -= self.pipe_speed
        self.x_coord_new -= self.pipe_speed

    def update(self):
        if self.x_coord < -self.width:
            self.x_coord = 864
            self.window_coord = randint(30, 270)

        if self.x_coord_new < -self.width:
            self.x_coord_new = 864
            self.window_coord_new = randint(30, 270)