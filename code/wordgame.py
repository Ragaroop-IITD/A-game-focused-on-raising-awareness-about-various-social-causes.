import pygame
from word_search_generator import WordSearch


class rectangle_box:
    def __init__(self, text, font, max_width=600):
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


class rectangle_box_main:
    def __init__(self, text, font, max_width=700):
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
            rendered_lines = [self.font.render(line, True, (250, 235, 215)) for line in lines]
        else:
            rendered_lines = [self.font.render(self.text, True, (250, 235, 215))]

        # Calculate the height required for rendering text
        total_height = len(rendered_lines) * self.font.get_linesize()

        # Calculate the dimensions of the rounded rectangle
        rect_width = speech_width
        rect_height = total_height + 2 * self.padding

        # Create a rectangle surface for the speech bubble
        rect_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)

        # Draw the rounded rectangle
        pygame.draw.rect(rect_surface, (31, 9, 84), (0, 0, rect_width, rect_height),
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


# Function to display the word search puzzle
def display_puzzle(puzzle, words, game):
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))

    font_size = 36
    font = pygame.font.Font(None, font_size)
    text_color = (215, 130, 87)
    line_color = (0, 0, 0)
    highlight_color = (88, 104, 132)  # Color for highlighting selected letters
    line_thickness = 5  # Increase this value to increase grid and gridlines thickness

    # Calculate grid size and position
    screen_width, screen_height = screen.get_size()
    grid_margin = min(screen_width, screen_height) // 12
    grid_size = min(screen_width, screen_height) - 2 * grid_margin
    vertical_margin = (screen_height - grid_size) // 2

    cell_size = grid_size // puzzle.size

    selected_cells = set()

    def highlight_selected():
        for cell in selected_cells:
            x, y = cell
            pygame.draw.rect(screen, highlight_color,
                             (grid_margin + x * cell_size, vertical_margin + y * cell_size,
                              cell_size, cell_size))

    def check_word_found(selected_cells):
        nonlocal words
        word = ""
        # Combine selected letters into a word
        for cell in sorted(selected_cells):
            x, y = cell
            word += puzzle.puzzle[y][x]

        # Convert the selected word to lowercase
        word = word.upper()

        print("Selected word:", word)  # Debugging print statement

        # Check if the word is in the word list
        if word in words:
            words.remove(word)
            selected_cells.clear()  # Clear selected cells after a word is found
            if not words:
                print("All words found!")
                return True
        return False

    running = True

    while running:
        screen.fill((235, 235, 235))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    game.vertical_position += game.move_speed
                    if game.vertical_position > 0:
                        game.vertical_position = 0
                elif event.key == pygame.K_DOWN:
                    game.vertical_position -= game.move_speed
                    if game.vertical_position < -1500:
                        game.vertical_position = -1500
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = event.pos
                    cell_x = (x - grid_margin) // cell_size
                    cell_y = (y - vertical_margin) // cell_size
                    if 0 <= cell_x < puzzle.size and 0 <= cell_y < puzzle.size:
                        cell = (cell_x, cell_y)
                        if cell in selected_cells:
                            selected_cells.remove(cell)
                        else:
                            selected_cells.add(cell)
                        if check_word_found(selected_cells):
                            print("Game Over!")
                            running = False

        game.run()

        # Draw grid lines
        for i in range(puzzle.size + 1):
            pygame.draw.line(screen, line_color, (grid_margin, vertical_margin + i * cell_size),
                             (grid_margin + grid_size, vertical_margin + i * cell_size), line_thickness)
            pygame.draw.line(screen, line_color, (grid_margin + i * cell_size, vertical_margin),
                             (grid_margin + i * cell_size, vertical_margin + grid_size), line_thickness)

        # Highlight selected cells
        highlight_selected()

        # Render word list
        vertical_margin_wordlist = 400  # Set the vertical margin for the word list
        horizontal_margin_wordlist = -350  # Set the horizontal margin for the word list
        for i, word in enumerate(words):
            text_surface = font.render(word, True, text_color)
            text_rect = text_surface.get_rect(centerx=(screen_width - horizontal_margin_wordlist) // 2,
                                              top=vertical_margin_wordlist + i * font_size)  # Adjusted calculation
            screen.blit(text_surface, text_rect)

        for y, row in enumerate(puzzle.puzzle):
            for x, cell in enumerate(row):
                # Render the letter in the center of the square
                text_surface = font.render(cell, True, text_color)
                text_rect = text_surface.get_rect(center=(grid_margin + x * cell_size + cell_size // 2,
                                                          vertical_margin + y * cell_size + cell_size // 2))
                screen.blit(text_surface, text_rect)

        pygame.display.flip()


class wordgame0:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.vertical_position = 0
        self.move_speed = 100

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 22)
        heading_font = pygame.font.Font('freesansbold.ttf', 24)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1300, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1300, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def run(self):
        word_0 = "Anxiety:"
        text_0 = "A feeling of worry, nervousness, or unease about something with an uncertain outcome. Anxiety disorders involve excessive and persistent feelings of anxiety that can interfere with daily life."
        word_1 = "Depression:"
        text_1 = "A mood disorder characterized by persistent feelings of sadness, hopelessness, and loss of interest or pleasure in activities. Depression can affect how a person thinks, feels, and behaves."
        word_2 = "Therapy:"
        text_2 = "Treatment for mental health issues provided by a trained therapist or counselor. Therapy can include various approaches such as cognitive-behavioral therapy, psychotherapy, and counseling."
        word_3 = "Stress:"
        text_3 = "A physiological and psychological response to demands or challenges in life. While some stress can be normal and even helpful in certain situations, chronic or excessive stress can negatively impact mental and physical health."
        word_4 = "Resilience:"
        text_4 = "The ability to adapt and bounce back from adversity, challenges, or trauma. Resilience involves coping effectively with stressors and maintaining mental health and well-being in the face of difficulties."
        word_5 = "Wellness:"
        text_5 = "An overall state of health and well-being that encompasses physical, emotional, social, and mental aspects of life. Wellness involves actively pursuing behaviors and practices that promote optimal health and quality of life."

        self.notebox_pos(word_0, text_0, 100)
        self.notebox_pos(word_1, text_1, 400)
        self.notebox_pos(word_2, text_2, 700)
        self.notebox_pos(word_3, text_3, 1000)
        self.notebox_pos(word_4, text_4, 1300)
        self.notebox_pos(word_5, text_5, 1600)


class wordgame1:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.vertical_position = 0
        self.move_speed = 100

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 22)
        heading_font = pygame.font.Font('freesansbold.ttf', 24)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1300, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1300, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def run(self):
        word_0 = "Renewable Energy:"
        text_0 = "Renewable energy refers to energy sources that are naturally replenished, such as sunlight, wind, and water. Unlike fossil fuels, which are finite and contribute to climate change, renewable energy sources are sustainable and environmentally friendly."
        word_1 = "Conservation:"
        text_1 = "Conservation involves the protection, preservation, and sustainable use of natural resources, ecosystems, and biodiversity. It aims to maintain the health and integrity of the environment for current and future generations."
        word_2 = "Greenhouse Gas Emissions:"
        text_2 = "Greenhouse gases are gases that trap heat in the Earth's atmosphere, contributing to global warming and climate change. Common greenhouse gases include carbon dioxide, methane, and nitrous oxide, primarily emitted from human activities such as burning fossil fuels, deforestation, and agriculture."
        word_3 = "Environmental Justice:"
        text_3 = "Environmental justice addresses the unequal distribution of environmental benefits and burdens among communities, particularly marginalized and low-income populations. It advocates for fair treatment and meaningful involvement of all people, regardless of race, ethnicity, or socioeconomic status, in environmental decision-making and policy implementation."

        self.notebox_pos(word_0, text_0, 100)
        self.notebox_pos(word_1, text_1, 450)
        self.notebox_pos(word_2, text_2, 800)
        self.notebox_pos(word_3, text_3, 1200)


