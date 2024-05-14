import pygame,sys
from settings import *
from map import Map
# from debug import debug

class Game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)
        pygame.display.set_caption('Aware Isle')
        icon=pygame.image.load("../data/assets/island.png")
        pygame.display.set_icon(icon)
        self.clock=pygame.time.Clock()

        self.map=Map()
        
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('black')
            self.map.run()
            pygame.display.update()
            self.clock.tick(fps)

if __name__=='__main__':
    game =Game()
    game.run()