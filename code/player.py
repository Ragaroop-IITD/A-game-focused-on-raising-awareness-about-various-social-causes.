import pygame,sys
from settings import *
from support import *
from debug import debug
from snake_game_main import Snake_Game
from Intro import IntroMain
from Start import InstrMain


class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("../data/assets/images/player1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-26)

        # graphics setup
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        #movement
        self.direction=pygame.math.Vector2()
        self.speed=5
        self.entering=False
        self.enter_cooldown=400
        self.enter_time=None

        #coordinates
        self.rel_x = self.hitbox.centerx // (tile_size // 2)
        self.rel_y = self.hitbox.centery // (tile_size // 2)


        self.obstacle_sprites=obstacle_sprites

    def import_player_assets(self):
        character_path = '../data/assets/player/'
        self.animations = {'up': [],'down': [],'left': [],'right': [],
            'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
            'right_enter':[],'left_enter':[],'up_enter':[],'down_enter':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        if not self.entering:
            keys=pygame.key.get_pressed()

            #movement input
            if keys[pygame.K_LEFT]:
                self.direction.x=-1
                self.status='left'
            elif keys[pygame.K_RIGHT]:
                self.direction.x=1
                self.status='right'
            else:
                self.direction.x=0
            
            if keys[pygame.K_UP]:
                self.direction.y=-1
                self.status='up'
            elif keys[pygame.K_DOWN]:
                self.direction.y=1
                self.status='down'
            else:
                self.direction.y=0

            if keys[pygame.K_h]:
                InstrMain()

            #entry input
            if keys[pygame.K_SPACE] and not self.entering:
                self.entering=True
                self.enter_time=pygame.time.get_ticks()
                print('entering...')

                if self.rel_x >=172 and self.rel_x<=176 and self.rel_y >=120 and self.rel_y<=121:
                    print('entered mental health care center')
                    IntroMain(0)
                elif self.rel_x >=93 and self.rel_x<=101 and self.rel_y >=78 and self.rel_y<=78:
                    print('Entered weather forecast centre')
                    IntroMain(1)
                elif self.rel_x >=145 and self.rel_x<=147 and self.rel_y >=136 and self.rel_y<=138:
                    print('Entered Nursery home')
                    IntroMain(2)
                elif self.rel_x >=105 and self.rel_x<=107 and self.rel_y >=98 and self.rel_y<=98:
                    print('Entered political activist office')
                    IntroMain(3)
                elif self.rel_x >=115 and self.rel_x<=117 and self.rel_y >=158 and self.rel_y<=159:
                    print('Entered lotus temple')
                    IntroMain(4)
                elif self.rel_x >=117 and self.rel_x<=119 and self.rel_y >=72 and self.rel_y<=72:
                    print('Entered police station')
                    IntroMain(5)
                elif self.rel_x >=147 and self.rel_x<=151 and self.rel_y >=96 and self.rel_y<=96:
                    print('Entered library')
                elif self.rel_x >=147 and self.rel_x<=151 and self.rel_y >=72 and self.rel_y<=73:
                    print('Entered lawyer office')
                    IntroMain(7)
                elif self.rel_x >=101 and self.rel_x<=105 and self.rel_y >=118 and self.rel_y<=119:
                    print('Entered food court')
                    IntroMain(8)
                elif self.rel_x >=173 and self.rel_x<=175 and self.rel_y >=144 and self.rel_y<=145:
                    snake_game=Snake_Game()
                    snake_game.run()
                elif self.rel_x >=173 and self.rel_x<=175 and self.rel_y >=96 and self.rel_y<=97:
                    print('Entered hospital')
                    IntroMain(9)
                elif self.rel_x >=153 and self.rel_x<=157 and self.rel_y >=162 and self.rel_y<=163:
                    print('Entered election office')
                    IntroMain(10)
                else:
                    pass


    def get_status(self):
        # idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'enter' in self.status:
                self.status = self.status + '_idle'
        
        if self.entering:
            self.direction.x = 0
            self.direction.y = 0
            if not 'enter' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_enter')
                else:
                    self.status = self.status + '_enter'
        else:
            if 'enter' in self.status:
                self.status = self.status.replace('_enter','')


    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    
    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def cooldowns(self):
        current_time=pygame.time.get_ticks()
        if self.entering:
            if current_time-self.enter_time >= self.enter_cooldown:
                self.entering=False

    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update_coordinates(self):
        self.rel_x = self.hitbox.centerx // (tile_size // 2)
        self.rel_y = self.hitbox.centery // (tile_size // 2)

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
        self.update_coordinates()
        debug(f'x:{self.rel_x-124} y:{self.rel_y-112}') #124,112
        debug("Press [H] for help",10,1700)
        