class wordgame2:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.vertical_position = 0
        self.move_speed = 100

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 22)
        heading_font = pygame.font.Font('freesansbold.ttf', 24)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1300, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1300, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def run(self):
        word_0 = "Caregiver:"
        text_0 = "A caregiver is someone who provides assistance and support to an elderly or disabled individual. Caregivers can be family members, friends, or hired professionals and may help with tasks ranging from personal care to household chores and medical management."

        word_1 = "Dementia: "
        text_1 = "Dementia is a general term for a decline in cognitive function severe enough to interfere with daily life. Alzheimer's disease is the most common type of dementia, but there are several other forms as well. Symptoms may include memory loss, confusion, difficulty with language and communication, and changes in mood or behavior."
        word_2 = "Geriatrician: "
        text_2 = "A geriatrician is a medical doctor who specializes in the care of elderly patients. Geriatricians have expertise in managing the complex health issues and unique needs of older adults, including multiple chronic conditions, medication management, and age-related changes in physiology and cognition."

        word_3 = "Assisted Living: "
        text_3 = "Assisted living facilities provide housing and support services for seniors who need assistance with activities of daily living (ADLs) but do not require intensive medical care. Residents typically live in private apartments and receive help with tasks such as bathing, dressing, and medication management."

        self.notebox_pos(word_0, text_0, 100)
        self.notebox_pos(word_1, text_1, 450)
        self.notebox_pos(word_2, text_2, 820)
        self.notebox_pos(word_3, text_3, 1190)


