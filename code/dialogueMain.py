import pygame
import sys
from dialogue import MentalHealth,Environmental_sustainability,Elder_care,Poltical_accountability,Religious_tolerence,Sexual_Harrasment,Natural_disaster,Legal_rights,Diet,Pregnency,Election


class Mental_Health_Game:
    def __init__(self, req_class):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.mentalhealth = req_class

    def run(self):
        SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(SCREEN_UPDATE, 150)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == SCREEN_UPDATE:
                    self.mentalhealth.dialogue_run()
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_UP:
                        self.mentalhealth.vertical_position += self.mentalhealth.move_speed
                        if self.mentalhealth.vertical_position > 0:
                            self.mentalhealth.vertical_position = 0
                    elif event.key == pygame.K_DOWN:
                        self.mentalhealth.vertical_position -= self.mentalhealth.move_speed


            pygame.display.update()
            self.clock.tick(60)
        return


class_list = [MentalHealth(), Environmental_sustainability(), Elder_care(), Poltical_accountability(), Religious_tolerence(),Sexual_Harrasment(),Natural_disaster(),Legal_rights(),Diet(),Pregnency(),Election()]


def maindialogue(command):
    game = Mental_Health_Game(class_list[command])
    game.run()


if __name__ == '__main__':
    maindialogue(10)
