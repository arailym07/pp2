import pygame
import math
import datetime
import sys

pygame.init()

#фон

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock + Music Player")

BLACK = (0, 0, 0)
RED = (255, 0, 0)

background = pygame.image.load("mickey.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# music
pygame.mixer.init()
songs = ["music.mp3", "mus2.mp3", "mus3.mp3"]
current_song = 0

def play_music():
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play(-1)  # (-1) — бесконечное воспроизведение

def next_song():
    global current_song
    current_song = (current_song + 1) % len(songs)
    play_music()

def prev_song():
    global current_song
    current_song = (current_song - 1) % len(songs)
    play_music()

# сразу начинаем играть первую песню
play_music()

# центр часов
cx, cy = WIDTH // 2, HEIGHT // 2

clock = pygame.time.Clock()
running = True

# Главный цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

        # управление плеером
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # play
                play_music()
            elif event.key == pygame.K_s:  # stop
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:  # next song
                next_song()
            elif event.key == pygame.K_b:  # previous song
                prev_song()

    # сlock
    now = datetime.datetime.now()
    sec = now.second
    minute = now.minute
    hour = now.hour % 12

    # вычисляем углы стрелок
    sec_angle = math.radians(sec * 6 - 90)
    min_angle = math.radians(minute * 6 - 90)
    hour_angle = math.radians(hour * 30 - 90)

    # координаты концов стрелок
    sec_x = cx + 180 * math.cos(sec_angle)
    sec_y = cy + 180 * math.sin(sec_angle)

    min_x = cx + 140 * math.cos(min_angle)
    min_y = cy + 140 * math.sin(min_angle)

    hour_x = cx + 100 * math.cos(hour_angle)
    hour_y = cy + 100 * math.sin(hour_angle)

    # === Рисуем ===
    screen.blit(background, (0, 0))  # твой фон
    pygame.draw.line(screen, BLACK, (cx, cy), (hour_x, hour_y), 8)
    pygame.draw.line(screen, BLACK, (cx, cy), (min_x, min_y), 5)
    pygame.draw.line(screen, RED, (cx, cy), (sec_x, sec_y), 2)
    pygame.draw.circle(screen, BLACK, (cx, cy), 10)  # центр часов

    pygame.display.flip()
    clock.tick(60)
