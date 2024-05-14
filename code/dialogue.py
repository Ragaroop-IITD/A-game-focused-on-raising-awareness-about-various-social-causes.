import pygame


class Character:
    def __init__(self, image_path, position):
        self.image = pygame.image.load(image_path)
        self.position = position

    def draw(self, screen):
        screen.blit(self.image, self.position)

    def set_position(self, new_position):
        self.position = new_position


class SpeechBubble:
    def __init__(self, text, font, max_width=600):
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
        pygame.draw.rect(rect_surface, (100, 111, 229), (0, 0, rect_width, rect_height),
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


class SpeechBubble_man:
    def __init__(self, text, font, max_width=600):
        self.text = text
        self.font = font
        self.position = (0, 0)  # Initialize position
        self.max_width = max_width  # Maximum width of the speech bubble
        self.border_radius = 20  # Border radius of the rounded rectangle
        self.border_width = 5  # Width of the border
        self.padding = 25  # Padding around the text

    def update_position(self, character_position):
        # Calculate the width of the text
        text_width, _ = self.font.size(self.text)

        # Calculate the width of the speech bubble
        speech_width = min(text_width + 2 * self.padding, self.max_width)

        # Calculate the x-coordinate of the speech bubble
        bubble_x = character_position[0] - speech_width - self.padding + 25

        # Calculate the y-coordinate of the speech bubble
        bubble_y = character_position[1]

        # Update the position of the speech bubble
        self.position = (bubble_x, bubble_y)

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
        pygame.draw.rect(rect_surface, (206, 172, 62), (0, 0, rect_width, rect_height),
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


class rectangle_box:
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


class MentalHealth:
    def __init__(self):
        self.vertical_position = 0
        self.move_speed = 100
        self.screen = pygame.display.set_mode((1920, 1080))
        self.width, self.height = self.screen.get_size()
        self.bg_color = (230, 230, 230)

    def set_y_pos(self, SpeechBubbleDoc, SpeechBubbleMan, y_doc, y_man):
        doctor = Character('../data/assets/images/doctor(1).png', (100, 100))
        man = Character('../data/assets/images/boy(1).png', (100, 100))

        doctor.set_position((50, y_doc + self.vertical_position))
        SpeechBubbleDoc.update_position(doctor.position)
        doctor.draw(self.screen)
        SpeechBubbleDoc.draw(self.screen)

        man.set_position((900, y_man + self.vertical_position))
        SpeechBubbleMan.update_position(man.position)
        man.draw(self.screen)
        SpeechBubbleMan.draw(self.screen)

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 24)
        heading_font = pygame.font.Font('freesansbold.ttf', 26)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1100, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1100, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def dialogue_run(self):
        self.screen.fill(self.bg_color)

        # doctor = Character('../data/assets/images/doctor(1).png', (100, 100))
        # man = Character('../data/assets/images/boy(1).png', (100, 100))

        font = pygame.font.Font('freesansbold.ttf', 24)
        speech_bubble_0 = SpeechBubble(
            "Good morning, welcome. I'm glad you're here. How are you feeling today?",
            font)
        speech_bubble_man_0 = SpeechBubble_man(
            "Hi, thank you. Honestly, I'm feeling quite overwhelmed. I've been struggling with my mental health lately, and it's been really tough to cope.",
            font)
        speech_bubble_1 = SpeechBubble(
            "I'm sorry to hear that you've been going through a difficult time. You've taken a brave step by coming here today. Would you like to share more about what you've been experiencing?",
            font)
        speech_bubble_man_1 = SpeechBubble_man(
            "Well, it's like... I just feel like I can't seem to shake off this constant sense of anxiety and sadness. It's affecting my work, my relationships, everything really. I just don't know how to deal with it anymore.",
            font)
        speech_bubble_2 = SpeechBubble(
            "It sounds like you've been carrying a heavy burden for a while. It's important to acknowledge that what you're feeling is valid. Let's work together to understand what might be contributing to these feelings. Have you noticed any specific triggers or patterns in your thoughts and behaviors?",
            font)
        speech_bubble_man_2 = SpeechBubble_man(
            "Yeah, I think so. Certain situations or even just small things can set off this spiral of negative thoughts. And then it feels like I'm stuck in this cycle, unable to break free from it.",
            font)
        speech_bubble_3 = SpeechBubble(
            "It's common to get caught up in those negative thought patterns, but it's also possible to learn how to manage them. One approach we can explore is cognitive-behavioral therapy, which focuses on identifying and challenging those negative thoughts. We can work on developing coping strategies to help you respond to them more effectively.",
            font)
        speech_bubble_man_3 = SpeechBubble_man(
            "That sounds like it could be really helpful. I'm willing to try anything at this point.",
            font)
        speech_bubble_4 = SpeechBubble(
            "Great, I'm glad to hear you're open to exploring different approaches. Alongside therapy, we can also discuss lifestyle changes and self-care practices that can support your mental well-being. Building a strong support network and practicing mindfulness techniques can also be beneficial.",
            font)
        speech_bubble_man_4 = SpeechBubble_man(
            "That all sounds good to me. I just want to feel like myself again, you know?", font)
        speech_bubble_5 = SpeechBubble(
            "Absolutely, and I'm here to support you every step of the way. It's important to remember that healing takes time, and it's okay to ask for help when you need it. You've already shown courage by seeking support, and I have no doubt that we can work together to help you feel better.",
            font)
        speech_bubble_man_5 = SpeechBubble_man(
            "Thank you, I really appreciate your support. I'm feeling a bit hopeful already.", font)
        speech_bubble_6 = SpeechBubble(
            "You're welcome. Remember, you're not alone in this journey. We'll take it one step at a time, and I'm here to walk alongside you.",
            font)
        speech_bubble_man_6 = SpeechBubble_man("Thank you", font)

        self.set_y_pos(speech_bubble_0, speech_bubble_man_0, 100, 250)
        self.set_y_pos(speech_bubble_1, speech_bubble_man_1, 450, 680)
        self.set_y_pos(speech_bubble_2, speech_bubble_man_2, 910, 1200)
        self.set_y_pos(speech_bubble_3, speech_bubble_man_3, 1440, 1790)
        self.set_y_pos(speech_bubble_4, speech_bubble_man_4, 1950, 2270)
        self.set_y_pos(speech_bubble_5, speech_bubble_man_5, 2430, 2720)
        self.set_y_pos(speech_bubble_6, speech_bubble_man_6, 2880, 3050)

        heading_font = pygame.font.Font('freesansbold.ttf', 30)

        heading_box = rectangle_box_main("Tips & Tricks to avoid Mental-Health issues", heading_font)
        heading_pos = (1100, 100 + self.vertical_position)
        heading_box.update_position(heading_pos)
        heading_box.draw(self.screen)

        word_0 = "1. Seek Professional Help:"
        text_0 = "Reach out to a therapist, counselor, or mental health professional who can provide support, guidance, and appropriate treatment options tailored to your needs."
        word_1 = "2. Practice Self-Compassion:"
        text_1 = "Be kind to yourself and recognize that it's okay to struggle sometimes. Treat yourself with the same empathy and understanding that you would offer to a friend in a similar situation."
        word_2 = "3. Develop Coping Strategies:"
        text_2 = "Identify healthy coping mechanisms that work for you, such as mindfulness, deep breathing exercises, journaling, or engaging in hobbies and activities you enjoy."
        word_3 = "4. Establish Routine:"
        text_3 = "Create a daily routine that includes regular sleep patterns, healthy meals, exercise, and structured activities. Consistency can provide stability and a sense of control."
        word_4 = "5. Stay Connected:"
        text_4 = "Maintain relationships with supportive friends, family members, or support groups who can offer encouragement, understanding, and companionship during difficult times."
        word_5 = "6. Limit Stressors:"
        text_5 = "Identify and minimize sources of stress in your life as much as possible. Set boundaries, prioritize tasks, and delegate responsibilities when needed to avoid feeling overwhelmed."
        word_6 = "7. Practice Mindfulness:"
        text_6 = "Incorporate mindfulness techniques into your daily routine, such as meditation, yoga, or mindful breathing exercises, to help you stay grounded and focused in the present moment."
        word_7 = "8. Set Realistic Goals:"
        text_7 = "Break larger goals into smaller, manageable steps, and celebrate your progress along the way. Focus on achievable outcomes and be patient with yourself during setbacks."
        word_8 = "9. Engage in Positive Activities:"
        text_8 = "Surround yourself with activities and experiences that bring you joy, fulfillment, and a sense of purpose. This could include spending time outdoors, volunteering, or pursuing creative outlets."
        word_9 = "10. Celebrate Progress:"
        text_9 = "Acknowledge and celebrate your achievements, no matter how small they may seem. Recognize your resilience and progress toward recovery, and give yourself credit for your efforts."

        self.notebox_pos(word_0, text_0, 250)
        self.notebox_pos(word_1, text_1, 570)
        self.notebox_pos(word_2, text_2, 930)
        self.notebox_pos(word_3, text_3, 1270)
        self.notebox_pos(word_4, text_4, 1610)
        self.notebox_pos(word_5, text_5, 1950)
        self.notebox_pos(word_6, text_6, 2290)
        self.notebox_pos(word_7, text_7, 2630)
        self.notebox_pos(word_8, text_8, 2980)
        self.notebox_pos(word_9, text_9, 3330)

        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 890, 50), (self.width - 890, self.height - 50), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 885, 50), (self.width - 885, self.height - 50), 3)