class wordgame3:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.vertical_position = 0
        self.move_speed = 100

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 22)
        heading_font = pygame.font.Font('freesansbold.ttf', 24)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1300, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1300, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def run(self):
        word_0 = "Transparency:"
        text_0 = "Transparency refers to the openness and accessibility of government actions, decisions, and information to the public. It ensures that citizens can understand how decisions are made and how public resources are utilized, which is crucial for holding officials accountable."
        word_1 = "Checks and Balances:"
        text_1 = "Checks and balances are mechanisms within a government system that distribute power among different branches (such as the legislative, executive, and judicial branches) to prevent any one branch from becoming too powerful. This system helps ensure accountability by allowing each branch to monitor and check the actions of the others."
        word_2 = "Oversight Mechanisms:"
        text_2 = "Oversight mechanisms are structures and processes, including independent agencies, audit offices, and investigative bodies, that oversee government actions and hold officials accountable for their decisions and use of public resources. These mechanisms help detect and prevent corruption, abuse of power, and inefficiency."
        word_3 = "Judicial Accountability:"
        text_3 = "Judicial accountability refers to the responsibility of the judiciary to uphold the rule of law and ensure justice is administered fairly and impartially. It involves holding judges and courts accountable for their decisions and actions, including adherence to legal standards and ethical conduct."

        self.notebox_pos(word_0, text_0, 100)
        self.notebox_pos(word_1, text_1, 500)
        self.notebox_pos(word_2, text_2, 900)
        self.notebox_pos(word_3, text_3, 1300)


class wordgame4:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.vertical_position = 0
        self.move_speed = 100

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 22)
        heading_font = pygame.font.Font('freesansbold.ttf', 24)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1300, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1300, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def run(self):
        word_0 = "Pluralism:"
        text_0 = "Pluralism refers to the acceptance and celebration of diversity within society, including religious diversity. It emphasizes the coexistence of different religious beliefs and practices without promoting any single ideology as superior."
        word_1 = "Secularism:"
        text_1 = "Secularism is the principle of separating religion from governmental and political affairs. It ensures that the state remains neutral in matters of religion, allowing individuals of all faiths (or none) to participate equally in public life without discrimination."
        word_2 = "Religious Freedom:"
        text_2 = "Religious freedom is the right of individuals to practice, change, or abstain from religion according to their conscience, without interference from the government or other authorities. It encompasses the freedom to worship, assemble, and express one's beliefs openly."
        word_3 = "Intolerance:"
        text_3 = "Intolerance refers to the unwillingness or refusal to accept and respect beliefs, practices, or opinions that differ from one's own, especially in matters of religion. It can manifest as discrimination, prejudice, or hostility towards individuals or groups based on their religious affiliations."
        word_4 = "Coexistence:"
        text_4 = "Coexistence signifies the peaceful and harmonious living together of individuals or communities with diverse religious backgrounds. It involves mutual respect, understanding, and acceptance of differences, fostering a sense of unity and cooperation despite varying beliefs."
        word_5 = "Inclusivity:"
        text_5 = " Inclusivity emphasizes the importance of including and embracing individuals from all religious backgrounds within society. It promotes equal opportunities and treatment for people of different faiths, ensuring that everyone feels valued and respected regardless of their religious affiliations."

        self.notebox_pos(word_0, text_0, 100)
        self.notebox_pos(word_1, text_1, 450)
        self.notebox_pos(word_2, text_2, 870)
        self.notebox_pos(word_3, text_3, 1300)
        self.notebox_pos(word_4, text_4, 1650)
        self.notebox_pos(word_5, text_5, 2000)


