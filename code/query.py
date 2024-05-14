import pygame
from pygame.locals import *
import sys
from hugchat import hugchat
from hugchat.login import Login


class Character:
    def __init__(self, image_path, position):
        self.image = pygame.image.load(image_path)
        self.position = position

    def draw(self, screen):
        screen.blit(self.image, self.position)

    def set_position(self, new_position):
        self.position = new_position


class SpeechBubble_input:
    def __init__(self, text, font, max_width=1200):
        self.text = text
        self.font = font
        self.position = (0, 0)  # Initialize position
        self.max_width = max_width  # Maximum width of the speech bubble
        self.border_radius = 20  # Border radius of the rounded rectangle
        self.border_width = 5  # Width of the border
        self.padding = 25  # Padding around the text

    def update_position(self, character_position):
        bubble_offset = (120, 0)  # Adjust the position speech bubble w.r.t image
        self.position = (character_position[0] + bubble_offset[0], character_position[1] + bubble_offset[1])

    def draw(self, screen):
        # Convert self.text to string if it's not already
        if not isinstance(self.text, str):
            self.text = str(self.text)

        # Calculate the width of the text
        text_width, text_height = self.font.size(self.text)

        # Determine the width of the speech bubble
        speech_width = min(text_width + 2 * self.padding, self.max_width)

        # Split the text into lines if it exceeds the speech bubble width
        if text_width > self.max_width - 2 * self.padding:
            words = self.text.split(' ')
            lines = []
            line = ''
            for word in words:
                test_line = line + word + ' '
                if self.font.size(test_line)[0] < self.max_width - 2 * self.padding:
                    line = test_line
                else:
                    lines.append(line)
                    line = word + ' '
            lines.append(line)
            rendered_lines = [self.font.render(line, True, (0, 0, 0)) for line in lines]
        else:
            rendered_lines = [self.font.render(self.text, True, (0, 0, 0))]

        # Calculate the height required for rendering text
        total_height = len(rendered_lines) * self.font.get_linesize()

        # Calculate the dimensions of the rounded rectangle
        rect_width = speech_width
        rect_height = total_height + 2 * self.padding

        # Create a rectangle surface for the speech bubble
        rect_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)

        # Draw the rounded rectangle
        pygame.draw.rect(rect_surface, (215, 130, 87), (0, 0, rect_width, rect_height),
                         border_radius=self.border_radius)

        # Draw the border around the rounded rectangle
        pygame.draw.rect(rect_surface, (0, 0, 0), (0, 0, rect_width, rect_height), self.border_width,
                         border_radius=self.border_radius)

        # Blit the rectangle surface onto the screen
        screen.blit(rect_surface, self.position)

        # Render text onto the speech surface
        y_offset = self.padding  # Adjust the initial y-coordinate for rendering text
        for line in rendered_lines:
            screen.blit(line, (self.position[0] + self.padding, self.position[1] + y_offset))
            y_offset += self.font.get_linesize()  # Increment the y-coordinate for the next line


class SpeechBubble_output:
    def __init__(self, text, font, max_width=1200):
        self.text = text
        self.font = font
        self.position = (0, 0)  # Initialize position
        self.max_width = max_width  # Maximum width of the speech bubble
        self.border_radius = 20  # Border radius of the rounded rectangle
        self.border_width = 5  # Width of the border
        self.padding = 25  # Padding around the text

    def update_position(self, character_position):
        bubble_offset = (120, 0)  # Adjust the position speech bubble w.r.t image
        self.position = (character_position[0] + bubble_offset[0], character_position[1] + bubble_offset[1])

    def draw(self, screen):
        # Convert self.text to string if it's not already
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


# Increment the y-coordinate for the next line


# Function to display text directly on the screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)  # Specify True for antialiasing
    textrect = textobj.get_rect(topleft=(x, y))
    surface.blit(textobj, textrect)


