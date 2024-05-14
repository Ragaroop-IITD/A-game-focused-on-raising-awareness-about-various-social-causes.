# Initialize pygame
import pygame
from wordgame import main
from query import mainQuery
from dialogueMain import maindialogue


class Character:
    def __init__(self, image_path, position):
        self.image = pygame.image.load(image_path)
        self.position = position

    def draw(self, screen):
        screen.blit(self.image, self.position)

    def set_position(self, new_position):
        self.position = new_position


class OptionBox:
    def __init__(self, text, font):
        self.text = text
        self.font = font
        self.position = (0, 0)  # Initialize position
        # self.max_width = max_width  # Maximum width of the speech bubble
        self.border_radius = 20  # Border radius of the rounded rectangle
        self.border_width = 5  # Width of the border
        self.padding = 25  # Padding around the text

    def update_position(self, character_position):
        bubble_offset = (140, 0)  # Adjust the position speech bubble w.r.t image
        self.position = (character_position[0] + bubble_offset[0], character_position[1] + bubble_offset[1])

    def draw(self, screen):
        rect_width = 400
        rect_height = 100

        # Create a rectangle surface for the speech bubble
        rect_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)

        # Draw the rounded rectangle
        pygame.draw.rect(rect_surface, (100, 111, 229), (0, 0, rect_width, rect_height),
                         border_radius=self.border_radius)

        # Draw the border around the rounded rectangle
        pygame.draw.rect(rect_surface, (0, 0, 0), (0, 0, rect_width, rect_height), self.border_width,
                         border_radius=self.border_radius)

        # Blit the rectangle surface onto the screen
        screen.blit(rect_surface, self.position)

        text_render = self.font.render(self.text, True, (0, 0, 0))  # Render the text
        text_rect = text_render.get_rect(
            center=(self.position[0] + rect_width // 2, self.position[1] + rect_height // 2))
        screen.blit(text_render, text_rect)





class Intro:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.width, self.height = self.screen.get_size()
        self.font = pygame.font.Font('freesansbold.ttf', 36)
        self.bg_color = (230, 230, 230)
        self.pointer = Character('../data/assets/images/decree.png', (100, 100))
        self.conversation_box = OptionBox("Conversation", self.font)
        self.query_box = OptionBox("Query", self.font)
        self.wordgame_box = OptionBox("WordGame", self.font)

    def bubble_pos(self,image, option_bubble, x_pos, y_pos):
        image.set_position((x_pos, y_pos))
        option_bubble.update_position(image.position)
        image.draw(self.screen)
        option_bubble.draw(self.screen)

    def run(self,command):
        running = True
        while running:
            self.screen.fill(self.bg_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                # Get mouse position
                mouse_pos = pygame.mouse.get_pos()

                # Check for mouse click events
                click = pygame.mouse.get_pressed()

                # Check if the conversation_box is clicked
                if self.conversation_box.position[0] < mouse_pos[0] < self.conversation_box.position[0] + 400 and \
                        self.conversation_box.position[1] < mouse_pos[1] < self.conversation_box.position[1] + 100:
                    if click[0] == 1:
                        maindialogue(command)

                # Check if the query_box is clicked
                if self.query_box.position[0] < mouse_pos[0] < self.query_box.position[0] + 400 and \
                        self.query_box.position[1] < mouse_pos[1] < self.query_box.position[1] + 100:
                    if click[0] == 1:
                        mainQuery(command)
                        # chat(doctor)

                # Check if the wordgame_box is clicked
                if self.wordgame_box.position[0] < mouse_pos[0] < self.wordgame_box.position[0] + 400 and \
                        self.wordgame_box.position[1] < mouse_pos[1] < self.wordgame_box.position[1] + 100:
                    if click[0] == 1:
                        main(command)
                        # print("hi")

            self.bubble_pos(self.pointer, self.conversation_box, self.width // 2 - 300, self.height // 2 - 300)
            self.bubble_pos(self.pointer, self.query_box, self.width // 2 - 300, self.height // 2 - 100)
            self.bubble_pos(self.pointer, self.wordgame_box, self.width // 2 - 300, self.height // 2 + 100)

            # Update the display
            pygame.display.update()

            # Cap the frame rate
            self.clock.tick(60)


def IntroMain(command):
    intro = Intro()
    intro.run(command)

if __name__ == '__main__':
    IntroMain(0)



