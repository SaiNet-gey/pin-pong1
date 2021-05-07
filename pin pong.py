from pygame import *
from random import randint

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
        if keys[K_UP] and self.rect.y > 3:
            self.rect.y -= 10
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += 10
    def update_l(self):
        keys = key.get_pressed()        
        if keys[K_w] and self.rect.y > 3:
            self.rect.y -= 10
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += 10

    
#вещи 
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 1320, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

speed_x = randint(1, 9)
speed_y = randint(1, 9)

speed_racket1 = 20
speed_racket2 = 20

win_width = 1400
win_height = 700
win = display.set_mode((win_width, win_height))
blue = 'fon.png'
display.set_caption('Pin-Pong')
bg = transform.scale(image.load(blue),(win_width, win_height))

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))


finish = False 
game = True
clock = time.Clock()
FPS = 120

'''while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:

        ball_.rect.x += 10 
        ball_.rect.y += 10

        if sprite.collide_rect(racket1, ball_) or sprite.collide_rect(racket2, ball_):
            speed_x *= -1
            speed_y *= 1
        
        if ball_.rect.y > win_height-50 or ball_.rect.y < 0:
            speed_y *= -1    


        if ball_.rect.x < 0: 
            finish = True 
            win.blit(lose1, (200, 200))
            game_over = True 

        if ball_.rect.x < win_width: 
            finish = True 
            win.blit(lose2, (200, 200))
            game_over = True     

        win.blit(bg,(0, 0))
        racket1.update_l()
        racket2.update_r()
        
        racket1.reset()
        racket2.reset()
        ball_.reset()
        
    display.update()
    #time.delay(-100)
    clock.tick(FPS)'''
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        win.blit(bg,(0, 0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        
        # если мяч достигает границ экрана меняем направление его движения
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        # если мяч улетел дальше ракетки, выводим условие проигрыша для первого игрока
        if ball.rect.x < 0:
            finish = True
            win.blit(lose1, (200, 200))
            game_over = True

        # если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока
        if ball.rect.x > win_width:
            finish = True
            win.blit(lose2, (200, 200))
            game_over = True

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
    


