from Tools import *


class FlappyBird:
    def __init__(self):
        self.x_size = 25
        self.y_size = 25
        self.bird = pygame.transform.scale(bird_image, (self.x_size, self.y_size))
        self.x_coord = 432
        self.y_coord = 200
        self.y_speed = 0
        self.acceleration = 0.15

    def show_bird(self):
        screen.blit(self.bird, (self.x_coord, self.y_coord))

    def moving(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sounds_effects['wing'].play()
                    self.y_speed = -self.acceleration * 40

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.y_speed = 1.25
        if self.acceleration != 0:
            if self.y_speed != 0:
                self.y_speed += self.acceleration
            self.y_coord += self.y_speed
