from pygame import *

win_height = 500
win_width = 700

COLOR_RED = (255, 0 , 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

font.init()
font1 = font.SysFont("Arial", 72)

win = font1.render("YOU WIN!", True, COLOR_WHITE)
lose = font1.render("YOU LOSE!", True, COLOR_WHITE)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # function for output player
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # function for moving the player
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height:
            self.rect.y += self.speed

# class for create walls
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        # картинка стіни - прямокутник потрібних розмірів та кольору
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        # кожен спрайт повинен зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))

# стіни - walls
w1 = Wall(0, 0, 0, 185, 335, 10, 80)
w2 = Wall(0, 0, 0, 0, 440, 700, 10)
w3 = Wall(0, 0, 0, 270, 245, 10, 80)
w4 = Wall(0, 0, 0, 370, 245, 10, 80)
w5 = Wall(0, 0, 0, 0, 90, 700, 10)

# basic setting for window(size of window, window caption)
window = display.set_mode((win_width, win_height))
display.set_caption("Geometry Dash 2.0")

# create and settings background
bg = transform.scale(image.load("background1.png"), (700, 500))

# create and settings for player and win point
player = Player("player.png", 70, 350, 60, 60, 4)
win_point = Player("win_point.png", 600, 350, 50, 50, 0 )

# game settings
game = True
finish = False
clock = time.Clock()
FPS = 60

# game 
while game:
    # keys and keyboard
    for e in event.get():
        # here we implement exit from the game
        if e.type == QUIT:
            game = False

    if not finish:
        # Screen cleaning
        window.fill((0, 0, 0))
    
        # screen output
        window.blit(bg, (0, 0))

        window.blit(win_point.image, (600, 350))
        
        player.update()
        player.reset()

        # малюємо стіни - draw the wall
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()


        # win
        if sprite.collide_rect(player, win_point):
            finish = True
            window.blit(win, (200, 200))

        # lose
        if sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5):
            finish = True
            window.blit(lose, (200, 200))

        display.flip()

    clock.tick(FPS) # you can use time.delay(50) 