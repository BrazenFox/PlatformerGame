from pygame import image, Color, Rect, draw, Surface
import config as c

class Bullet:
    def __init__(self, x, y, direction):
        self.bullet = Rect(x, y, c.bullet_radius*2, c.bullet_radius*2)
        self.speed = c.speed_bullet
        self.x_speed = 0
        self.y_speed = 0
        self.direction = direction
        self.collision = False

    '''def left(self):
        return self.platform.left
    def right(self):
        return self.platform.right
    def top(self):
        return self.platform.top
    def bottom(self):
        return self.platform.bottom'''

    def draw(self, surface, pos):
        if not self.collision:
            draw.circle(surface, c.color_bullet, (self.bullet.x + pos[0],  self.bullet.y + pos[1]), c.bullet_radius)  # Position is the center of the circle.

    def update(self):
        if not self.collision:
            if self.direction:               #влево
                self.x_speed = -self.speed
            else:                            #вправо
                self.x_speed = self.speed

            self.bullet.x += self.x_speed
            self.collide(self.speed, 0)

            self.bullet.y += self.y_speed
            self.collide(self.speed, 0)

    def collide_objects(self, object):
        if (self.bullet.right <= object.platform.left) or (self.bullet.top >= object.platform.bottom) or (self.bullet.left >= object.platform.right) or (self.bullet.bottom <= object.platform.top):
            return False
        else:
            return True

    def collide(self, xvel, yvel):
        for p in c.platforms:

            if self.collide_objects(p):  # если есть пересечение платформы с пулей
                self.collision = True
                for b in c.bullets:
                    if b.collision:
                        c.objects.remove(b)
                c.bullets = []
                '''if isinstance(p, blocks.BlockDie) or isinstance(p, monsters.Monster): # если пересакаемый блок- blocks.BlockDie или Monster
                    self.die()# умираем
                elif isinstance(p, blocks.Princess): # если коснулись принцессы
                    self.winner = True # победили!!!
                elif isinstance(p, blocks.BlockTeleport):
                    self.teleporting(p.goX, p.goY)

                else:'''
                if xvel > 0:  # если движется вправо
                    self.bullet.right = p.platform.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.bullet.left = p.platform.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.bullet.bottom = p.platform.top  # то не падает вниз

                if yvel < 0:  # если движется вверх
                    self.bullet.top = p.platform.bottom  # то не движется вверх

    def move(self, dx):
        self.bullet.x += dx