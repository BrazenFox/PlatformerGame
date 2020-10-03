import pygame
import sys
import config as c
from collections import defaultdict


class GameEngine:
    def __init__(self, caption, width, height, back_image_filename, frame_rate):
        self.width = width
        self.height = height
        self.frame_rate = frame_rate
        self.game_over = False
        self.play = False
        self.objects = c.objects
        self.menu_objects = []
        self.player = None
        self.game_camera = None

        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height))
        # self.surface = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)

        pygame.display.set_caption(caption)

        # self.background_image = pygame.image.load(back_image_filename)

        self.background_image = pygame.Surface((width, height))  # Создание видимой поверхности
        self.background_image.fill(pygame.Color("#004400"))
        '''self.background_image = pygame.Surface((width, height))  # Создание видимой поверхности
        self.background_image.fill(pygame.Color("#004400"))'''
        ####

        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []

    def camera(self):
        x = self.player.player.x
        y = self.player.player.y
        x, y = -x + self.width / 2, -y + self.height / 2

        x = min(0, x)  # Не движемся дальше левой границы
        x = max(-(self.game_camera.width - self.width), x)  # Не движемся дальше правой границы
        y = max(-(self.game_camera.height - self.height), y)  # Не движемся дальше нижней границы
        y = min(0, y)  # Не движемся дальше верхней границы
        self.game_camera.x = x
        self.game_camera.y = y

    def update(self):
        if self.play:
            for o in self.objects:
                o.update()
        else:
            for o in self.menu_objects:
                o.update()

    def draw(self):
        if self.play:
            for o in self.objects:
                o.draw(self.surface, self.game_camera.topleft)
        else:
            for o in self.menu_objects:
                o.draw(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()

            if self.play:
                self.camera()

            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)
