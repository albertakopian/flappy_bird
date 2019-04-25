from Background import *
from Pipe import *
from Bird import *


class Game:
    def __init__(self):
        self.stop_run = False
        self.is_game_over = False
        self.score = 0
        self.list_of_results = []
        self.pipe = column()
        self.bird = FlappyBird()
        self.background = Background()

    def build_image(self):
        self.background.draw_back()
        self.pipe.update()
        self.pipe.draw_column()
        self.bird.show_bird()
        self.bird.moving()
        self.pipe.moving()
        self.background.draw_base()

    def is_hit_ground(self):
        if self.bird.y_coord + self.bird.y_size > 400 + b_c:
            return True
        else:
            return False

    def is_hit_up_pipe(self):
        if self.bird.x_coord + self.bird.x_size - l_c > self.pipe.x_coord:
            if self.bird.x_coord + l_c < self.pipe.x_coord + self.pipe.width:
                if self.bird.y_coord + b_c < self.pipe.window_coord:
                    return True
        if self.bird.x_coord + self.bird.x_size - l_c > self.pipe.x_coord_new:
            if self.bird.x_coord + l_c < self.pipe.x_coord_new + self.pipe.width:
                if self.bird.y_coord + b_c < self.pipe.window_coord_new:
                    return True
        return False

    def is_hit_down_pipe(self):
        if self.bird.x_coord + self.bird.x_size - l_c > self.pipe.x_coord:
            if self.bird.x_coord + l_c < self.pipe.x_coord + self.pipe.width:
                if self.bird.y_coord + self.bird.y_size - b_c > self.pipe.window_coord + self.pipe.space:
                    return True
        if self.bird.x_coord + self.bird.x_size - l_c > self.pipe.x_coord_new:
            if self.bird.x_coord + l_c < self.pipe.x_coord_new + self.pipe.width:
                if self.bird.y_coord + self.bird.y_size - b_c > self.pipe.window_coord_new + self.pipe.space:
                    return True
        return False

    def game_over(self):
        self.background.draw_game_over_menu(self.score)
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            self.list_of_results.append(self.score // 2)
            self.pipe = column()
            self.bird = FlappyBird()
            self.is_game_over = False
            self.score = 0
        if key[pygame.K_ESCAPE]:
            self.list_of_results.append(self.score // 2)
            self.stop_run = True

    def count_score(self):
        if self.pipe.x_coord <= self.bird.x_coord <= self.pipe.x_coord + 5:
            sounds_effects['point'].play()
            self.score += 1
        if self.pipe.x_coord_new <= self.bird.x_coord <= self.pipe.x_coord_new + 5:
            sounds_effects['point'].play()
            self.score += 1

    def run(self):
        while not self.stop_run:
            pygame.time.delay(12)

            self.build_image()
            self.background.draw_score(self.score)

            if self.is_hit_ground() or self.is_hit_up_pipe() or self.is_hit_down_pipe():
                if not self.is_game_over:
                    sounds_effects['hit'].play()
                self.is_game_over = True
                self.bird.y_speed = 0
                self.bird.acceleration = 0
                self.pipe.pipe_speed = 0
                self.game_over()
            else:
                self.count_score()

            pygame.display.update()
