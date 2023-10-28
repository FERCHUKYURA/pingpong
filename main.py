import pygame


WIDHT = 1300
HEIGHT = 700

SIZE = (WIDHT, HEIGHT)

FPS = 60

window = pygame.display.set_mode(SIZE)
backround_color = (0, 255, 0)
window.fill(backround_color)
clock = pygame.time.Clock()


class Ball(pygame.sprite.Sprite):
    def __init__(self, filename, coords, size):
        self.image = pygame.transform.scale(pygame.image.load(filename),
                                        size)


        self.rect = self.image.get_rect()
        self.rect.center = coords 

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y ))

class Racket(pygame.sprite.Sprite):
    def __init__(self, filename, coords, size, speed):
        self.image = pygame.transform.scale(
                    pygame.image.load(filename),
                    size
        )
        self.rect = self.image.get_rect()
        self.rect.center = coords

        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y ))


    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 0 :
            self.rect.y -= self.speed
        if keys[pygame.K_s]and self.rect.y < HEIGHT-200:
            self.rect.y += self.speed


    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]and self.rect.y > 0 :
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < HEIGHT-200:
            self.rect.y += self.speed        



racket_l = Racket("tennis.png", (50, HEIGHT/2 ), (75,200), 5 )

racket_r = Racket("tennis.png", (WIDHT-50, HEIGHT/2 ), (75,200), 5 )

ball = Ball("tennis-ball.png", (WIDHT/2, HEIGHT/2), (50,50))

speed_x, speed_y = 5,5



pygame.font.init()
font1 = pygame.font.Font(None, 60)

score_l = 0
score_r = 0


game = True 
finish = False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False 

    if not finish:
        window.fill(backround_color)
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        ball.reset()

        racket_l.reset()
        racket_r.reset()

        racket_l.update_l()
        racket_r.update_r()

        if ball.rect.y <= 0 or ball.rect.y >= HEIGHT - 50:
            speed_y = -speed_y

        if pygame.sprite.collide_rect(ball, racket_l) \
        or  pygame.sprite.collide_rect(ball, racket_r):
            speed_x = -speed_x

        if ball.rect.x >= WIDHT+50:
            finish = True
            text = font1.render("Переміг Лівий Гравець",True,(0,0,100))
            window.blit(text, (WIDHT/2, HEIGHT/2))


        if ball.rect.x <= -50:
            score_r += 1
            ball.rect.center = WIDTH/2, HEIGHT/2
        if score_r >= 5:
            finish = True
            text = font1.render("Переміг Правий Гравець",True,(0,0,100))
            window.blit(text, (WIDTH/2, HEIGHT/2))



        if ball.rect.x >= WIDTH+50:
            score_l +=1 
            ball.rect.center = WIDTH/2, HEIGHT/2
        if  score_l >= 5:
            finish = True
            text = font1.render("Переміг Лівий Гравець",True,(0
0,100))
            window.blit(text, (WIDTH/2, HEIGHT/2))


    pygame.display.update()
    clock.tick(FPS)


