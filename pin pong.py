from pygame import *

win_width = 1000
win_height = 700
win = display.set_mode((win_width, win_height))
blue = 'fon.png'
display.set_caption('Pin-Pong')
bg = transform.scale(image.load(blue),(win_width, win_height))

run = True
finish = False 

while run: 
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        win.blit(bg,(0, 0))

    display.update()
    time.delay(40)
    

