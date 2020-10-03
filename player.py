import pygame

import config as c
from pygame import *
from bullets import Bullet

class Player:
    def __init__(self, x, y, w, h, char):
        self.player = pygame.Rect(x, y, w, h)
        self.char = char
        #self.color = c.player_color

        self.startX = x # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.xvel = 0 # скорость горизонтального перемещения
        self.yvel = 0 # скорость вертикального перемещения

        self.player_speed = c.player_speed
        self.player_boost_speed = c.player_boost_speed

        self.player_jump_power = c.player_jump_power
        self.player_boost_jump_power = c.player_boost_jump_power
        self.player_gravity = c.player_gravity


        self.onGround = False # На земле ли я?

        self.turn_left = False
        self.left = False
        self.right = False
        self.jump = False
        self.shoot = False
        self.boost = False
        self.frame = 0

        self.stock_of_bullets = 100
        self.counts_of_bullets = 0
        '''self.character = Surface((WIDTH,HEIGHT))
        self.character.fill(Color(COLOR))
        self.character.set_colorkey(Color(COLOR)) # делаем фон прозрачным'''

        self.animation_stand = [pygame.image.load("data/players/%s/stand_1.png" % self.char),
                                pygame.image.load("data/players/%s/stand_2.png" % self.char)]

        self.animation_right = [pygame.image.load('data/players/%s/right_1.png' % self.char),
                                pygame.image.load('data/players/%s/right_2.png' % self.char),
                                pygame.image.load('data/players/%s/right_3.png' % self.char),
                                pygame.image.load('data/players/%s/right_4.png' % self.char),
                                pygame.image.load('data/players/%s/right_5.png' % self.char),
                                pygame.image.load('data/players/%s/right_6.png' % self.char),
                                pygame.image.load('data/players/%s/right_7.png' % self.char),
                                pygame.image.load('data/players/%s/right_8.png' % self.char)]

        self.animation_left = [pygame.image.load('data/players/%s/left_1.png' % self.char),
                               pygame.image.load('data/players/%s/left_2.png' % self.char),
                               pygame.image.load('data/players/%s/left_3.png' % self.char),
                               pygame.image.load('data/players/%s/left_4.png' % self.char),
                               pygame.image.load('data/players/%s/left_5.png' % self.char),
                               pygame.image.load('data/players/%s/left_6.png' % self.char),
                               pygame.image.load('data/players/%s/left_7.png' % self.char),
                               pygame.image.load('data/players/%s/left_8.png' % self.char)]

        self.animation_jump = pygame.image.load('data/players/%s/jump.png' % self.char)

        self.animation_jump_right = pygame.image.load('data/players/%s/jump_right.png' % self.char)

        self.animation_jump_left = pygame.image.load('data/players/%s/jump_left.png' % self.char)

        self.animation_stand_shoot_right = [pygame.image.load('data/players/%s/stand_shoot_right_1.png' % self.char),
                                            pygame.image.load('data/players/%s/stand_shoot_right_2.png' % self.char),
                                            pygame.image.load('data/players/%s/stand_shoot_right_3.png' % self.char)]

        self.animation_stand_shoot_left = [pygame.image.load('data/players/%s/stand_shoot_left_1.png' % self.char),
                                           pygame.image.load('data/players/%s/stand_shoot_left_2.png' % self.char),
                                           pygame.image.load('data/players/%s/stand_shoot_left_3.png' % self.char)]

        self.animation_shoot_right = [pygame.image.load('data/players/%s/shoot_right_1.png' % self.char),
                                      pygame.image.load('data/players/%s/shoot_right_2.png' % self.char),
                                      pygame.image.load('data/players/%s/shoot_right_3.png' % self.char),
                                      pygame.image.load('data/players/%s/shoot_right_4.png' % self.char),
                                      pygame.image.load('data/players/%s/shoot_right_5.png' % self.char),
                                      pygame.image.load('data/players/%s/shoot_right_6.png' % self.char),
                                      pygame.image.load('data/players/%s/shoot_right_7.png' % self.char),
                                      pygame.image.load('data/players/%s/shoot_right_8.png' % self.char)]

        self.animation_shoot_left = [pygame.image.load('data/players/%s/shoot_left_1.png' % self.char),
                                     pygame.image.load('data/players/%s/shoot_left_2.png' % self.char),
                                     pygame.image.load('data/players/%s/shoot_left_3.png' % self.char),
                                     pygame.image.load('data/players/%s/shoot_left_4.png' % self.char),
                                     pygame.image.load('data/players/%s/shoot_left_5.png' % self.char),
                                     pygame.image.load('data/players/%s/shoot_left_6.png' % self.char),
                                     pygame.image.load('data/players/%s/shoot_left_7.png' % self.char),
                                     pygame.image.load('data/players/%s/shoot_left_8.png' % self.char)]

        self.animation_stand_shoot_left = [pygame.image.load('data/players/%s/stand_shoot_left_1.png' % self.char),
                                           pygame.image.load('data/players/%s/stand_shoot_left_2.png' % self.char),
                                           pygame.image.load('data/players/%s/stand_shoot_left_3.png' % self.char)]

        self.animation_jump_shoot_right = [pygame.image.load('data/players/%s/jump_shoot_right_1.png' % self.char),
                                           pygame.image.load('data/players/%s/jump_shoot_right_2.png' % self.char),
                                           pygame.image.load('data/players/%s/jump_shoot_right_3.png' % self.char)]

        self.animation_jump_shoot_left = [pygame.image.load('data/players/%s/jump_shoot_left_1.png' % self.char),
                                          pygame.image.load('data/players/%s/jump_shoot_left_2.png' % self.char),
                                          pygame.image.load('data/players/%s/jump_shoot_left_3.png' % self.char)]

        self.character = self.animation_stand

    def animation(self, player_animate, animate_delay):

        if self.frame + 1 >= animate_delay*len(player_animate):
            self.frame = 0
        self.frame += 1
        return player_animate[self.frame // animate_delay]

    def animate(self):
        if self.left:
            if self.jump:
                if self.shoot:
                    self.character = self.animation(self.animation_jump_shoot_left, 10)
                else:
                    self.character = self.animation_jump_left

            elif self.boost:
                if self.shoot:
                    self.character = self.animation(self.animation_shoot_left, 5)
                else:
                    self.character = self.animation(self.animation_left, 5)

            else:
                if self.shoot:
                    self.character = self.animation(self.animation_shoot_left, 10)
                else:
                    self.character = self.animation(self.animation_left, 10)

        elif self.right:
            if self.jump:
                if self.shoot:
                    self.character = self.animation(self.animation_jump_shoot_right, 10)
                else:
                    self.character = self.animation_jump_right

            elif self.boost:
                if self.shoot:
                    self.character = self.animation(self.animation_shoot_right, 5)
                else:
                    self.character = self.animation(self.animation_right, 5)

            else:
                if self.shoot:
                    self.character = self.animation(self.animation_shoot_right, 10)
                else:
                    self.character = self.animation(self.animation_right, 10)

        elif self.jump:
            if self.shoot:
                if self.turn_left:
                    self.character = self.animation(self.animation_jump_shoot_left, 10)
                else:
                    self.character = self.animation(self.animation_jump_shoot_right, 10)
            else:
                self.character = self.animation_jump

        else:
            if self.shoot:
                if self.turn_left:
                    self.character = self.animation(self.animation_stand_shoot_left, 10)
                else:
                    self.character = self.animation(self.animation_stand_shoot_right, 10)
            else:
                self.character = self.animation(self.animation_stand, 10)


    def draw(self, surface, pos):
        self.animate()
        surface.blit(self.character, self.player.move(pos))
        #print(self.turn_left)

    def handle(self, key):
        if key == pygame.K_a:
            self.left = not self.left
            self.turn_left = True
        if key == pygame.K_d:
            self.right = not self.right
            self.turn_left = False
        if key == pygame.K_SPACE:
            self.jump = not self.jump
        if key == pygame.K_LSHIFT:
            self.boost = not self.boost
        if key == pygame.K_f:
            self.shoot = not self.shoot

    def update(self):

        if self.jump:
            if self.onGround: # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -self.player_jump_power
                if self.boost and (self.left or self.right): # если есть ускорение и мы движемся
                    self.yvel -= self.player_boost_jump_power # то прыгаем выше

        if self.shoot:
            if self.stock_of_bullets > 0:
                if self.counts_of_bullets == 0:
                    self.counts_of_bullets = 20

                if self.counts_of_bullets == 20:
                    if self.turn_left:
                        bullet = Bullet(self.player.x + 5, self.player.y + 55, True)
                        c.bullets.append(bullet)
                        c.objects.append(bullet)
                    else:
                        bullet = Bullet(self.player.x + 55, self.player.y + 55, False)
                        c.bullets.append(bullet)
                        c.objects.append(bullet)
                    self.stock_of_bullets -=1

                self.counts_of_bullets -= 1

        if self.left:
            self.xvel = -self.player_speed # Лево = x- n
            #self.image.fill(Color(COLOR))
            if self.boost: # если ускорение
                self.xvel -= self.player_boost_speed # то передвигаемся быстрее


        if self.right:
            self.xvel = self.player_speed # Право = x + n
            #self.image.fill(Color(COLOR))
            if self.boost:
                self.xvel += self.player_boost_speed


        if not(self.left or self.right): # стоим, когда нет указаний идти
            self.xvel = 0

        if not self.onGround:
            self.yvel += self.player_gravity

        self.onGround = False; # Мы не знаем, когда мы на земле((

        self.player.y += self.yvel
        self.collide(0, self.yvel)

        self.player.x += self.xvel # переносим свои положение на xvel
        self.collide(self.xvel, 0)

    def collide_objects(self, object):
        if (self.player.right <= object.platform.left) or (self.player.top >= object.platform.bottom) or (self.player.left >= object.platform.right) or (self.player.bottom <= object.platform.top):
            return False
        else:
            return True

    def collide(self, xvel, yvel):
        for p in c.platforms:

            if self.collide_objects(p): # если есть пересечение платформы с игроком
                '''if isinstance(p, blocks.BlockDie) or isinstance(p, monsters.Monster): # если пересакаемый блок- blocks.BlockDie или Monster
                    self.die()# умираем
                elif isinstance(p, blocks.Princess): # если коснулись принцессы
                    self.winner = True # победили!!!
                elif isinstance(p, blocks.BlockTeleport):
                    self.teleporting(p.goX, p.goY)

                else:'''
                if xvel > 0:                      # если движется вправо
                    self.player.right = p.platform.left # то не движется вправо

                if xvel < 0:                      # если движется влево
                    self.player.left = p.platform.right # то не движется влево

                if yvel > 0:                      # если падает вниз
                    self.player.bottom = p.platform.top # то не падает вниз
                    self.onGround = True          # и становится на что-то твердое
                    self.yvel = 0                 # и энергия падения пропадает

                if yvel < 0:                      # если движется вверх
                    self.player.top = p.platform.bottom # то не движется вверх
                    self.yvel = 0                 # и энергия прыжка пропадает

    def move(self, dx, dy):
        self.player.x += dx
        self.player.y += dy