class Environmental_sustainability:
    def __init__(self):
        self.vertical_position = 0
        self.move_speed = 100
        self.screen = pygame.display.set_mode((1920, 1080))
        self.width, self.height = self.screen.get_size()
        self.bg_color = (230, 230, 230)

    def set_y_pos(self, SpeechBubbleDoc, SpeechBubbleMan, y_doc, y_man):
        main = Character('../data/assets/images/park-ranger.png', (100, 100))
        man = Character('../data/assets/images/boy(1).png', (100, 100))

        man.set_position((50, y_doc + self.vertical_position))
        SpeechBubbleDoc.update_position(man.position)
        man.draw(self.screen)
        SpeechBubbleDoc.draw(self.screen)

        main.set_position((900, y_man + self.vertical_position))
        SpeechBubbleMan.update_position(main.position)
        main.draw(self.screen)
        SpeechBubbleMan.draw(self.screen)

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 24)
        heading_font = pygame.font.Font('freesansbold.ttf', 26)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1100, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1100, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def dialogue_run(self):
        self.screen.fill(self.bg_color)

        font = pygame.font.Font('freesansbold.ttf', 24)
        speech_bubble_0 = SpeechBubble(
            "Hi there! I heard you're an environmentalist. I've been thinking lately about how we can raise awareness about environmental sustainability. Got any tips?",
            font)
        speech_bubble_man_0 = SpeechBubble_man(
            "Absolutely! One effective way is through education and outreach programs. We can organize workshops, seminars, and community events to inform people about the importance of environmental conservation.",
            font)
        speech_bubble_1 = SpeechBubble(
            "That sounds great! But how do we ensure people actually attend these events?",
            font)
        speech_bubble_man_1 = SpeechBubble_man(
            "We can use social media platforms to promote our events and reach a wider audience. Also, partnering with local schools, businesses, and organizations can help us spread the word effectively.",
            font)
        speech_bubble_2 = SpeechBubble(
            "That makes sense. What about reaching out to policymakers? How can we influence them to prioritize environmental sustainability?",
            font)
        speech_bubble_man_2 = SpeechBubble_man(
            "Engaging with policymakers is crucial. We can organize petitions, write letters, and even schedule meetings to discuss environmental issues and advocate for policy changes that promote sustainability.",
            font)
        speech_bubble_3 = SpeechBubble(
            "That sounds like a proactive approach. But what about those who are still not convinced about the urgency of environmental conservation?",
            font)
        speech_bubble_man_3 = SpeechBubble_man(
            "It's important to address their concerns and misconceptions with facts and evidence. Sharing success stories and showcasing the tangible benefits of sustainable practices can help change hearts and minds.",
            font)
        speech_bubble_4 = SpeechBubble(
            "That's a good point. Do you think individual actions really make a difference in the grand scheme of things?",
            font)
        speech_bubble_man_4 = SpeechBubble_man(
            "Absolutely! Every small action counts. Whether it's reducing waste, conserving energy, or supporting eco-friendly products, individual choices collectively have a significant impact on the environment.",
            font)
        speech_bubble_5 = SpeechBubble(
            "I'm inspired to take action now. Thanks for your insights!",
            font)
        speech_bubble_man_5 = SpeechBubble_man(
            "Thank you.",
            font)

        self.set_y_pos(speech_bubble_0, speech_bubble_man_0, 100, 300)
        self.set_y_pos(speech_bubble_1, speech_bubble_man_1, 530, 680)
        self.set_y_pos(speech_bubble_2, speech_bubble_man_2, 910, 1100)
        self.set_y_pos(speech_bubble_3, speech_bubble_man_3, 1340, 1550)
        self.set_y_pos(speech_bubble_4, speech_bubble_man_4, 1780, 1970)
        self.set_y_pos(speech_bubble_5, speech_bubble_man_5, 2230, 2400)

        heading_font = pygame.font.Font('freesansbold.ttf', 30)

        heading_box = rectangle_box_main("Important points about Environment", heading_font)
        heading_pos = (1100, 100 + self.vertical_position)
        heading_box.update_position(heading_pos)
        heading_box.draw(self.screen)

        word_0 = "1. Conservation of Resources:"
        text_0 = "Environmental sustainability involves using natural resources in a way that ensures their availability for future generations. This includes practices such as reducing waste, conserving water, and minimizing energy consumption."

        word_1 = "2. Biodiversity Preservation:"
        text_1 = "Maintaining biodiversity is crucial for the stability and resilience of ecosystems. Protecting habitats, preventing species extinction, and promoting conservation efforts help preserve biodiversity."

        word_2 = "3. Mitigating Climate Change:"
        text_2 = "Environmental sustainability aims to reduce greenhouse gas emissions and mitigate climate change effects. This includes transitioning to renewable energy sources, promoting energy efficiency, and implementing climate-resilient infrastructure."

        word_3 = "4. Waste Reduction and Recycling:"
        text_3 = "Minimizing waste generation and promoting recycling are key components of environmental sustainability. Adopting circular economy principles, such as reusing materials and extending product lifecycles, helps reduce environmental impact."

        word_4 = "5. Sustainable Agriculture and Food Systems:"
        text_4 = "Sustainable agriculture practices prioritize soil health, water conservation, and biodiversity conservation. Emphasizing local and organic food production, reducing food waste, and promoting sustainable farming methods contribute to environmental sustainability."

        word_5 = "6. Responsible Consumption and Production:"
        text_5 = "Encouraging sustainable consumption patterns involves choosing products with minimal environmental impact, reducing overconsumption, and supporting ethical and eco-friendly businesses. Additionally, implementing sustainable production processes reduces resource use and pollution."

        word_6 = "7. Environmental Justice and Equity:"
        text_6 = "Environmental sustainability should address social inequalities and ensure that all communities have access to clean air, water, and a healthy environment. Promoting environmental justice involves addressing environmental racism, supporting marginalized communities, and involving stakeholders in decision-making processes."

        word_7 = "8. Education and Awareness:"
        text_7 = "Raising awareness about environmental issues and promoting environmental literacy are essential for fostering a culture of sustainability. Educating individuals, communities, and businesses about the interconnectedness of human activities and the environment encourages responsible behavior and informed decision-making."

        word_8 = "9. Collaboration and Partnerships:"
        text_8 = "Achieving environmental sustainability requires collaboration among governments, businesses, NGOs, communities, and individuals. Building partnerships, sharing knowledge and resources, and fostering cooperation at local, national, and global levels are essential for addressing complex environmental challenges."

        word_9 = "10. Long-Term Planning and Policy Development:"
        text_9 = "Implementing effective policies and regulations that promote environmental protection and sustainable development is crucial. Long-term planning, evidence-based decision-making, and integrated approaches to environmental management help ensure a sustainable future for current and future generations."

        self.notebox_pos(word_0, text_0, 250)
        self.notebox_pos(word_1, text_1, 590)
        self.notebox_pos(word_2, text_2, 930)
        self.notebox_pos(word_3, text_3, 1300)
        self.notebox_pos(word_4, text_4, 1660)
        self.notebox_pos(word_5, text_5, 2030)
        self.notebox_pos(word_6, text_6, 2390)
        self.notebox_pos(word_7, text_7, 2810)
        self.notebox_pos(word_8, text_8, 3200)
        self.notebox_pos(word_9, text_9, 3630)

        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 890, 50), (self.width - 890, self.height - 50), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 885, 50), (self.width - 885, self.height - 50), 3)


class Elder_care:
    def __init__(self):
        self.vertical_position = 0
        self.move_speed = 100
        self.screen = pygame.display.set_mode((1920, 1080))
        self.width, self.height = self.screen.get_size()
        self.bg_color = (230, 230, 230)

    def set_y_pos(self, SpeechBubbleDoc, SpeechBubbleMan, y_doc, y_man):
        main = Character('../data/assets/images/man.png', (100, 100))
        man = Character('../data/assets/images/boy(1).png', (100, 100))

        main.set_position((50, y_doc + self.vertical_position))
        SpeechBubbleDoc.update_position(main.position)
        main.draw(self.screen)
        SpeechBubbleDoc.draw(self.screen)

        man.set_position((900, y_man + self.vertical_position))
        SpeechBubbleMan.update_position(man.position)
        man.draw(self.screen)
        SpeechBubbleMan.draw(self.screen)

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 24)
        heading_font = pygame.font.Font('freesansbold.ttf', 26)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1100, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1100, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def dialogue_run(self):
        self.screen.fill(self.bg_color)

        font = pygame.font.Font('freesansbold.ttf', 24)
        speech_bubble_0 = SpeechBubble(
            "Hey there, I wanted to talk to you about something important today. Have you ever thought about elder care?",
            font)
        speech_bubble_man_0 = SpeechBubble_man(
            "Elder care? Not really, why do you ask?",
            font)
        speech_bubble_1 = SpeechBubble(
            "Well, it's something that's been on my mind a lot lately. You see, as our parents and grandparents age, their needs change, and sometimes they require assistance with everyday tasks or even medical care.",
            font)
        speech_bubble_man_1 = SpeechBubble_man(
            "That makes sense. I guess I haven't really thought about it much. What kind of assistance do they need?",
            font)
        speech_bubble_2 = SpeechBubble(
            "It varies from person to person, but it can include help with things like bathing, dressing, meal preparation, medication management, and even companionship. Some elders also need assistance with mobility or managing chronic conditions.",
            font)
        speech_bubble_man_2 = SpeechBubble_man(
            "Wow, I didn't realize there were so many aspects to it. How do people typically provide elder care?",
            font)
        speech_bubble_3 = SpeechBubble(
            "There are a few different options. Some families choose to take on the responsibility themselves, providing care for their loved ones at home. Others may opt for assisted living facilities or nursing homes, where trained professionals can provide round-the-clock care.",
            font)
        speech_bubble_man_3 = SpeechBubble_man(
            "That's a lot to consider. How do you know what the best option is?",
            font)
        speech_bubble_4 = SpeechBubble(
            "It really depends on the individual's needs, preferences, and financial situation. Sometimes it's helpful to consult with a social worker or elder care specialist who can provide guidance and help you weigh your options.",
            font)
        speech_bubble_man_4 = SpeechBubble_man(
            "That sounds like a good idea. I'll definitely keep that in mind. Thanks for bringing it up and explaining it to me.",
            font)
        speech_bubble_5 = SpeechBubble(
            "Of course, no problem. It's something that affects many families, so it's important to have these conversations and plan ahead as much as possible.",
            font)
        speech_bubble_man_5 = SpeechBubble_man(
            "Thank you.",
            font)

        self.set_y_pos(speech_bubble_0, speech_bubble_man_0, 100, 290)
        self.set_y_pos(speech_bubble_1, speech_bubble_man_1, 430, 680)
        self.set_y_pos(speech_bubble_2, speech_bubble_man_2, 890, 1150)
        self.set_y_pos(speech_bubble_3, speech_bubble_man_3, 1340, 1630)
        self.set_y_pos(speech_bubble_4, speech_bubble_man_4, 1800, 2080)
        self.set_y_pos(speech_bubble_5, speech_bubble_man_5, 2280, 2470)

        heading_font = pygame.font.Font('freesansbold.ttf', 30)

        heading_box = rectangle_box_main("Tips for better Elder-care", heading_font)
        heading_pos = (1100, 100 + self.vertical_position)
        heading_box.update_position(heading_pos)
        heading_box.draw(self.screen)

        word_0 = "1.  Assessment of Needs:"
        text_0 = "Each elder's needs are unique, so it's crucial to assess their physical, emotional, and social requirements before deciding on a care plan."

        word_1 = "2.  Communication and Involvement:"
        text_1 = "Involving the elder in decision-making about their care empowers them and ensures their preferences are respected. Clear communication among family members and caregivers is also essential."

        word_2 = "3.  Safety and Accessibility:"
        text_2 = "Creating a safe environment is paramount. This includes preventing falls, ensuring medication safety, and making necessary modifications to the home for accessibility."

        word_3 = "4.  Healthcare Management:"
        text_3 = "Managing medications, scheduling medical appointments, and coordinating with healthcare providers are vital aspects of elder care, especially for those with chronic conditions."

        word_4 = "5.  Nutrition and Hydration:"
        text_4 = "Proper nutrition and hydration are crucial for maintaining health and well-being. Caregivers should ensure elders have access to nutritious meals and adequate fluids."

        word_5 = "6.  Social Engagement:"
        text_5 = "Social isolation can have detrimental effects on an elder's mental and emotional health. Encouraging social activities, whether through family visits, community events, or senior centers, is important."

        word_6 = "7.  Respite for Caregivers:"
        text_6 = "Caregiving can be demanding physically, emotionally, and mentally. Providing respite care, where other family members or professional caregivers temporarily relieve the primary caregiver, is essential for preventing burnout."

        word_7 = "8.  Legal and Financial Planning:"
        text_7 = "Planning for the elder's future, including legal matters such as wills, powers of attorney, and advance directives, as well as financial planning for long-term care expenses, is crucial."

        word_8 = "9.  Monitoring and Adjusting Care Plans:"
        text_8 = "Elders' needs can change over time, so it's essential to regularly monitor their health and well-being and adjust care plans accordingly."

        word_9 = "10.  Self-Care for Caregivers:"
        text_9 = "Caregivers must prioritize their own physical and emotional well-being. This includes seeking support from others, taking breaks when needed, and seeking professional help if feeling overwhelmed."

        self.notebox_pos(word_0, text_0, 250)
        self.notebox_pos(word_1, text_1, 550)
        self.notebox_pos(word_2, text_2, 900)
        self.notebox_pos(word_3, text_3, 1250)
        self.notebox_pos(word_4, text_4, 1600)
        self.notebox_pos(word_5, text_5, 1950)
        self.notebox_pos(word_6, text_6, 2280)
        self.notebox_pos(word_7, text_7, 2650)
        self.notebox_pos(word_8, text_8, 3000)
        self.notebox_pos(word_9, text_9, 3300)

        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 890, 50), (self.width - 890, self.height - 50), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 885, 50), (self.width - 885, self.height - 50), 3)

