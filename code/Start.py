# Initialize pygame
import pygame


class OptionBox:
    def __init__(self, text, font, max_width=1080):
        self.text = text
        self.font = font
        self.position = (0, 0)  # Initialize position
        self.max_width = max_width  # Maximum width of the speech bubble
        self.border_radius = 20  # Border radius of the rounded rectangle
        self.border_width = 5  # Width of the border
        self.padding = 25  # Padding around the text

    def update_position(self, new_position):
        self.position = new_position

    def draw(self, screen):
        if not isinstance(self.text, str):
            self.text = str(self.text)

        # Split the text into lines based on newline characters (\n) if they exist
        lines = self.text.split('\n')

        # Initialize a list to store lines after wrapping
        wrapped_lines = []

        # Loop through each line to wrap text to the next line if it exceeds max_width
        for line in lines:
            if self.font.size(line)[0] <= self.max_width - 2 * self.padding:
                wrapped_lines.append(line)
            else:
                words = line.split(' ')
                wrapped_line = ''
                for word in words:
                    test_line = wrapped_line + word + ' '
                    if self.font.size(test_line)[0] < self.max_width - 2 * self.padding:
                        wrapped_line = test_line
                    else:
                        wrapped_lines.append(wrapped_line)
                        wrapped_line = word + ' '
                wrapped_lines.append(wrapped_line)

        # Calculate the width required for rendering text
        text_width = max([self.font.size(line)[0] for line in wrapped_lines]) + 2 * self.padding

        # Set the rectangle width to the calculated text width if it's less than max_width
        rect_width = min(text_width, self.max_width)

        # Calculate the height required for rendering text
        total_height = len(wrapped_lines) * self.font.get_linesize()

        # Calculate the dimensions of the rounded rectangle
        rect_height = total_height + 2 * self.padding

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

        # Render text onto the speech surface
        y_offset = self.padding  # Adjust the initial y-coordinate for rendering text
        for line in wrapped_lines:
            rendered_line = self.font.render(line, True, (250, 235, 215))
            screen.blit(rendered_line, (self.position[0] + self.padding, self.position[1] + y_offset))
            y_offset += self.font.get_linesize()





class Instructions:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.width, self.height = self.screen.get_size()
        self.font = pygame.font.Font('freesansbold.ttf', 36)
        self.bg_color = (230, 230, 230)
        self.pointer = pygame.image.load('../data/assets/mini_map.png')
        self.conversation_box = OptionBox("Conversation", self.font)
        self.query_box = OptionBox("Query", self.font)
        self.heading_box = OptionBox(f"How to Play?\n\nIn this game you need to go to different locations to gain awareness on different topics.\nYou can always refer the map below to go where you want to go.\n\nThe building you can visit are given below with their coordinates you can refer to your player coordinates at the top left corner\n\n1.Mental health care center  x:{172-124} y:{120-112}\n2.Enviromentalist    x:{93-124} y:{78-112}\n3.Nursery House    x:{146-124} y:{137-112}\n4.Political activist  x:{106-124} y:{98-112}\n5.Lotus Temple  x:{116-124} y:{158-112}\n6.Police station  x:{118-124} y:{72-112}\n7.Library  x:{148-124} y:{96-112}\n8.Lawyer office  x:{148-124} y:{72-112}\n9.Food court  x:{102-124} y:{118-112}\n10.Arcade  x:{173-124} y:{144-112}\n11.Hospital  x:{1173-124} y:{96-112}\n12.Election office  x:{154-124} y:{162-112}", self.font)  # Move to __init__
        self.vertical_position = 0
        self.move_speed = 100

    def bubble_pos(self, image, option_bubble, x_pos, y_pos):
        image.set_position((x_pos, y_pos))
        option_bubble.update_position(image.position)
        image.draw(self.screen)
        option_bubble.draw(self.screen)

    def run(self):
        running = True
        while running:
            self.screen.fill(self.bg_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_UP:
                        self.vertical_position += self.move_speed
                        if self.vertical_position > 0:
                            self.vertical_position = 0
                    elif event.key == pygame.K_DOWN:
                        # Ensure heading stays within screen height
                        if self.vertical_position - self.move_speed > -self.height + self.heading_box.font.get_linesize()-300:
                            self.vertical_position -= self.move_speed

            # Draw the heading box
            heading_pos = (420, 100 + self.vertical_position)
            self.heading_box.update_position(heading_pos)
            self.heading_box.draw(self.screen)

            # Draw the resized image
            resized_image = pygame.transform.scale(self.pointer, (1100, 1100))
            self.screen.blit(resized_image, (500, 1200 + self.vertical_position))

            pygame.display.update()

            # Cap the frame rate
            self.clock.tick(60)


def InstrMain():
    intro = Instructions()
    intro.run()

if __name__=='__main__':
    InstrMain()


