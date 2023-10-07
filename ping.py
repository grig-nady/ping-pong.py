from pygame import *
from random import randint
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-pong")


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = "left"
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

speed_x = 3
speed_y = 3
background = transform.scale(image.load("Fon.jpg"), (win_width, win_height))
player1 = Player('racets.png', 0, 100, 5, 75, 90)
player2 = Player('racets.png', 625, 100, 5, 75, 90)   
ball = GameSprite('boll.png', 250, 250, 5, 80, 80)      
clock = time.Clock()
FPS = 60
run = True

finish = False
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('1 ПРОИГРАЛ', True, (180, 0, 0))
lose2 = font1.render('2 ПРОИГРАЛ', True, (180, 0, 0))


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.blit(background,(0,0)) 
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200,200))
    if ball.rect.x > win_width-50 :
        finish = True
        window.blit(lose2, (200,200))
    if ball.rect.y<0 or ball.rect.y>win_height-50:
        speed_y = speed_y* (-1)
    player1.update_L()
    player2.update_R()
    player1.reset()
    player2.reset()
    ball.reset()
    display.update()
    clock.tick(FPS)
    
