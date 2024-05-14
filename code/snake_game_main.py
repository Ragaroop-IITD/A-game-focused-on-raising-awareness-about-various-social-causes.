import pygame
import sys
from SnakeGame import MAIN
from pygame.math import Vector2

class Snake_Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        
        self.clock = pygame.time.Clock()
        self.main_game = MAIN()

    def run(self):
        SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(SCREEN_UPDATE, 150)
        running=True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == SCREEN_UPDATE:
                    self.main_game.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.main_game.snake.direction.y != 1:
                            self.main_game.snake.direction = Vector2(0, -1)
                    if event.key == pygame.K_RIGHT:
                        if self.main_game.snake.direction.x != -1:
                            self.main_game.snake.direction = Vector2(1, 0)
                    if event.key == pygame.K_DOWN:
                        if self.main_game.snake.direction.y != -1:
                            self.main_game.snake.direction = Vector2(0, 1)
                    if event.key == pygame.K_LEFT:
                        if self.main_game.snake.direction.x != 1:
                            self.main_game.snake.direction = Vector2(-1, 0)
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # Fill the entire window with black color
            self.screen.fill((175,215,70))

            # Draw the game elements with offsets to center them
            self.main_game.draw_elements() 
            
            # Update the display
            pygame.display.update()
            self.clock.tick(60)
        return
# if __name__ == '__main__':
#     game = Game()
#     game.run()
