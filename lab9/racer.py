import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0         
COINS = 0         

COINS_TO_INCREASE_SPEED = 10  

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("road.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")


class Enemy(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.image = pygame.image.load("enemy_car.png")
        self.image = pygame.transform.scale(self.image, (60, 120))
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)

        # Ушёл вниз → начисляем очко + телепорт вверх
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.reset_position()


class Player(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.image = pygame.image.load("player_car.png")
        self.image = pygame.transform.scale(self.image, (60, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()

        
        coin_type = random.choice(["bronze", "silver", "gold"])

        if coin_type == "bronze":
            self.value = 1
            size = 25
            color = (205, 127, 50)

        elif coin_type == "silver":
            self.value = 3
            size = 25
            color = (192, 192, 192)

        else:
            self.value = 5
            size = 30
            color = (255, 215, 0)

        
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (size // 2, size // 2), size // 2)

        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()


P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()

coins.add(Coin())

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(*coins)


INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

pygame.mixer.Sound("drive.mp3").play(-1)


while True:

    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # дополнительный рост скорости каждую секунду
        if event.type == INC_SPEED:
            SPEED += 0.1

    # DRAW BACKGROUND
    DISPLAYSURF.blit(background, (0, 0))

    # HUD — счёт
    score_text = font_small.render(f"Score: {SCORE}", True, WHITE)
    coin_text = font_small.render(f"Coins: {COINS}", True, WHITE)

    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (10, 35))

    # MOVE & DRAW ALL
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    
    # COIN 
    coin_collected = pygame.sprite.spritecollide(P1, coins, True)
    for coin in coin_collected:
        COINS += coin.value

        if COINS % COINS_TO_INCREASE_SPEED == 0:
            SPEED += 1

        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)


    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("crash.mp3").play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)