class Poltical_accountability:
    def __init__(self):
        self.vertical_position = 0
        self.move_speed = 100
        self.screen = pygame.display.set_mode((1920, 1080))
        self.width, self.height = self.screen.get_size()
        self.bg_color = (230, 230, 230)

    def set_y_pos(self, SpeechBubbleDoc, SpeechBubbleMan, y_doc, y_man):
        # main = Character('../data/assets/images/main(1).png', (100, 100))
        # man = Character('../data/assets/images/boy(1).png', (100, 100))
        main = Character('../data/assets/images/woman.png', (100, 100))
        man = Character('../data/assets/images/boy(1).png', (100, 100))

        main.set_position((50, y_doc + self.vertical_position))
        SpeechBubbleDoc.update_position(main.position)
        main.draw(self.screen)
        SpeechBubbleDoc.draw(self.screen)

        man.set_position((900, y_man + self.vertical_position))
        SpeechBubbleMan.update_position(man.position)
        man.draw(self.screen)
        SpeechBubbleMan.draw(self.screen)

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 24)
        heading_font = pygame.font.Font('freesansbold.ttf', 26)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1100, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1100, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def dialogue_run(self):
        self.screen.fill(self.bg_color)

        # doctor = Character('../data/assets/images/doctor(1).png', (100, 100))
        # man = Character('../data/assets/images/boy(1).png', (100, 100))

        font = pygame.font.Font('freesansbold.ttf', 24)
        speech_bubble_0 = SpeechBubble(
            "Hey, have you ever thought about the importance of political accountability?",
            font)
        speech_bubble_man_0 = SpeechBubble_man(
            "Hmm, not really. What's that all about?",
            font)
        speech_bubble_1 = SpeechBubble(
            "Well, political accountability refers to the responsibility of government officials and institutions to the public and the mechanisms through which they can be held answerable for their actions.",
            font)
        speech_bubble_man_1 = SpeechBubble_man(
            "It's crucial because it ensures transparency, honesty, and integrity in governance. When politicians know they're accountable, they're more likely to act in the public's best interest.",
            font)
        speech_bubble_2 = SpeechBubble(
            "Makes sense. But how can we spread awareness about this?",
            font)
        speech_bubble_man_2 = SpeechBubble_man(
            "One way is through education and advocacy. We can organize workshops, seminars, and social media campaigns to inform people about their rights and how they can hold politicians accountable.",
            font)
        speech_bubble_3 = SpeechBubble(
            "That sounds like a plan. But won't it be challenging to get people interested?",
            font)
        speech_bubble_man_3 = SpeechBubble_man(
            "It might be, but we can start small and gradually build momentum. We need to show people how political accountability affects their lives directly.",
            font)
        speech_bubble_4 = SpeechBubble(
            "True. I guess once people understand its importance, they'll be more motivated to get involved.",
            font)
        speech_bubble_man_4 = SpeechBubble_man(
            "Exactly! And by empowering citizens with knowledge, we can create a more accountable and responsive government.",
            font)
        speech_bubble_5 = SpeechBubble(
            "I'm onboard. Count me in for spreading awareness about political accountability!",
            font)
        speech_bubble_man_5 = SpeechBubble_man(
            "That's fantastic to hear! Together, we can make a real difference in promoting a more accountable political system.",
            font)

        self.set_y_pos(speech_bubble_0, speech_bubble_man_0, 100, 250)
        self.set_y_pos(speech_bubble_1, speech_bubble_man_1, 400, 650)
        self.set_y_pos(speech_bubble_2, speech_bubble_man_2, 880, 1050)
        self.set_y_pos(speech_bubble_3, speech_bubble_man_3, 1300, 1460)
        self.set_y_pos(speech_bubble_4, speech_bubble_man_4, 1700, 1900)
        self.set_y_pos(speech_bubble_5, speech_bubble_man_5, 2100, 2270)

        heading_font = pygame.font.Font('freesansbold.ttf', 30)

        heading_box = rectangle_box_main("Important points about Political Accountability", heading_font)
        heading_pos = (1100, 100 + self.vertical_position)
        heading_box.update_position(heading_pos)
        heading_box.draw(self.screen)

        word_0 = "1.  Definition:"
        text_0 = "Political accountability refers to the obligation of government officials and institutions to act in accordance with the laws and norms of society and to be answerable for their actions."

        word_1 = "2.  Transparency:"
        text_1 = "Political accountability requires transparency in government actions and decision-making processes. Citizens should have access to information about how decisions are made and how public resources are utilized."

        word_2 = "3.  Checks and Balances:"
        text_2 = "A system of checks and balances is essential for political accountability. This involves the separation of powers among different branches of government (legislative, executive, and judicial) to prevent any one branch from becoming too powerful and to ensure accountability."

        word_3 = "4.  Electoral Accountability:"
        text_3 = "In democratic systems, political accountability is often achieved through elections. Elected officials are accountable to the electorate, who can choose to re-elect or remove them from office based on their performance."

        word_4 = "5.  Oversight Mechanisms:"
        text_4 = "Independent oversight bodies, such as ombudsmen, audit offices, and anticorruption agencies, play a crucial role in holding government officials accountable. These bodies investigate complaints, audit government activities, and ensure compliance with laws and regulations."

        word_5 = "6.  Civil Society and Media:"
        text_5 = "Civil society organizations, including non-governmental organizations (NGOs), advocacy groups, and the media, serve as watchdogs to monitor government actions and hold officials accountable. They provide a platform for citizen engagement and help expose corruption and abuses of power."

        word_6 = "7.  Legal Accountability:"
        text_6 = "Political leaders and government officials can be held legally accountable for their actions through the judicial system. This includes prosecution for criminal activities, civil lawsuits for misconduct, and judicial review of government decisions."

        word_7 = "8.  Ethical Standards:"
        text_7 = "Political accountability also encompasses adherence to ethical standards and codes of conduct. Elected officials are expected to act with integrity, honesty, and in the best interests of the public they serve."

        word_8 = "9.  International Standards:"
        text_8 = "Many international agreements and conventions promote political accountability as a fundamental principle of good governance. Countries may be held accountable for their adherence to these standards through international monitoring and peer review mechanisms."

        word_9 = "10.  Continuous Improvement:"
        text_9 = "Political accountability is an ongoing process that requires constant vigilance and improvement. It involves not only holding current officials accountable but also implementing reforms to strengthen democratic institutions and ensure greater transparency, participation, and integrity in governance."

        self.notebox_pos(word_0, text_0, 250)
        self.notebox_pos(word_1, text_1, 570)
        self.notebox_pos(word_2, text_2, 930)
        self.notebox_pos(word_3, text_3, 1270)
        self.notebox_pos(word_4, text_4, 1610)
        self.notebox_pos(word_5, text_5, 1950)
        self.notebox_pos(word_6, text_6, 2290)
        self.notebox_pos(word_7, text_7, 2630)
        self.notebox_pos(word_8, text_8, 2980)
        self.notebox_pos(word_9, text_9, 3330)

        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 890, 50), (self.width - 890, self.height - 50), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 885, 50), (self.width - 885, self.height - 50), 3)


