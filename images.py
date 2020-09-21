import pygame
import config as c

class Image:
    def __init__(self, x, y, character):
        self.pos = (x,y)
        self.character =  pygame.image.load(character)

    def draw(self, surface):
        #pos = self.character.get_rect(center=(self.pos[0], self.pos[1]))
        surface.blit(self.character, self.pos)

    def character_change(self, character):
        self.character =  pygame.image.load(character)

    def update(self):
        pass