class wordgame5:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.vertical_position = 0
        self.move_speed = 100

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 22)
        heading_font = pygame.font.Font('freesansbold.ttf', 24)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1300, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1300, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def run(self):
        word_0 = "Verbal Harassment:"
        text_0 = "Verbal harassment involves the use of words, comments, or language of a sexual nature that is unwelcome and creates a hostile or uncomfortable environment for the recipient."
        word_1 = "Physical Harassment:"
        text_1 = "Physical harassment involves any unwanted physical contact or advances of a sexual nature, including touching, groping, or assault."
        word_2 = "Quid Pro Quo:"
        text_2 = "Quid pro quo harassment occurs when a person in a position of authority requests sexual favors in exchange for employment benefits, promotions, or other favorable treatment."
        word_3 = "Hostile Work Environment:"
        text_3 = "A hostile work environment is created when unwelcome sexual conduct, comments, or behavior makes it difficult for an individual to perform their job duties, leading to a hostile, intimidating, or offensive workplace atmosphere."
        word_4 = "Retaliation:"
        text_4 = "Retaliation occurs when an individual faces adverse actions or consequences, such as demotion, termination, or ostracism, as a result of reporting or resisting sexual harassment."
        word_5 = "Consent:"
        text_5 = "Consent is the voluntary agreement to engage in sexual activity. It should be clear, informed, and freely given by all parties involved. Without consent, any sexual activity is considered harassment or assault."

        self.notebox_pos(word_0, text_0, 100)
        self.notebox_pos(word_1, text_1, 450)
        self.notebox_pos(word_2, text_2, 870)
        self.notebox_pos(word_3, text_3, 1300)
        self.notebox_pos(word_4, text_4, 1650)
        self.notebox_pos(word_5, text_5, 2000)


class wordgame6:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.vertical_position = 0
        self.move_speed = 100

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 22)
        heading_font = pygame.font.Font('freesansbold.ttf', 24)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1300, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1300, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def run(self):
        word_0 = "Earthquake:"
        text_0 = "A sudden and violent shaking of the ground, often caused by the movement of tectonic plates beneath the Earth's surface."
        word_1 = "Hurricane:"
        text_1 = "A large, rotating storm system characterized by strong winds, heavy rain, and storm surges, typically forming over warm ocean waters."
        word_2 = "Tornado:"
        text_2 = "A rapidly rotating column of air extending from a thunderstorm to the ground, capable of causing significant damage and destruction in its path."
        word_3 = "Flood:"
        text_3 = "An overflow of water onto normally dry land, often caused by heavy rainfall, melting snow, or the overflow of rivers and lakes."
        word_4 = "Wildfire:"
        text_4 = "An uncontrolled fire that spreads rapidly through vegetation, fueled by dry conditions, high winds, and combustible materials."
        word_5 = "Tsunami:"
        text_5 = "A series of large ocean waves caused by underwater earthquakes, volcanic eruptions, or landslides, capable of causing widespread destruction along coastlines."

        self.notebox_pos(word_0, text_0, 100)
        self.notebox_pos(word_1, text_1, 400)
        self.notebox_pos(word_2, text_2, 700)
        self.notebox_pos(word_3, text_3, 1000)
        self.notebox_pos(word_4, text_4, 1330)
        self.notebox_pos(word_5, text_5, 1650)


class wordgame7:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.vertical_position = 0
        self.move_speed = 100

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 22)
        heading_font = pygame.font.Font('freesansbold.ttf', 24)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1300, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1300, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def run(self):
        word_0 = "Habeas Corpus:"
        text_0 = "Habeas corpus is a legal principle that protects individuals from being unlawfully detained or imprisoned. It allows individuals to challenge the legality of their detention before a court and requires authorities to provide a valid legal reason for holding someone in custody."
        word_1 = "Miranda Rights:"
        text_1 = "Miranda rights are a set of rights that must be read to individuals upon arrest or custodial interrogation. These rights include the right to remain silent and the right to legal representation. The Miranda warning ensures that individuals are aware of their rights during the legal process."
        word_2 = "Freedom of Speech:"
        text_2 = "Freedom of speech is a fundamental right that allows individuals to express their opinions and ideas without censorship or government interference. It is protected by various legal frameworks and constitutions in democratic societies."
        word_3 = "Right to Privacy:"
        text_3 = "The right to privacy protects individuals from unwanted intrusion into their personal lives and affairs. It encompasses privacy rights in areas such as communications, personal data, and bodily integrity, and is essential for maintaining autonomy and dignity."
        word_4 = "Right to a Fair Trial:"
        text_4 = "The right to a fair trial guarantees that individuals accused of crimes have the opportunity to present their case before an impartial judge and jury. It includes rights such as the presumption of innocence, the right to legal representation, and the right to confront witnesses."
        # word_5 = "Tsunami:"
        # text_5 = "A series of large ocean waves caused by underwater earthquakes, volcanic eruptions, or landslides, capable of causing widespread destruction along coastlines."

        self.notebox_pos(word_0, text_0, 100)
        self.notebox_pos(word_1, text_1, 400)
        self.notebox_pos(word_2, text_2, 700)
        self.notebox_pos(word_3, text_3, 1000)
        self.notebox_pos(word_4, text_4, 1330)
        # self.notebox_pos(word_5, text_5, 1650)