class Religious_tolerence:
    def __init__(self):
        self.vertical_position = 0
        self.move_speed = 100
        self.screen = pygame.display.set_mode((1920, 1080))
        self.width, self.height = self.screen.get_size()
        self.bg_color = (230, 230, 230)

    def set_y_pos(self, SpeechBubbleDoc, SpeechBubbleMan, y_doc, y_man):
        # main = Character('../data/assets/images/main(1).png', (100, 100))
        # man = Character('../data/assets/images/boy(1).png', (100, 100))
        main = Character('../data/assets/images/religious.png', (100, 100))
        man = Character('../data/assets/images/boy(1).png', (100, 100))

        main.set_position((50, y_doc + self.vertical_position))
        SpeechBubbleDoc.update_position(main.position)
        main.draw(self.screen)
        SpeechBubbleDoc.draw(self.screen)

        man.set_position((900, y_man + self.vertical_position))
        SpeechBubbleMan.update_position(man.position)
        man.draw(self.screen)
        SpeechBubbleMan.draw(self.screen)

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 24)
        heading_font = pygame.font.Font('freesansbold.ttf', 26)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1100, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1100, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def dialogue_run(self):
        self.screen.fill(self.bg_color)

        # doctor = Character('../data/assets/images/doctor(1).png', (100, 100))
        # man = Character('../data/assets/images/boy(1).png', (100, 100))

        font = pygame.font.Font('freesansbold.ttf', 24)
        speech_bubble_0 = SpeechBubble(
            "Hi there! Have you ever thought about the importance of religious tolerance in our society?",
            font)
        speech_bubble_man_0 = SpeechBubble_man(
            "Hmm, not really. Why do you think it's so important?",
            font)
        speech_bubble_1 = SpeechBubble(
            "Well, think about it. Our world is incredibly diverse, with people from all walks of life and belief systems. Religious tolerance ensures that everyone can coexist peacefully, despite our differences.",
            font)
        speech_bubble_man_1 = SpeechBubble_man(
            " I see your point. But sometimes it feels like religious differences cause more harm than good.",
            font)
        speech_bubble_2 = SpeechBubble(
            "That's true, but that's precisely why spreading awareness about religious tolerance is crucial. It helps bridge the gap between different faiths and promotes understanding and acceptance.",
            font)
        speech_bubble_man_2 = SpeechBubble_man(
            "How can we promote religious tolerance effectively?",
            font)
        speech_bubble_3 = SpeechBubble(
            "Education plays a significant role. By teaching people about different religions and cultures, we can break down stereotypes and foster empathy.",
            font)
        speech_bubble_man_3 = SpeechBubble_man(
            "But what about deeply ingrained prejudices?",
            font)
        speech_bubble_4 = SpeechBubble(
            "Overcoming prejudices is challenging, but it's not impossible. It starts with individuals like us engaging in open-minded conversations and challenging discriminatory beliefs when we encounter them.",
            font)
        speech_bubble_man_4 = SpeechBubble_man(
            "So, it's about fostering a culture of respect and acceptance?",
            font)
        speech_bubble_5 = SpeechBubble(
            "Exactly! When we respect each other's beliefs and practices, we create a more harmonious society where everyone feels valued and included.",
            font)
        speech_bubble_man_5 = SpeechBubble_man(
            "That makes sense. I'll definitely start paying more attention to promoting religious tolerance in my community.",
            font)
        speech_bubble_6 = SpeechBubble(
            "That's great to hear! Every small step we take towards promoting tolerance can make a big difference in the long run.",
            font)
        speech_bubble_man_6 = SpeechBubble_man("Thank you.", font)

        self.set_y_pos(speech_bubble_0, speech_bubble_man_0, 100, 300)
        self.set_y_pos(speech_bubble_1, speech_bubble_man_1, 470, 720)
        self.set_y_pos(speech_bubble_2, speech_bubble_man_2, 930, 1180)
        self.set_y_pos(speech_bubble_3, speech_bubble_man_3, 1350, 1560)
        self.set_y_pos(speech_bubble_4, speech_bubble_man_4, 1700, 1960)
        self.set_y_pos(speech_bubble_5, speech_bubble_man_5, 2130, 2350)
        self.set_y_pos(speech_bubble_6, speech_bubble_man_6, 2550, 2770)

        heading_font = pygame.font.Font('freesansbold.ttf', 30)

        heading_box = rectangle_box_main("Important points about Religious Tolerence", heading_font)
        heading_pos = (1100, 100 + self.vertical_position)
        heading_box.update_position(heading_pos)
        heading_box.draw(self.screen)

        word_0 = "1.  Foundation of Diversity:"
        text_0 = "Religious tolerance is a cornerstone of a diverse society. It acknowledges and respects the existence of various religious beliefs and practices within a community or nation."

        word_1 = "2.  Freedom of Religion:"
        text_1 = "It is a fundamental human right recognized by international law. People have the freedom to practice their religion or belief system without fear of discrimination or persecution."

        word_2 = "3.  Promotes Peaceful Coexistence:"
        text_2 = "Religious tolerance fosters harmony and peaceful coexistence among individuals and communities with different religious backgrounds. It encourages mutual respect, understanding, and acceptance."

        word_3 = "4.  Counteracts Prejudice and Discrimination:"
        text_3 = "Tolerance helps counteract prejudices and stereotypes associated with certain religious groups. It challenges discriminatory attitudes and promotes empathy and compassion."

        word_4 = "5.  Strengthens Social Cohesion:"
        text_4 = "Embracing religious diversity strengthens the fabric of society by promoting social cohesion and unity. It encourages collaboration and cooperation among people of different faiths towards common goals."

        word_5 = "6.  Facilitates Dialogue and Understanding:"
        text_5 = "Tolerance paves the way for constructive dialogue and interfaith exchanges. It allows individuals to engage in meaningful conversations, share perspectives, and learn from one another."

        word_6 = "7.  Respects Individual Beliefs:"
        text_6 = "Religious tolerance acknowledges that everyone has the right to hold their own beliefs and practices, as long as they do not infringe upon the rights of others or cause harm."

        word_7 = "8.  Challenges Extremism and Intolerance:"
        text_7 = "By promoting tolerance, societies can combat extremism and religious intolerance, which can lead to conflict and violence. It encourages moderation and respect for diverse viewpoints."

        word_8 = "9.  Educational and Legal Frameworks:"
        text_8 = "Building educational programs and legal frameworks that promote religious tolerance is essential for its widespread acceptance and implementation. Education plays a crucial role in shaping attitudes and behaviors towards religious diversity."

        word_9 = "10. Continuous Effort:"
        text_9 = "Religious tolerance requires ongoing effort and commitment from individuals, communities, and governments. It is a journey towards building a more inclusive and equitable society for all."

        self.notebox_pos(word_0, text_0, 250)
        self.notebox_pos(word_1, text_1, 570)
        self.notebox_pos(word_2, text_2, 930)
        self.notebox_pos(word_3, text_3, 1270)
        self.notebox_pos(word_4, text_4, 1610)
        self.notebox_pos(word_5, text_5, 1950)
        self.notebox_pos(word_6, text_6, 2290)
        self.notebox_pos(word_7, text_7, 2630)
        self.notebox_pos(word_8, text_8, 2980)
        self.notebox_pos(word_9, text_9, 3330)

        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 890, 50), (self.width - 890, self.height - 50), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 885, 50), (self.width - 885, self.height - 50), 3)


