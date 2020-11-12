import random
from datetime import datetime, timedelta

import sys
import time
import pygame
from pygame.rect import Rect

import config as c

from button import Button
from button import Character_button
from blocks import Platform
from player import Player
from game_engine import GameEngine
from images import Image
from text_object import TextObject
import colors

class GetDiploma(GameEngine):

    def __init__(self):
        GameEngine.__init__(self, 'Platformer', c.screen_width, c.screen_height, c.background_image, c.frame_rate)
        self.reset_effect = None
        self.effect_start_time = None
        self.score = 0
        #self.lives = c.initial_lives
        self.start_level = False



        #self.platforms = []
        self.monsters = []
        self.animatedobjects = []
        self.level = []
        self.level_width = 0
        self.level_height = 0

        self.is_game_running = False
        self.create_menu_objects()
        self.points_per_brick = 1

        self.playerX = 0
        self.playerY = 0

        self.style_player = "boy"

    def create_menu(self):

        def on_play(button):
            '''for b in self.menu_objects:
                self.objects.remove(b)'''
            self.menu_objects = []
            self.is_game_running = True
            self.start_level = True
            self.play = True
            self.create_game_objects()

        def on_quit(button):
            self.game_over = True
            self.is_game_running = False
            self.game_over = True
            pygame.quit()
            sys.exit

        def on_move_girl(button):
            self.image.character_change(c.menu_girl)

        def on_click_girl(button):
            #print("selected girl")
            self.style_player = "girl"

        def on_move_boy(button):
            self.image.character_change(c.menu_boy)

        def on_click_boy(button):
            #print("selected boy")
            self.style_player = "boy"

        for i, (text, click_handler) in enumerate((('PLAY', on_play), ('QUIT', on_quit))):
            b = Button(c.menu_offset_x,
                       c.menu_offset_y + (c.menu_button_h + 5) * i*3,
                       c.menu_button_w,
                       c.menu_button_h,
                       text,
                       click_handler,
                       padding=5)

            #self.objects.append(b)
            self.menu_objects.append(b)
            self.mouse_handlers.append(b.handle_mouse_event)

        for i, (text, click_handler, move_handler) in enumerate((('GIRL', on_click_girl, on_move_girl), ('BOY', on_click_boy, on_move_boy))):
            b = Character_button(c.menu_offset_x,
                       c.menu_offset_y + (c.menu_button_h + 5) * (i+1),
                       c.menu_button_w,
                       c.menu_button_h,
                       text,
                       click_handler,
                       move_handler,
                       padding=5)

            #self.objects.append(b)
            self.menu_objects.append(b)
            self.mouse_handlers.append(b.handle_mouse_event)

    def create_image(self):
        self.image = Image(c.center_image_x, c.center_image_y, c.menu_boy)
        #self.objects.append(self.image)
        self.menu_objects.append(self.image)

    def create_menu_objects(self):
        self.create_menu()
        self.create_image()

    def create_game_objects(self):
        #print("created")
        self.loadLevel()
        self.create_player()

    def loadLevel(self):
        levelFile = open('data/levels/1.txt') # config!!!!
        line = " "
        commands = []
        while line[0] != "/": # пока не нашли символ завершения файла
            line = levelFile.readline() #считываем построчно
            if line[0] == "[": # если нашли символ начала уровня
                x=y=0 # координаты
                while line[0] != "]": # то, пока не нашли символ конца уровня
                    line = levelFile.readline() # считываем построчно уровень
                    if line[0] != "]": # и если нет символа конца уровня
                        self.level_height += 1
                        endLine = line.find("|") # то ищем символ конца строки
                        #self.level.append(line[0: endLine]) # и добавляем в уровень строку от начала до символа "|"
                        for col in line[0: endLine]: # каждый символ
                            self.level_width += 1
                            '''if col == "*":
                                die_block = BlockDie(x,y)
                                self.objects.append(die_block)
                                self.platforms.append(die_block)'''
                            if col == "-":
                                platform = Platform(x,y)
                                self.objects.append(platform)
                                c.platforms.append(platform)
                            '''if col == "P":
                                princess = Princess(x,y)
                                self.objects.append(princess)
                                self.platforms.append(princess)
                                self.animatedobjects.append(princess)'''

                            x += c.platform_width #блоки платформы ставятся на ширине блоков

                        y += c.platform_height    #то же самое и с высотой
                        x = 0                   #на каждой новой строчке начинаем с нуля

                self.level_width //= self.level_height
                self.level_width *= c.platform_width
                self.level_height *= c.platform_height
                self.game_camera = pygame.Rect(0, 0, self.level_width, self.level_height)

            if line[0] != "": # если строка не пустая
                commands = line.split() # разбиваем ее на отдельные команды
                if len(commands) > 1: # если количество команд > 1, то ищем эти команды
                    if commands[0] == "player": # если первая команда - player
                        self.playerX = int(commands[1]) # то записываем координаты героя
                        self.playerY = int(commands[2])
                    '''if commands[0] == "portal": # если первая команда portal, то создаем портал
                        teleport_block = BlockTeleport(int(commands[1]),int(commands[2]),int(commands[3]),int(commands[4]))
                        self.objects.append(teleport_block)
                        self.platforms.append(teleport_block)
                        self.animatedobjects.append(teleport_block)
                    if commands[0] == "monster": # если первая команда monster, то создаем монстра
                        monster = Monster(int(commands[1]),int(commands[2]),int(commands[3]),int(commands[4]),int(commands[5]),int(commands[6]))
                        self.objects.append(monster)
                        self.platforms.append(monster)
                        self.monsters.append(monster)'''

    def create_player(self):
        player = Player(self.playerX,
                        self.playerY,
                        c.player_width,
                        c.player_height,
                        self.style_player)

        self.keydown_handlers[pygame.K_SPACE].append(player.handle)
        self.keyup_handlers[pygame.K_SPACE].append(player.handle)

        self.keydown_handlers[pygame.K_a].append(player.handle)
        self.keyup_handlers[pygame.K_a].append(player.handle)

        self.keydown_handlers[pygame.K_d].append(player.handle)
        self.keyup_handlers[pygame.K_d].append(player.handle)

        self.keydown_handlers[pygame.K_LSHIFT].append(player.handle)
        self.keyup_handlers[pygame.K_LSHIFT].append(player.handle)

        self.keydown_handlers[pygame.K_f].append(player.handle)
        self.keyup_handlers[pygame.K_f].append(player.handle)

        self.player = player
        self.objects.append(self.player)











def main():
    GetDiploma().run()

if __name__ == '__main__':
    main()