class wordgame8:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.vertical_position = 0
        self.move_speed = 100

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 22)
        heading_font = pygame.font.Font('freesansbold.ttf', 24)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1300, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1300, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def run(self):
        word_0 = "Nutrients:"
        text_0 = "Nutrients are substances in food that are essential for growth, development, and overall health. They include carbohydrates, proteins, fats, vitamins, minerals, and water."
        word_1 = "Fiber:"
        text_1 = "Fiber is a type of carbohydrate found in plant-based foods like fruits, vegetables, whole grains, nuts, and seeds. It aids in digestion, helps regulate blood sugar levels, and promotes feelings of fullness."
        word_2 = "Antioxidants:"
        text_2 = "Antioxidants are compounds found in foods like fruits, vegetables, nuts, and dark chocolate that help protect cells from damage caused by free radicals. They may reduce the risk of chronic diseases such as heart disease and cancer."
        word_3 = "Probiotics:"
        text_3 = "Probiotics are beneficial bacteria found in fermented foods like yogurt, kefir, sauerkraut, and kimchi. They help maintain a healthy balance of gut bacteria, which is important for digestion and immune function."
        word_4 = "Hydration:"
        text_4 = "Hydration refers to maintaining adequate fluid balance in the body by consuming enough water throughout the day. It's important for regulating body temperature, aiding digestion, and transporting nutrients and oxygen to cells."
        word_5 = "Healthy Fats:"
        text_5 = "Healthy fats, such as those found in avocados, nuts, seeds, olive oil, and fatty fish, are important for brain health, hormone production, and absorbing fat-soluble vitamins. They also help reduce inflammation and protect against heart disease."

        self.notebox_pos(word_0, text_0, 100)
        self.notebox_pos(word_1, text_1, 400)
        self.notebox_pos(word_2, text_2, 700)
        self.notebox_pos(word_3, text_3, 1000)
        self.notebox_pos(word_4, text_4, 1330)
        self.notebox_pos(word_5, text_5, 1650)


class wordgame9:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.vertical_position = 0
        self.move_speed = 100

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 22)
        heading_font = pygame.font.Font('freesansbold.ttf', 24)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1300, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1300, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def run(self):
        word_0 = "Ultrasound:"
        text_0 = "An imaging technique that uses high-frequency sound waves to create images of the developing fetus in the womb. It helps monitor fetal growth and development, as well as detect any abnormalities."
        word_1 = "Braxton Hicks:"
        text_1 = "Also known as practice contractions, these are sporadic uterine contractions that can occur during pregnancy, usually in the second or third trimester. They are typically mild and irregular and help prepare the uterus for labor."
        word_2 = "Amniocentesis"
        text_2 = "A prenatal test where a small sample of amniotic fluid is extracted from the uterus using a needle. It is usually performed between 15 and 20 weeks of pregnancy to screen for genetic disorders and chromosomal abnormalities."
        word_3 = "Episiotomy:"
        text_3 = "A surgical incision made in the perineum (the area between the vagina and anus) during childbirth to widen the vaginal opening and facilitate delivery. It may be performed to prevent tearing or to expedite the birth process."
        word_4 = "Cesarean Section:"
        text_4 = "Also known as a C-section, it is a surgical procedure used to deliver a baby through incisions made in the mother's abdomen and uterus. It may be planned in advance or performed as an emergency procedure if vaginal delivery is not possible or safe."
        word_5 = "Colostrum:"
        text_5 = "A thick, yellowish fluid produced by the breasts during pregnancy and the first few days after childbirth. It is rich in antibodies and nutrients and serves as the baby's first food before breast milk production begins."

        self.notebox_pos(word_0, text_0, 100)
        self.notebox_pos(word_1, text_1, 400)
        self.notebox_pos(word_2, text_2, 700)
        self.notebox_pos(word_3, text_3, 1000)
        self.notebox_pos(word_4, text_4, 1330)
        self.notebox_pos(word_5, text_5, 1650)