class Sexual_Harrasment:
    def __init__(self):
        self.vertical_position = 0
        self.move_speed = 100
        self.screen = pygame.display.set_mode((1920, 1080))
        self.width, self.height = self.screen.get_size()
        self.bg_color = (230, 230, 230)

    def set_y_pos(self, SpeechBubbleDoc, SpeechBubbleMan, y_doc, y_man):
        # main = Character('../data/assets/images/main(1).png', (100, 100))
        # man = Character('../data/assets/images/boy(1).png', (100, 100))
        main = Character('../data/assets/images/police-officer.png', (100, 100))
        man = Character('../data/assets/images/woman(1).png', (100, 100))

        main.set_position((50, y_doc + self.vertical_position))
        SpeechBubbleDoc.update_position(main.position)
        main.draw(self.screen)
        SpeechBubbleDoc.draw(self.screen)

        man.set_position((900, y_man + self.vertical_position))
        SpeechBubbleMan.update_position(man.position)
        man.draw(self.screen)
        SpeechBubbleMan.draw(self.screen)

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 24)
        heading_font = pygame.font.Font('freesansbold.ttf', 26)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1100, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1100, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def dialogue_run(self):
        self.screen.fill(self.bg_color)

        font = pygame.font.Font('freesansbold.ttf', 24)
        speech_bubble_0 = SpeechBubble(
            "Good afternoon, miss. I'm here today to talk to you about an important topic: sexual harassment awareness.",
            font)
        speech_bubble_man_0 = SpeechBubble_man(
            "Hi officer. Sure, I'm all ears. What do I need to know?",
            font)
        speech_bubble_1 = SpeechBubble(
            "Firstly, it's crucial to understand what constitutes sexual harassment. It can range from inappropriate comments or gestures to unwanted physical contact.",
            font)
        speech_bubble_man_1 = SpeechBubble_man(
            "That sounds serious. I guess it's important to know how to recognize it.",
            font)
        speech_bubble_2 = SpeechBubble(
            "Exactly. Awareness is key. If you ever feel uncomfortable or threatened by someone's words or actions, it's important to speak up and seek help.",
            font)
        speech_bubble_man_2 = SpeechBubble_man(
            "What if it happens in a public place? Like, what if someone harasses me on the street?",
            font)
        speech_bubble_3 = SpeechBubble(
            "In public spaces, you can seek assistance from bystanders or approach law enforcement officers like myself. It's essential not to feel ashamed or afraid to report it.",
            font)
        speech_bubble_man_3 = SpeechBubble_man(
            "That's reassuring to know. But what if it's someone I know, like a friend or a colleague?",
            font)
        speech_bubble_4 = SpeechBubble(
            "Even if it's someone familiar to you, harassment is never acceptable. You have the right to set boundaries and say no. If the behavior persists, don't hesitate to report it to authorities or your workplace's HR department.",
            font)
        speech_bubble_man_4 = SpeechBubble_man(
            "Okay, I understand. What about online harassment? I've heard it's becoming more common.",
            font)
        speech_bubble_5 = SpeechBubble(
            "Online harassment, or cyberbullying, is indeed prevalent. Remember to block and report individuals who engage in such behavior. Keep records of any threatening or harassing messages as evidence if needed.",
            font)
        speech_bubble_man_5 = SpeechBubble_man(
            "Got it. It's important to stay vigilant both online and offline. Thanks for the information, officer.",
            font)

        self.set_y_pos(speech_bubble_0, speech_bubble_man_0, 100, 300)
        self.set_y_pos(speech_bubble_1, speech_bubble_man_1, 470, 720)
        self.set_y_pos(speech_bubble_2, speech_bubble_man_2, 900, 1150)
        self.set_y_pos(speech_bubble_3, speech_bubble_man_3, 1350, 1560)
        self.set_y_pos(speech_bubble_4, speech_bubble_man_4, 1700, 1960)
        self.set_y_pos(speech_bubble_5, speech_bubble_man_5, 2130, 2350)

        heading_font = pygame.font.Font('freesansbold.ttf', 30)

        heading_box = rectangle_box_main("What is Sexual Harassment?", heading_font)
        heading_pos = (1100, 100 + self.vertical_position)
        heading_box.update_position(heading_pos)
        heading_box.draw(self.screen)

        word_0 = "1. Definition:  "
        text_0 = "Sexual harassment refers to unwelcome or unwanted behavior of a sexual nature that affects an individual's work or creates a hostile or offensive environment. It can include verbal, physical, or visual conduct."

        word_1 = "2.  Forms of Sexual Harassment:"
        text_1 = " It can manifest in various forms such as:\n\nVerbal harassment: Comments, jokes, or conversations of a sexual nature.\nNon-verbal harassment: Lewd gestures, staring, or displaying sexually suggestive images.\nPhysical harassment: Unwanted touching, groping, or assault."

        word_2 = "3.  Power Dynamics: "
        text_2 = "Sexual harassment often involves a power dynamic, where the harasser holds authority or influence over the victim, such as in workplace settings, educational institutions, or within social circles."

        word_3 = "4.  Impact on Victims: "
        text_3 = "Sexual harassment can have severe emotional, psychological, and professional consequences for victims. It can lead to anxiety, depression, decreased self-esteem, and hinder career advancement."

        word_4 = "5.  Legal Protections: "
        text_4 = "Many countries have laws and regulations in place to protect individuals from sexual harassment in the workplace, educational institutions, and other settings. Victims have the right to report harassment and seek legal recourse."

        word_5 = "6.  Importance of Reporting: "
        text_5 = "It's crucial for victims to report instances of sexual harassment to appropriate authorities or HR departments. Reporting not only helps the victim seek justice but also prevents future incidents and fosters a safer environment for everyone."

        word_6 = "7.  Prevention and Awareness: "
        text_6 = "Educating individuals about what constitutes sexual harassment and promoting a culture of respect and equality are essential for prevention. Training programs, workshops, and awareness campaigns can contribute to creating safer spaces."

        word_7 = "8.  Support for Victims: "
        text_7 = "Victims of sexual harassment should be provided with support services, including access to counseling, legal assistance, and resources for reporting and addressing the harassment."

        word_8 = "9.  Zero Tolerance Policy: "
        text_8 = "Organizations and institutions should adopt a zero-tolerance policy towards sexual harassment. Clear guidelines, procedures for reporting, and disciplinary actions against perpetrators should be established and enforced."

        word_9 = "10.  Cultural Change: "
        text_9 = "Ultimately, addressing sexual harassment requires a societal shift in attitudes and behaviors. It involves challenging harmful gender norms, promoting consent and respect, and advocating for gender equality in all aspects of life."

        self.notebox_pos(word_0, text_0, 250)
        self.notebox_pos(word_1, text_1, 570)
        self.notebox_pos(word_2, text_2, 930)
        self.notebox_pos(word_3, text_3, 1270)
        self.notebox_pos(word_4, text_4, 1610)
        self.notebox_pos(word_5, text_5, 1950)
        self.notebox_pos(word_6, text_6, 2290)
        self.notebox_pos(word_7, text_7, 2630)
        self.notebox_pos(word_8, text_8, 2980)
        self.notebox_pos(word_9, text_9, 3330)

        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 890, 50), (self.width - 890, self.height - 50), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 885, 50), (self.width - 885, self.height - 50), 3)


class Natural_disaster:
    def __init__(self):
        self.vertical_position = 0
        self.move_speed = 100
        self.screen = pygame.display.set_mode((1920, 1080))
        self.width, self.height = self.screen.get_size()
        self.bg_color = (230, 230, 230)

    def set_y_pos(self, SpeechBubbleDoc, SpeechBubbleMan, y_doc, y_man):
        # main = Character('../data/assets/images/main(1).png', (100, 100))
        # man = Character('../data/assets/images/boy(1).png', (100, 100))
        main = Character('../data/assets/images/teacher.png', (100, 100))
        man = Character('../data/assets/images/boy(1).png', (100, 100))

        main.set_position((50, y_doc + self.vertical_position))
        SpeechBubbleDoc.update_position(main.position)
        main.draw(self.screen)
        SpeechBubbleDoc.draw(self.screen)

        man.set_position((900, y_man + self.vertical_position))
        SpeechBubbleMan.update_position(man.position)
        man.draw(self.screen)
        SpeechBubbleMan.draw(self.screen)

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 24)
        heading_font = pygame.font.Font('freesansbold.ttf', 26)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1100, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1100, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def dialogue_run(self):
        self.screen.fill(self.bg_color)

        font = pygame.font.Font('freesansbold.ttf', 24)
        speech_bubble_0 = SpeechBubble(
            "Hi there! I'm here to talk to you about natural disasters and how we can be prepared for them.",
            font)
        speech_bubble_man_0 = SpeechBubble_man(
            "Oh, sure. I've heard a bit about them, but I'm not really sure what to do if one happens.",
            font)
        speech_bubble_1 = SpeechBubble(
            "That's okay! It's important to know how to stay safe. Did you know that different regions are prone to different types of natural disasters?",
            font)
        speech_bubble_man_1 = SpeechBubble_man(
            "I didn't know that. What kinds of natural disasters should I be aware of?",
            font)
        speech_bubble_2 = SpeechBubble(
            "Well, depending on where you live, you might need to prepare for earthquakes, hurricanes, tornadoes, floods, wildfires, or even tsunamis.",
            font)
        speech_bubble_man_2 = SpeechBubble_man(
            "Wow, that's a lot. How do I know which ones are relevant to me?",
            font)
        speech_bubble_3 = SpeechBubble(
            "You can check with local authorities or emergency management agencies to find out which natural disasters are common in your area. They often provide resources and information on how to prepare.",
            font)
        speech_bubble_man_3 = SpeechBubble_man(
            "Okay, that makes sense. What should I do to prepare for a natural disaster?",
            font)
        speech_bubble_4 = SpeechBubble(
            "First, you should create an emergency kit with essential items like water, non-perishable food, a flashlight, batteries, a first aid kit, and any necessary medications. You should also have a family emergency plan in place, including evacuation routes and meeting points.",
            font)
        speech_bubble_man_4 = SpeechBubble_man(
            "That sounds like a good idea. How often should I update my emergency kit?",
            font)
        speech_bubble_5 = SpeechBubble(
            "It's a good idea to check your emergency kit at least once a year to make sure everything is still in good condition and to replace any expired items. Additionally, you should review and practice your family emergency plan regularly.",
            font)
        speech_bubble_man_5 = SpeechBubble_man(
            "Got it. Thanks for the information! I'll make sure to start preparing for natural disasters now.",
            font)

        self.set_y_pos(speech_bubble_0, speech_bubble_man_0, 100, 300)
        self.set_y_pos(speech_bubble_1, speech_bubble_man_1, 470, 720)
        self.set_y_pos(speech_bubble_2, speech_bubble_man_2, 900, 1150)
        self.set_y_pos(speech_bubble_3, speech_bubble_man_3, 1350, 1560)
        self.set_y_pos(speech_bubble_4, speech_bubble_man_4, 1700, 1960)
        self.set_y_pos(speech_bubble_5, speech_bubble_man_5, 2130, 2400)

        heading_font = pygame.font.Font('freesansbold.ttf', 30)

        heading_box = rectangle_box_main("What to do during a disaster", heading_font)
        heading_pos = (1100, 100 + self.vertical_position)
        heading_box.update_position(heading_pos)
        heading_box.draw(self.screen)

        word_0 = "1. Stay Informed:"
        text_0 = "Keep yourself updated with reliable information from local authorities, weather services, or emergency management agencies."

        word_1 = "2. Evacuation Routes:"
        text_1 = "Know the evacuation routes in your area and have a plan in place in case you need to evacuate quickly."

        word_2 = "3. Emergency Kit:"
        text_2 = "Prepare an emergency kit with essential items such as water, non-perishable food, flashlight, batteries, first aid supplies, medications, and important documents."

        word_3 = "4. Family Communication Plan:"
        text_3 = "Establish a communication plan with your family or household members to stay in touch during emergencies, including a designated meeting point."

        word_4 = "5. Shelter:"
        text_4 = "Identify safe places to take shelter in your home or community, such as basements, storm shelters, or designated evacuation centers."

        word_5 = "6. Follow Instructions:"
        text_5 = "Follow instructions from local authorities, including evacuation orders or shelter-in-place directives."

        word_6 = "7. Utility Safety:"
        text_6 = "Be aware of utility safety procedures, such as turning off gas, electricity, and water mains if instructed to do so or if you suspect damage."

        word_7 = "8. Help Others:"
        text_7 = "Check on neighbors, especially the elderly, disabled, or those who may need assistance during emergencies."

        word_8 = "9. Stay Calm:"
        text_8 = "Remain calm and reassure others, especially children, during stressful situations. Panic can exacerbate the impact of a disaster."

        word_9 = "10. Aftermath:"
        text_9 = "Be cautious when returning home after a disaster, as there may be hazards such as debris, downed power lines, or contaminated water. Follow safety guidelines provided by authorities."

        self.notebox_pos(word_0, text_0, 250)
        self.notebox_pos(word_1, text_1, 570)
        self.notebox_pos(word_2, text_2, 930)
        self.notebox_pos(word_3, text_3, 1270)
        self.notebox_pos(word_4, text_4, 1610)
        self.notebox_pos(word_5, text_5, 1950)
        self.notebox_pos(word_6, text_6, 2290)
        self.notebox_pos(word_7, text_7, 2630)
        self.notebox_pos(word_8, text_8, 2980)
        self.notebox_pos(word_9, text_9, 3330)

        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 890, 50), (self.width - 890, self.height - 50), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 885, 50), (self.width - 885, self.height - 50), 3)


