import pygame

from text_object import TextObject
import config as c


class Button:
    def __init__(self, x, y, w, h, text, on_click=lambda x: None,  padding=0):
        self.bounds =  pygame.Rect(x, y, w, h) # прямоугольный объект
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.padding = padding
        self.state = 'normal'
        self.on_click = on_click
        self.text = TextObject(x + padding, y + padding, lambda: text, c.button_text_color, c.font_name, c.font_size)

    @property
    def back_color(self):
        return dict(normal=c.button_normal_back_color,
                    hover=c.button_hover_back_color,
                    pressed=c.button_pressed_back_color)[self.state]

    def draw(self, surface):
        pygame.draw.rect(surface, self.back_color, self.bounds)
        self.text.draw(surface)
    def update(self):
        pass
    def handle_mouse_event(self, type, pos):
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)

    def handle_mouse_move(self, pos):
        if self.bounds.collidepoint(pos):
            if self.state != 'pressed':
                self.size_button(self.state)
                self.state = 'hover'
        else:
            self.size_button(self.state)
            self.state = 'normal'

    def handle_mouse_down(self, pos):
        if self.bounds.collidepoint(pos):
            self.size_button(self.state)
            self.state = 'pressed'

    def handle_mouse_up(self, pos):
        if self.state == 'pressed':
            self.size_button(self.state)
            self.on_click(self)
            self.state = 'hover'

    def size_button(self, state):
        if self.state != 'normal':
            self.bounds.height = self.h + c.button_loop_h
            self.bounds.width = self.w + c.button_loop_w
            self.bounds.x = self.x - c.button_loop_w//2
            self.bounds.y = self.y - c.button_loop_h//2
            self.text.change_font(c.font_size_loop, (self.bounds.x + self.padding, self.bounds.y + self.padding))
        else:
            self.bounds.height = self.h
            self.bounds.width = self.w
            self.bounds.x = self.x
            self.bounds.y = self.y
            self.text.change_font(c.font_size, (self.bounds.x + self.padding, self.bounds.y + self.padding))

class Character_button(Button):
    def __init__(self, x, y, w, h, text, on_click=lambda x: None, on_move=lambda x: None,  padding=0):
        super().__init__(x, y, w, h,  text, on_click, padding)
        self.on_move = on_move

    def handle_mouse_move(self, pos):
        if self.bounds.collidepoint(pos):
            if self.state != 'pressed':
                self.size_button(self.state)
                self.on_move(self)
                self.state = 'hover'
        else:
            self.size_button(self.state)
            self.state = 'normal'

    def handle_mouse_down(self, pos):
        if self.bounds.collidepoint(pos):
            self.size_button(self.state)
            self.on_move(self)
            self.state = 'pressed'
