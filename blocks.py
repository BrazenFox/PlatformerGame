from pygame import image, Color, Rect, draw
import config as c

class Platform:
    def __init__(self, x, y):
        self.PLATFORM_HEIGHT = c.platform_height
        self.PLATFORM_WIDTH = c.platform_width
        self.PLATFORM_COLOR = c.platform_color
        #self.platform_image = image.load("data/blocks/platform.png")
        #self.platform_image.set_colorkey(Color(self.PLATFORM_COLOR))
        self.platform = Rect(x, y, self.PLATFORM_WIDTH, self.PLATFORM_HEIGHT)


    '''def left(self):
        return self.platform.left
    def right(self):
        return self.platform.right
    def top(self):
        return self.platform.top
    def bottom(self):
        return self.platform.bottom'''

    def draw(self, surface, pos):
        #surface.blit(self.platform_image, self.platform.move(pos))
        draw.rect(surface, self.PLATFORM_COLOR, self.platform.move(pos))

    def update(self):
        pass

    def move(self, dx, dy):
        self.platform.x += dx
        self.platform.y += dy