class Legal_rights:
    def __init__(self):
        self.vertical_position = 0
        self.move_speed = 100
        self.screen = pygame.display.set_mode((1920, 1080))
        self.width, self.height = self.screen.get_size()
        self.bg_color = (230, 230, 230)

    def set_y_pos(self, SpeechBubbleDoc, SpeechBubbleMan, y_doc, y_man):
        # main = Character('../data/assets/images/main(1).png', (100, 100))
        # man = Character('../data/assets/images/boy(1).png', (100, 100))
        main = Character('../data/assets/images/lawyer.png', (100, 100))
        man = Character('../data/assets/images/boy(1).png', (100, 100))

        main.set_position((50, y_doc + self.vertical_position))
        SpeechBubbleDoc.update_position(main.position)
        main.draw(self.screen)
        SpeechBubbleDoc.draw(self.screen)

        man.set_position((900, y_man + self.vertical_position))
        SpeechBubbleMan.update_position(man.position)
        man.draw(self.screen)
        SpeechBubbleMan.draw(self.screen)

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 24)
        heading_font = pygame.font.Font('freesansbold.ttf', 26)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1100, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1100, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def dialogue_run(self):
        self.screen.fill(self.bg_color)

        font = pygame.font.Font('freesansbold.ttf', 24)

        speech_bubble_0 = SpeechBubble(
            "Good afternoon. Thank you for meeting with me today. Let's start by discussing your legal rights. Have you ever had any legal issues before?",
            font)
        speech_bubble_man_0 = SpeechBubble_man(
            "No, I haven't. I'm not really sure what my rights are in certain situations.",
            font)
        speech_bubble_1 = SpeechBubble(
            "That's completely understandable. Everyone should be aware of their legal rights, regardless of whether they've encountered legal issues before. One of your fundamental rights is the right to remain silent. This means you don't have to answer any questions from law enforcement without an attorney present.",
            font)
        speech_bubble_man_1 = SpeechBubble_man(
            "So, I don't have to say anything if I'm being questioned by the police?",
            font)
        speech_bubble_2 = SpeechBubble(
            "Exactly. You have the right to refrain from speaking until you have consulted with a lawyer. Additionally, you have the right to legal representation. If you cannot afford an attorney, one will be provided for you.",
            font)
        speech_bubble_man_2 = SpeechBubble_man(
            "That's reassuring to know. What other rights do I have?",
            font)
        speech_bubble_3 = SpeechBubble(
            "You also have the right to be treated fairly and equally under the law. This means you cannot be discriminated against based on factors such as race, gender, religion, or disability.",
            font)
        speech_bubble_man_3 = SpeechBubble_man(
            "What if I'm arrested? What are my rights then?",
            font)
        speech_bubble_4 = SpeechBubble(
            "If you're arrested, you have the right to be informed of the charges against you. You also have the right to a fair and speedy trial by jury, where you can confront witnesses and present evidence in your defense.",
            font)
        speech_bubble_man_4 = SpeechBubble_man(
            "That sounds like a lot to remember. Is there anything else I should know?",
            font)
        speech_bubble_5 = SpeechBubble(
            "Yes, you have the right to due process, which means you cannot be deprived of life, liberty, or property without fair legal procedures. And finally, you have the right to appeal a decision if you believe it was made unfairly or unlawfully.",
            font)
        speech_bubble_man_5 = SpeechBubble_man(
            "Thank you for explaining all of this to me. I feel much more informed about my legal rights now.",
            font)
        speech_bubble_6 = SpeechBubble(
            "You're welcome. It's essential to understand your rights so you can protect yourself if you ever find yourself in a legal situation. If you have any more questions or need further assistance, don't hesitate to reach out.",
            font)
        speech_bubble_man_6 = SpeechBubble_man("Thank you", font)

        self.set_y_pos(speech_bubble_0, speech_bubble_man_0, 100, 300)
        self.set_y_pos(speech_bubble_1, speech_bubble_man_1, 470, 770)
        self.set_y_pos(speech_bubble_2, speech_bubble_man_2, 900, 1150)
        self.set_y_pos(speech_bubble_3, speech_bubble_man_3, 1350, 1560)
        self.set_y_pos(speech_bubble_4, speech_bubble_man_4, 1700, 1960)
        self.set_y_pos(speech_bubble_5, speech_bubble_man_5, 2130, 2400)
        self.set_y_pos(speech_bubble_6, speech_bubble_man_6, 2630, 2900)

        heading_font = pygame.font.Font('freesansbold.ttf', 30)

        heading_box = rectangle_box_main("About you legal rights", heading_font)
        heading_pos = (1100, 100 + self.vertical_position)
        heading_box.update_position(heading_pos)
        heading_box.draw(self.screen)

        word_0 = "1. Right to Legal Representation:"
        text_0 = "Individuals have the right to legal representation, meaning they can hire an attorney to represent them in legal proceedings. If they cannot afford an attorney, one will be provided for them."

        word_1 = "2. Right to Remain Silent:"
        text_1 = "People have the right to remain silent and not incriminate themselves. This right protects individuals from self-incrimination and ensures a fair legal process."

        word_2 = "3. Right to Due Process:"
        text_2 = "The right to due process guarantees that individuals cannot be deprived of life, liberty, or property without fair legal procedures. This includes the right to a fair trial and the opportunity to present evidence and witnesses in one's defense."

        word_3 = "4. Right to a Speedy Trial:"
        text_3 = "Defendants have the right to a speedy trial, meaning they cannot be held in pretrial detention for an unreasonable amount of time. This right helps prevent prolonged incarceration without resolution."

        word_4 = "5. Right to Equality Before the Law:"
        text_4 = "Everyone is entitled to equal treatment under the law, regardless of race, gender, religion, or other characteristics. Discrimination in any form is prohibited by law."

        word_5 = "6. Right to Privacy:"
        text_5 = "Individuals have the right to privacy, which protects them from unreasonable searches and seizures by law enforcement. This right is enshrined in various legal frameworks and constitutions around the world."

        word_6 = "7. Right to Appeal:"
        text_6 = "If individuals believe that a legal decision made against them is unfair or unlawful, they have the right to appeal the decision to a higher court. This allows for a review of the case and the possibility of overturning an unjust verdict."

        word_7 = "8. Right to Compensation for Wrongs:"
        text_7 = "Victims of crimes or injustices have the right to seek compensation for any harm or losses they have suffered. This may include financial compensation or other forms of restitution."

        word_8 = "9. Right to Freedom of Speech:"
        text_8 = "Individuals have the right to express their opinions and beliefs freely, without censorship or punishment from the government. This right is protected in many countries' constitutions and legal frameworks."

        word_9 = "10. Right to Education:"
        text_9 = "Children have the right to receive an education, and governments are obligated to provide accessible and quality education to all children. This right is recognized by international human rights treaties."

        self.notebox_pos(word_0, text_0, 250)
        self.notebox_pos(word_1, text_1, 570)
        self.notebox_pos(word_2, text_2, 930)
        self.notebox_pos(word_3, text_3, 1270)
        self.notebox_pos(word_4, text_4, 1610)
        self.notebox_pos(word_5, text_5, 1950)
        self.notebox_pos(word_6, text_6, 2290)
        self.notebox_pos(word_7, text_7, 2630)
        self.notebox_pos(word_8, text_8, 2980)
        self.notebox_pos(word_9, text_9, 3330)

        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 890, 50), (self.width - 890, self.height - 50), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 885, 50), (self.width - 885, self.height - 50), 3)


