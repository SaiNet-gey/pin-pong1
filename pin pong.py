from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight , height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()        
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#вещи 
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 920, 200, 4, 50, 150)
ball_ = GameSprite('ball.png', 200, 200, 4, 50, 50)

speed_x = 300
speed_y = 300


win_width = 1000
win_height = 700
win = display.set_mode((win_width, win_height))
blue = 'fon.png'
display.set_caption('Pin-Pong')
bg = transform.scale(image.load(blue),(win_width, win_height))

run = True
finish = False 
game = True
clock = time.Clock()
FPS = 9999

while run: 
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        
        win.blit(bg,(0, 0))
        racket1.update_l()
        racket2.update_r()
    
        racket1.reset()
        racket2.reset()
        ball_.reset()
    display.update()
    time.delay(40)
    


    

from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight , height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()        
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#вещи 
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 920, 200, 4, 50, 150)
ball_ = GameSprite('ball.png', 200, 200, 4, 50, 50)

speed_x = 300
speed_y = 300


win_width = 1000
win_height = 700
win = display.set_mode((win_width, win_height))
blue = 'fon.png'
display.set_caption('Pin-Pong')
bg = transform.scale(image.load(blue),(win_width, win_height))

run = True
finish = False 
game = True
clock = time.Clock()
FPS = 9999

while run: 
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        
        win.blit(bg,(0, 0))
        racket1.update_l()
        racket2.update_r()
    
        racket1.reset()
        racket2.reset()
        ball_.reset()
    display.update()
    time.delay(40)
    