class wordgame10:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.vertical_position = 0
        self.move_speed = 100

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 22)
        heading_font = pygame.font.Font('freesansbold.ttf', 24)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1300, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1300, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def run(self):
        word_0 = "Ballot:"
        text_0 = "A ballot is a piece of paper or electronic device used to cast a vote in an election. Voters mark their choices on the ballot to indicate their preferred candidates or options."
        word_1 = "Campaign: "
        text_1 = "A campaign refers to the organized efforts by candidates, political parties, or advocacy groups to promote their platform, persuade voters, and win elections. Campaigns often involve activities such as rallies, debates, advertising, and canvassing."
        word_2 = "Polling Station:"
        text_2 = "A polling station is a designated location where voters go to cast their ballots during an election. Polling stations are typically set up in public buildings such as schools, community centers, or churches."
        word_3 = "Gerrymandering:"
        text_3 = "Gerrymandering is the manipulation of electoral district boundaries to favor a particular political party or group. Gerrymandering is often used to concentrate the voting power of one party or to dilute the voting power of certain communities."
        word_4 = "Exit Poll:"
        text_4 = "An exit poll is a survey conducted with voters as they leave the polling station after voting. Exit polls are used to predict election outcomes and analyze voting patterns."
        # word_5 = "Colostrum:"
        # text_5 = "A thick, yellowish fluid produced by the breasts during pregnancy and the first few days after childbirth. It is rich in antibodies and nutrients and serves as the baby's first food before breast milk production begins."

        self.notebox_pos(word_0, text_0, 100)
        self.notebox_pos(word_1, text_1, 400)
        self.notebox_pos(word_2, text_2, 700)
        self.notebox_pos(word_3, text_3, 1000)
        self.notebox_pos(word_4, text_4, 1330)
        # self.notebox_pos(word_5, text_5, 1650)


words = [["ANXIETY", "DEPRESSION", "THERAPY", "STRESS", "RESILIENCE", "WELLNESS"],
         ["RENEWABLE", "ENERGY", "CONSERVATION", "GREENHOUSE", "ENVIRONMENT"],
         ["CARE", "LIVING", "DEMENTIA", "CAREGIVER", "GERIATRICIAN"],
         ["TRANSPARENCY", "CHECKS", "BALANCES", "MECHANISMS", "JUDICIAL"],
         ["PLURALISM", "SECULARISM", "FREEDOM", "INTOLERENCE", "COEXISTENCE", "INCLUSIVITY"],
         ["HARASSMENT", "VERBAL", "PHYSICAL", "QUIDPROQUO", "HOSTILE", "RETALIATION, ""CONSENT"],
         ["EARTHQUAKE", "HURRICANE", "TORNADO", "FLOOD", "WILDFIRE", "TSUNAMI"],
         ["HABEASCORPUS", "MIRANDA", "RIGHTS", "FREEDOM", "PRIVACY", "TRAIL"],
         ["NUTIENTS", "FIBRE", "ANTIOXIDANTS", "PROBIOTICS", "HYDRATION", "FATS"],
         ["ULTRASOUND", "HICKS", "AMNIOCENTESIS", "EPISIOTOMY", "CESAREAN", "COLOSTRUM"],
         ["BALLOT", "CAMPAIGN", "POLLING", "ELECTION", "PARTY", "POLITICS"]]
word_gam_class_list = [wordgame0(), wordgame1(), wordgame2(), wordgame3(), wordgame4(), wordgame5(), wordgame6(),
                       wordgame7(), wordgame8(), wordgame9(), wordgame10()]


def main(command):
    # Generate the word search puzzle
    puzzle = WordSearch(", ".join(words[command]))
    puzzle.directions = "E,S"
    puzzle.show()

    game = word_gam_class_list[command]

    # Display the puzzle
    display_puzzle(puzzle, (words[command]), game)


if __name__ == "__main__":
    main(10)