class Diet:
    def __init__(self):
        self.vertical_position = 0
        self.move_speed = 100
        self.screen = pygame.display.set_mode((1920, 1080))
        self.width, self.height = self.screen.get_size()
        self.bg_color = (230, 230, 230)

    def set_y_pos(self, SpeechBubbleDoc, SpeechBubbleMan, y_doc, y_man):
        # main = Character('../data/assets/images/main(1).png', (100, 100))
        # man = Character('../data/assets/images/boy(1).png', (100, 100))
        main = Character('../data/assets/images/man.png', (100, 100))
        man = Character('../data/assets/images/boy(1).png', (100, 100))

        main.set_position((50, y_doc + self.vertical_position))
        SpeechBubbleDoc.update_position(main.position)
        main.draw(self.screen)
        SpeechBubbleDoc.draw(self.screen)

        man.set_position((900, y_man + self.vertical_position))
        SpeechBubbleMan.update_position(man.position)
        man.draw(self.screen)
        SpeechBubbleMan.draw(self.screen)

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 24)
        heading_font = pygame.font.Font('freesansbold.ttf', 26)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1100, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1100, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def dialogue_run(self):
        self.screen.fill(self.bg_color)

        font = pygame.font.Font('freesansbold.ttf', 24)

        speech_bubble_0 = SpeechBubble(
            "Hello! It's great to meet you. So, let's talk about your diet. Can you tell me what your current eating habits are like?",
            font)
        speech_bubble_man_0 = SpeechBubble_man(
            "Hi! Sure, I typically have a lot of fast food and processed snacks throughout the day. I know it's not the healthiest, but it's convenient.",
            font)
        speech_bubble_1 = SpeechBubble(
            "I understand. Convenience is often a big factor in our food choices. However, we should aim for a balanced diet that includes plenty of fruits, vegetables, lean proteins, and whole grains.",
            font)
        speech_bubble_man_1 = SpeechBubble_man(
            "That sounds reasonable. But I'm not sure how to start. Do I need to cut out all the junk food completely?",
            font)
        speech_bubble_2 = SpeechBubble(
            "It's not about cutting out everything at once. We can start by gradually reducing your intake of processed foods and incorporating more nutritious options into your meals and snacks.",
            font)
        speech_bubble_man_2 = SpeechBubble_man(
            "Okay, that sounds manageable. What are some examples of nutritious snacks I could try?",
            font)
        speech_bubble_3 = SpeechBubble(
            "Good question! Instead of reaching for chips or candy, you could have things like sliced veggies with hummus, Greek yogurt with berries, or a handful of nuts. These snacks provide a good balance of nutrients and will keep you feeling satisfied.",
            font)
        speech_bubble_man_3 = SpeechBubble_man(
            "I like the sound of those options. What about meals? I often struggle with what to make for dinner.",
            font)
        speech_bubble_4 = SpeechBubble(
            "For meals, focus on including a variety of foods. Aim to fill half your plate with vegetables, a quarter with lean protein like chicken or fish, and a quarter with whole grains like quinoa or brown rice. And don't forget healthy fats like avocado or olive oil.",
            font)
        speech_bubble_man_4 = SpeechBubble_man(
            "That makes sense. I'll try to incorporate those guidelines into my meals. But what about portion sizes? I tend to eat large portions without realizing it.",
            font)
        speech_bubble_5 = SpeechBubble(
            "Portion control is important too. Pay attention to your hunger and fullness cues, and try using smaller plates to help control portion sizes. And remember, it's okay to leave food on your plate if you're full.",
            font)
        speech_bubble_man_5 = SpeechBubble_man(
            "Got it. I'll start paying more attention to my portion sizes. Thanks for all the advice!",
            font)
        speech_bubble_6 = SpeechBubble(
            "You're welcome! Remember, making small changes over time can lead to big improvements in your health. If you have any more questions or need support along the way, don't hesitate to reach out.",
            font)
        speech_bubble_man_6 = SpeechBubble_man("Thank you", font)

        self.set_y_pos(speech_bubble_0, speech_bubble_man_0, 100, 300)
        self.set_y_pos(speech_bubble_1, speech_bubble_man_1, 470, 700)
        self.set_y_pos(speech_bubble_2, speech_bubble_man_2, 900, 1150)
        self.set_y_pos(speech_bubble_3, speech_bubble_man_3, 1350, 1610)
        self.set_y_pos(speech_bubble_4, speech_bubble_man_4, 1830, 2100)
        self.set_y_pos(speech_bubble_5, speech_bubble_man_5, 2300, 2500)
        self.set_y_pos(speech_bubble_6, speech_bubble_man_6, 2630, 2900)

        heading_font = pygame.font.Font('freesansbold.ttf', 30)

        heading_box = rectangle_box_main("A proper healthy diet", heading_font)
        heading_pos = (1100, 100 + self.vertical_position)
        heading_box.update_position(heading_pos)
        heading_box.draw(self.screen)

        word_0 = "1. Balanced Macronutrients:"
        text_0 = "A healthy diet includes a balance of macronutrients such as carbohydrates, proteins, and fats. Each of these nutrients plays a vital role in supporting overall health and well-being."

        word_1 = "2. Fruits and Vegetables:"
        text_1 = "Incorporating a variety of fruits and vegetables into your diet provides essential vitamins, minerals, and antioxidants. Aim to include a colorful assortment to ensure you're getting a wide range of nutrients."

        word_2 = "3. Whole Grains:"
        text_2 = "Whole grains, such as brown rice, quinoa, oats, and whole wheat, are rich in fiber, which aids in digestion and helps maintain steady blood sugar levels. They also provide essential nutrients like B vitamins and minerals."

        word_3 = "4. Lean Proteins:"
        text_3 = "Choose lean sources of protein, such as poultry, fish, beans, lentils, tofu, and low-fat dairy products. Protein is crucial for building and repairing tissues, supporting immune function, and maintaining muscle mass."

        word_4 = "5. Healthy Fats:"
        text_4 = "Include sources of healthy fats in your diet, such as avocados, nuts, seeds, and olive oil. These fats are important for brain health, hormone production, and absorbing fat-soluble vitamins."

        word_5 = "6. Portion Control:"
        text_5 = "Pay attention to portion sizes to avoid overeating. Use visual cues, such as using smaller plates and measuring serving sizes, to help control portions and prevent consuming excess calories."

        word_6 = "7. Hydration:"
        text_6 = "Drink plenty of water throughout the day to stay hydrated. Water is essential for regulating body temperature, aiding digestion, and transporting nutrients and waste products in the body."

        word_7 = "8. Limit Processed Foods and Added Sugars:"
        text_7 = "Minimize the intake of processed foods, sugary beverages, and snacks high in added sugars, unhealthy fats, and sodium. These foods often lack nutritional value and can contribute to weight gain and various health issues."

        word_8 = "9. Mindful Eating:"
        text_8 = "Practice mindful eating by paying attention to hunger and fullness cues, eating slowly, and savoring each bite. This can help prevent overeating and promote a healthier relationship with food."

        word_9 = "10. Regular Physical Activity:"
        text_9 = "In addition to diet, regular physical activity is essential for overall health and well-being. Aim for a combination of cardiovascular exercise, strength training, and flexibility exercises to maintain a healthy weight and reduce the risk of chronic diseases."

        self.notebox_pos(word_0, text_0, 250)
        self.notebox_pos(word_1, text_1, 570)
        self.notebox_pos(word_2, text_2, 930)
        self.notebox_pos(word_3, text_3, 1270)
        self.notebox_pos(word_4, text_4, 1610)
        self.notebox_pos(word_5, text_5, 1950)
        self.notebox_pos(word_6, text_6, 2290)
        self.notebox_pos(word_7, text_7, 2630)
        self.notebox_pos(word_8, text_8, 2980)
        self.notebox_pos(word_9, text_9, 3330)

        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 890, 50), (self.width - 890, self.height - 50), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 885, 50), (self.width - 885, self.height - 50), 3)


class Pregnency:
    def __init__(self):
        self.vertical_position = 0
        self.move_speed = 100
        self.screen = pygame.display.set_mode((1920, 1080))
        self.width, self.height = self.screen.get_size()
        self.bg_color = (230, 230, 230)

    def set_y_pos(self, SpeechBubbleDoc, SpeechBubbleMan, y_doc, y_man):
        # main = Character('../data/assets/images/main(1).png', (100, 100))
        # man = Character('../data/assets/images/boy(1).png', (100, 100))
        main = Character('../data/assets/images/avatar.png', (100, 100))
        man = Character('../data/assets/images/woman(1).png', (100, 100))

        main.set_position((50, y_doc + self.vertical_position))
        SpeechBubbleDoc.update_position(main.position)
        main.draw(self.screen)
        SpeechBubbleDoc.draw(self.screen)

        man.set_position((900, y_man + self.vertical_position))
        SpeechBubbleMan.update_position(man.position)
        man.draw(self.screen)
        SpeechBubbleMan.draw(self.screen)

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 24)
        heading_font = pygame.font.Font('freesansbold.ttf', 26)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1100, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1100, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def dialogue_run(self):
        self.screen.fill(self.bg_color)

        font = pygame.font.Font('freesansbold.ttf', 24)

        speech_bubble_0 = SpeechBubble(
            "Good morning! How are you feeling today?",
            font)
        speech_bubble_man_0 = SpeechBubble_man(
            "I'm doing well, thank you. Excited and a bit nervous about the pregnancy.",
            font)
        speech_bubble_1 = SpeechBubble(
            "That's completely normal! Pregnancy can be both exciting and overwhelming. First off, let's talk about the importance of prenatal vitamins.",
            font)
        speech_bubble_man_1 = SpeechBubble_man(
            "Yes, I've been taking them regularly. Is there anything specific I should be looking for in my prenatal vitamins?",
            font)
        speech_bubble_2 = SpeechBubble(
            "It's great that you're taking them. Look for ones that contain folic acid, iron, calcium, and DHA. These nutrients are crucial for the development of your baby.",
            font)
        speech_bubble_man_2 = SpeechBubble_man(
            "Got it, I'll make sure to check the labels. What about diet? Are there any foods I should avoid?",
            font)
        speech_bubble_3 = SpeechBubble(
            "Maintaining a balanced diet is essential. Avoid raw or undercooked foods like sushi or unpasteurized dairy. Also, limit your caffeine intake and avoid alcohol completely.",
            font)
        speech_bubble_man_3 = SpeechBubble_man(
            "Okay, I'll be mindful of what I eat. How about exercise? Can I continue with my usual routine?",
            font)
        speech_bubble_4 = SpeechBubble(
            "Yes, staying active is important, but listen to your body. Aim for moderate exercises like walking, swimming, or prenatal yoga. Avoid high-impact activities and contact sports.",
            font)
        speech_bubble_man_4 = SpeechBubble_man(
            "That makes sense. I'll try to incorporate those exercises into my routine. What about prenatal appointments? How often should I see you?",
            font)
        speech_bubble_5 = SpeechBubble(
            "Typically, we'll schedule monthly appointments until you're about 28 weeks along, then we'll increase the frequency to every two weeks, and finally weekly as you approach your due date. These appointments are crucial for monitoring your health and the baby's development.",
            font)
        speech_bubble_man_5 = SpeechBubble_man(
            "Alright, I'll make sure to keep up with my appointments. Is there anything else I should be doing to ensure a healthy pregnancy?",
            font)
        speech_bubble_6 = SpeechBubble(
            "Plenty! Get plenty of rest, stay hydrated, manage stress, and avoid harmful substances like tobacco smoke. And don't hesitate to reach out if you have any concerns or questions along the way.",
            font)
        speech_bubble_man_6 = SpeechBubble_man(
            "Thank you, doctor. I feel much more prepared now. I'll make sure to follow your advice for a healthy pregnancy.",
            font)
        speech_bubble_7 = SpeechBubble(
            "You're welcome! Remember, we're here to support you every step of the way. Don't hesitate to reach out if you need anything at all.",
            font)
        speech_bubble_man_7 = SpeechBubble_man("Thank you", font)

        self.set_y_pos(speech_bubble_0, speech_bubble_man_0, 100, 300)
        self.set_y_pos(speech_bubble_1, speech_bubble_man_1, 470, 700)
        self.set_y_pos(speech_bubble_2, speech_bubble_man_2, 900, 1150)
        self.set_y_pos(speech_bubble_3, speech_bubble_man_3, 1350, 1610)
        self.set_y_pos(speech_bubble_4, speech_bubble_man_4, 1830, 2100)
        self.set_y_pos(speech_bubble_5, speech_bubble_man_5, 2300, 2600)
        self.set_y_pos(speech_bubble_6, speech_bubble_man_6, 2800, 3000)
        self.set_y_pos(speech_bubble_7, speech_bubble_man_7, 3180, 3370)

        heading_font = pygame.font.Font('freesansbold.ttf', 30)

        heading_box = rectangle_box_main("Tips during pregnancy", heading_font)
        heading_pos = (1100, 100 + self.vertical_position)
        heading_box.update_position(heading_pos)
        heading_box.draw(self.screen)

        word_0 = "1. Attend Prenatal Care Appointments:"
        text_0 = "Regular check-ups with your healthcare provider are essential for monitoring your health and the baby's development."

        word_1 = "2. Eat a Balanced Diet: "
        text_1 = "Consume a variety of nutrient-rich foods including fruits, vegetables, whole grains, lean proteins, and dairy products to support both you and your baby's nutritional needs."

        word_2 = "3. Stay Hydrated: "
        text_2 = "Drink plenty of water throughout the day to help with digestion, circulation, and to prevent dehydration."

        word_3 = "4. Take Prenatal Vitamins: "
        text_3 = "Ensure you're getting essential nutrients like folic acid, iron, calcium, and DHA by taking prenatal vitamins as recommended by your doctor."

        word_4 = "5. Get Regular Exercise: "
        text_4 = "Engage in safe and moderate physical activity like walking, swimming, or prenatal yoga to promote circulation, reduce stress, and prepare your body for labor."

        word_5 = "6. Get Adequate Rest: "
        text_5 = "Aim for 7-9 hours of quality sleep per night and listen to your body's signals for rest during the day."

        word_6 = "7. Avoid Harmful Substances: "
        text_6 = "Stay away from alcohol, tobacco, and recreational drugs as they can harm your baby's development."

        word_7 = "8. Practice Good Hygiene: "
        text_7 = "Wash your hands frequently, cook meats thoroughly, and avoid exposure to harmful chemicals to prevent infections and toxins from affecting your baby."

        word_8 = "9. Manage Stress: "
        text_8 = "Practice relaxation techniques such as deep breathing, meditation, or prenatal massage to reduce stress levels and promote overall well-being."

        word_9 = "10. Educate Yourself: "
        text_9 = "Take childbirth and parenting classes to learn about labor, breastfeeding, and newborn care. Knowledge can help alleviate anxiety and prepare you for the journey ahead."

        self.notebox_pos(word_0, text_0, 250)
        self.notebox_pos(word_1, text_1, 570)
        self.notebox_pos(word_2, text_2, 930)
        self.notebox_pos(word_3, text_3, 1270)
        self.notebox_pos(word_4, text_4, 1610)
        self.notebox_pos(word_5, text_5, 1950)
        self.notebox_pos(word_6, text_6, 2290)
        self.notebox_pos(word_7, text_7, 2630)
        self.notebox_pos(word_8, text_8, 2980)
        self.notebox_pos(word_9, text_9, 3330)

        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 890, 50), (self.width - 890, self.height - 50), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 885, 50), (self.width - 885, self.height - 50), 3)