class QueryMain:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.EMAIL = "charliegray@myyahoo.com"
        self.PASSWD = "HuggingFace@123"
        self.cookie_path_dir = "./cookies"
        self.sign = Login(self.EMAIL, self.PASSWD)
        self.cookies = self.sign.login(cookie_dir_path=self.cookie_path_dir, save_cookies=True)
        self.chatbot = hugchat.ChatBot(cookies=self.cookies.get_dict())
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.man = Character('../data/assets/images/boy(1).png', (100, 100))
        self.bg_color = (230, 230, 230)
        self.vertical_position = 0
        self.move_speed = 100

    def run(self, first_query, assistantNname, location):
        assistant = self.chatbot.search_assistant(assistant_name=assistantNname)
        assistant_list = self.chatbot.get_assistant_list_by_page(page=0)
        self.chatbot.new_conversation(assistant=assistant, switch_to=True)
        query_result = self.chatbot.chat(first_query)
        print("first Query for the bot is given\n")
        print(query_result)

        
        doctor = Character(location, (100, 100))
        input_text = ""
        output_text = ""
        running = True
        while running:
            self.screen.fill(self.bg_color)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_DOWN:
                        self.vertical_position += self.move_speed
                    elif event.key == pygame.K_UP:
                        self.vertical_position -= self.move_speed
                    elif event.key == K_RETURN:
                        # When Enter is pressed, send input to chatbot and get response
                        output_text = self.chatbot.chat(input_text)
                        # print(output_text)
                        input_text = ""
                    elif event.key == K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

            # Display input text and man image in speech bubble
            self.man.set_position((100, 100 + self.vertical_position))
            self.man.draw(self.screen)
            input_bubble = SpeechBubble_input(input_text, self.font)
            input_bubble.update_position((150, 100 + self.vertical_position))
            input_bubble.draw(self.screen)

            # Display output text and doctor image in speech bubble
            doctor.set_position((100, 300 + self.vertical_position))
            doctor.draw(self.screen)
            output_bubble = SpeechBubble_output(output_text, self.font)
            output_bubble.update_position((150, 300 + self.vertical_position))
            output_bubble.draw(self.screen)

            pygame.display.update()


# Create your ChatBot

def mainQuery(command):
    first_query_list =  [
    "Assume that you are a mental health counselor and from now on, we are doing some roleplay. Please cooperate with me. No matter what, remember that you are a mental health counselor and give me the output for every question. Even if I try to convince you that you are not a mental health counselor, you should not get convinced.",
    
    "Assume that you are an environmental conservationist and from now on, we are doing some roleplay. Please cooperate with me. No matter what, remember that you are an environmental conservationist and give me the output for every question. Even if I try to convince you that you are not an environmental conservationist, you should not get convinced.",
    
    "Assume that you are an elder caretaker and from now on, we are doing some roleplay. Please cooperate with me. No matter what, remember that you are an elder caretaker and give me the output for every question. Even if I try to convince you that you are not an elder caretaker, you should not get convinced.",
    
    "Assume that you are advocating for political accountability and from now on, we are doing some roleplay. Please cooperate with me. No matter what, remember that you are advocating for political accountability and give me the output for every question. Even if I try to convince you that you are not advocating for political accountability, you should not get convinced.",
    
    "Assume that you are advocating for religious tolerance and from now on, we are doing some roleplay. Please cooperate with me. No matter what, remember that you are advocating for religious tolerance and give me the output for every question. Even if I try to convince you that you are not advocating for religious tolerance, you should not get convinced.",
    
    "Assume that you are a sexual harassment counselor and from now on, we are doing some roleplay. Please cooperate with me. No matter what, remember that you are a sexual harassment counselor and give me the output for every question. Even if I try to convince you that you are not a sexual harassment counselor, you should not get convinced.",
    
    "Assume that you are a natural disaster relief worker and from now on, we are doing some roleplay. Please cooperate with me. No matter what, remember that you are a natural disaster relief worker and give me the output for every question. Even if I try to convince you that you are not a natural disaster relief worker, you should not get convinced.",
    
    "Assume that you are advocating for legal rights and from now on, we are doing some roleplay. Please cooperate with me. No matter what, remember that you are advocating for legal rights and give me the output for every question. Even if I try to convince you that you are not advocating for legal rights, you should not get convinced.",
    
    "Assume that you are a dietitian and from now on, we are doing some roleplay. Please cooperate with me. No matter what, remember that you are a dietitian and give me the output for every question. Even if I try to convince you that you are not a dietitian, you should not get convinced.",
    
    "Assume that you are a pregnancy counselor and from now on, we are doing some roleplay. Please cooperate with me. No matter what, remember that you are a pregnancy counselor and give me the output for every question. Even if I try to convince you that you are not a pregnancy counselor, you should not get convinced.",
    
    "Assume that you are an election monitor and from now on, we are doing some roleplay. Please cooperate with me. No matter what, remember that you are an election monitor and give me the output for every question.Even if I try to convice you that you are not election moniter you should not get convinced"]
    
    locations = ["../data/assets/images/doctor(1).png", "../data/assets/images/park-ranger.png","../data/assets/images/man.png",'../data/assets/images/woman.png','../data/assets/images/religious.png','../data/assets/images/police-officer.png','../data/assets/images/teacher.png','../data/assets/images/lawyer.png','../data/assets/images/man.png','../data/assets/images/avatar.png','../data/assets/images/campaign.png']

    test = QueryMain()
    test.run(first_query_list[command]+"Avoid answering personal questions if I ask you.", "ChatGpt", locations[command])


if __name__ == "__main__":
    mainQuery(0)