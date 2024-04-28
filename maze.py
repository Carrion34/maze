#создай игру "Лабиринт"!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def recet(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            self.rect.y -= 10
        if keys_pressed[K_DOWN]:
            self.rect.y += 10
        if keys_pressed[K_RIGHT]:
            self.rect.x += 10
        if keys_pressed[K_LEFT]:
            self.rect.x -= 10
            
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 700 - 85:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super(). __init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    
#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Изображение')
#задай фон сцены
background = transform.scale(image.load('background.jpg'), (700, 500))
x1 = 100
x2 = 200
y1 = 130
y2 = 400

FPS = 60
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
clock = time.Clock()
hero = Player('hero.png', x1, y1, 10)
cyborg = Enemy('cyborg.png', x2, y2, 10)
treasure = GameSprite('treasure.png', 200, 120, 0)
wall_1 = Wall(100, 30, 40, 100, 100, 300, 15)
wall_2 = Wall(100, 30, 40, 160, 100, 15, 300)
wall_3 = Wall(100, 30, 40, 160, 200, 300, 15)
wall_4 = Wall(100, 30, 40, 250, 385, 300, 15)
wall_5 = Wall(100, 30, 40, 300, 285, 15, 100)
wall_6 = Wall(100, 30, 40, 400, 200, 15, 100)
wall_7 = Wall(100, 30, 40, 540, 100, 15, 300)
wall_8 = Wall(100, 30, 40, 160, 0, 15, 100)
wall_9 = Wall(100, 30, 40, 0, 0, 15, 700)
wall_10 = Wall(100, 30, 40, 0, 0, 700, 15)
wall_11 = Wall(100, 30, 40, 690, 0, 15, 500)
wall_12 = Wall(100, 30, 40, 0, 490, 700, 15)
game = True
while game:
    window.blit(background, (0, 0))
    hero.update()
    cyborg.update()
    wall_1.draw_wall()
    wall_2.draw_wall()
    wall_3.draw_wall()
    wall_4.draw_wall()
    wall_5.draw_wall()
    wall_6.draw_wall()
    wall_7.draw_wall()
    wall_8.draw_wall()
    wall_9.draw_wall()
    wall_10.draw_wall()
    wall_11.draw_wall()
    wall_12.draw_wall()
    clock.tick(FPS)
    treasure.recet()
    hero.recet()
    cyborg.recet()
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()