class Election:
    def __init__(self):
        self.vertical_position = 0
        self.move_speed = 100
        self.screen = pygame.display.set_mode((1920, 1080))
        self.width, self.height = self.screen.get_size()
        self.bg_color = (230, 230, 230)

    def set_y_pos(self, SpeechBubbleDoc, SpeechBubbleMan, y_doc, y_man):
        # main = Character('../data/assets/images/main(1).png', (100, 100))
        # man = Character('../data/assets/images/boy(1).png', (100, 100))
        main = Character('../data/assets/images/campaign.png', (100, 100))
        man = Character('../data/assets/images/boy(1).png', (100, 100))

        main.set_position((50, y_doc + self.vertical_position))
        SpeechBubbleDoc.update_position(main.position)
        main.draw(self.screen)
        SpeechBubbleDoc.draw(self.screen)

        man.set_position((900, y_man + self.vertical_position))
        SpeechBubbleMan.update_position(man.position)
        man.draw(self.screen)
        SpeechBubbleMan.draw(self.screen)

    def notebox_pos(self, word, text, y_pos):
        my_font = pygame.font.Font('freesansbold.ttf', 24)
        heading_font = pygame.font.Font('freesansbold.ttf', 26)
        my_rectangle_box_word = rectangle_box_main(word, heading_font)
        my_rectangle_box_text = rectangle_box(text, my_font)

        # Set the position of the rectangle_box
        new_position_word = (1100, y_pos + self.vertical_position)  # Set your desired position here
        my_rectangle_box_word.update_position(new_position_word)
        new_position_text = (1100, y_pos + 100 + self.vertical_position)
        my_rectangle_box_text.update_position(new_position_text)

        # Inside your game loop, you can draw the rectangle_box
        my_rectangle_box_word.draw(self.screen)
        my_rectangle_box_text.draw(self.screen)

    def dialogue_run(self):
        self.screen.fill(self.bg_color)

        font = pygame.font.Font('freesansbold.ttf', 24)

        speech_bubble_0 = SpeechBubble(
            "Good morning! How can I assist you today?",
            font)
        speech_bubble_man_0 = SpeechBubble_man(
            "I'm a bit curious about the upcoming elections. Could you provide me with some information?",
            font)
        speech_bubble_1 = SpeechBubble(
            "Of course! We're here to help. Firstly, let me explain the basics. Elections are a fundamental aspect of our democratic system. They allow citizens like yourself to choose representatives who will govern and make decisions on your behalf.",
            font)
        speech_bubble_man_1 = SpeechBubble_man(
            "That makes sense. How often do these elections take place?",
            font)
        speech_bubble_2 = SpeechBubble(
            "Well, it depends on the level of government. Generally, we have local, state, and national elections. Local elections may happen yearly or every couple of years, while state and national elections usually occur less frequently, often every two to four years.",
            font)
        speech_bubble_man_2 = SpeechBubble_man(
            "Ah, got it. How does the voting process work exactly?",
            font)
        speech_bubble_3 = SpeechBubble(
            "Voting typically takes place at designated polling stations. On the day of the election, eligible voters like yourself visit these stations and cast their ballots. You'll be provided with a ballot paper or directed to an electronic voting machine to make your choices.",
            font)
        speech_bubble_man_3 = SpeechBubble_man(
            "And who can participate in these elections?",
            font)
        speech_bubble_4 = SpeechBubble(
            "Any citizen who meets the eligibility criteria set by law can participate. This often includes factors such as age, residency, and citizenship status. It's crucial to ensure you're registered to vote beforehand.",
            font)
        speech_bubble_man_4 = SpeechBubble_man(
            "What if I can't make it to the polling station on election day?",
            font)
        speech_bubble_5 = SpeechBubble(
            "Not to worry. Many jurisdictions offer options for early or absentee voting. This allows individuals to vote ahead of time or by mail if they're unable to make it on election day. Just make sure to check the specific procedures in your area.",
            font)
        speech_bubble_man_5 = SpeechBubble_man(
            "That's convenient. How are the results determined?",
            font)
        speech_bubble_6 = SpeechBubble(
            "Once all the votes are cast, they're counted either manually or electronically, depending on the system in place. The candidate or party with the majority of votes wins the election and assumes office.",
            font)
        speech_bubble_man_6 = SpeechBubble_man(
            "What measures are in place to ensure the integrity of the elections?",
            font)
        speech_bubble_7 = SpeechBubble(
            "Electoral integrity is paramount. There are strict protocols in place to prevent fraud and ensure fairness, including voter registration systems, secure ballot handling procedures, and observation by independent monitors.",
            font)
        speech_bubble_man_7 = SpeechBubble_man(
            "Thank you for the information. I feel much more informed now.",
            font)

        self.set_y_pos(speech_bubble_0, speech_bubble_man_0, 100, 230)
        self.set_y_pos(speech_bubble_1, speech_bubble_man_1, 430, 700)
        self.set_y_pos(speech_bubble_2, speech_bubble_man_2, 900, 1160)
        self.set_y_pos(speech_bubble_3, speech_bubble_man_3, 1350, 1630)
        self.set_y_pos(speech_bubble_4, speech_bubble_man_4, 1830, 2100)
        self.set_y_pos(speech_bubble_5, speech_bubble_man_5, 2300, 2600)
        self.set_y_pos(speech_bubble_6, speech_bubble_man_6, 2800, 3010)
        self.set_y_pos(speech_bubble_7, speech_bubble_man_7, 3180, 3400)

        heading_font = pygame.font.Font('freesansbold.ttf', 30)

        heading_box = rectangle_box_main("Important points related to elections", heading_font)
        heading_pos = (1100, 100 + self.vertical_position)
        heading_box.update_position(heading_pos)
        heading_box.draw(self.screen)

        word_0 = "1. Democratic Foundation:"
        text_0 = "Elections are a cornerstone of democracy, allowing citizens to choose their representatives and participate in decision-making processes."

        word_1 = "2. Types of Elections:"
        text_1 = "Elections can be at various levels of government, including local, state/provincial, and national/federal levels. Each level may have different voting procedures and timelines."

        word_2 = "3. Voter Eligibility:"
        text_2 = "To participate in elections, individuals typically need to meet certain eligibility criteria, such as age, citizenship, and residency requirements."

        word_3 = "4. Registration:"
        text_3 = "In many countries, voters need to register before they can cast their ballots. Registration processes vary by jurisdiction and may involve providing proof of identity and address."

        word_4 = "5. Voting Methods:"
        text_4 = "There are different voting methods used in elections, including in-person voting at polling stations, mail-in or absentee voting, and electronic voting. The method used often depends on the country's laws and infrastructure."

        word_5 = "6. Campaigning:"
        text_5 = "Political parties and candidates engage in campaigning to persuade voters to support them. Campaigning activities include rallies, debates, advertising, and outreach efforts."

        word_6 = "7. Ballot Design:"
        text_6 = "The design of the ballot paper or electronic voting interface can impact the voting process and outcomes. Clear and intuitive ballot designs help prevent confusion and errors."

        word_7 = "8. Vote Counting:"
        text_7 = "After polls close, votes are counted to determine the winners. Depending on the election system, this process may involve manual counting, electronic tabulation, or a combination of both."

        word_8 = "9. Electoral Integrity:"
        text_8 = "Maintaining the integrity of elections is crucial for ensuring fairness and legitimacy. Measures such as voter registration systems, ballot security, and independent oversight help safeguard against fraud and manipulation."

        word_9 = "10. Civic Responsibility:"
        text_9 = "Voting is not only a right but also a civic duty. Participating in elections allows citizens to have a voice in shaping their communities and societies."

        self.notebox_pos(word_0, text_0, 250)
        self.notebox_pos(word_1, text_1, 570)
        self.notebox_pos(word_2, text_2, 930)
        self.notebox_pos(word_3, text_3, 1270)
        self.notebox_pos(word_4, text_4, 1610)
        self.notebox_pos(word_5, text_5, 1950)
        self.notebox_pos(word_6, text_6, 2290)
        self.notebox_pos(word_7, text_7, 2630)
        self.notebox_pos(word_8, text_8, 2980)
        self.notebox_pos(word_9, text_9, 3330)

        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 890, 50), (self.width - 890, self.height - 50), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width - 885, 50), (self.width - 885, self.height - 50), 3)