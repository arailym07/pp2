import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PALETTE = [BLACK, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]
ERASER_COLOR = WHITE

font = pygame.font.SysFont("Arial", 18)

current_color = BLACK
brush_size = 5
drawing = False

win.fill(WHITE)

palette_rects = []
for i, color in enumerate(PALETTE):
    rect = pygame.Rect(10 + i * 40, 10, 30, 30)
    palette_rects.append((rect, color))


eraser_btn = pygame.Rect(10, 50, 80, 30)
save_btn = pygame.Rect(100, 50, 80, 30)

def draw_ui():
    for rect, color in palette_rects:
        pygame.draw.rect(win, color, rect)
        if color == current_color:
            pygame.draw.rect(win, WHITE, rect, 3)

    pygame.draw.rect(win, (200, 200, 200), eraser_btn)
    pygame.draw.rect(win, (200, 200, 200), save_btn)
    win.blit(font.render("Eraser", True, BLACK), (eraser_btn.x + 10, eraser_btn.y + 5))
    win.blit(font.render("Save", True, BLACK), (save_btn.x + 20, save_btn.y + 5))

def save_drawing():
    pygame.image.save(win, "drawing.png")
    print("Saved to drawing.png")

run = True
while run:
    draw_ui()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mouse_pos = pygame.mouse.get_pos()
                drawing = True


                for rect, color in palette_rects:
                    if rect.collidepoint(mouse_pos):
                        current_color = color
                        drawing = False

                if eraser_btn.collidepoint(mouse_pos):
                    current_color = ERASER_COLOR
                    drawing = False

                if save_btn.collidepoint(mouse_pos):
                    save_drawing()
                    drawing = False

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

    if drawing:
        mx, my = pygame.mouse.get_pos()
        pygame.draw.circle(win, current_color, (mx, my), brush_size)

pygame.quit()
sys.exit()