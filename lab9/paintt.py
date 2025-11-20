import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


PALETTE = [
    BLACK, (255, 0, 0), (0, 255, 0),
    (0, 0, 255), (255, 255, 0),
    (255, 165, 0), (128, 0, 128)
]

ERASER_COLOR = WHITE

font = pygame.font.SysFont("Arial", 18)

current_color = BLACK
brush_size = 5

draw_mode = "brush"    
start_pos = None        

win.fill(WHITE)


palette_rects = []
for i, color in enumerate(PALETTE):
    rect = pygame.Rect(10 + i * 40, 10, 30, 30)
    palette_rects.append((rect, color))

eraser_btn = pygame.Rect(10, 50, 80, 30)
save_btn   = pygame.Rect(100, 50, 80, 30)


square_btn     = pygame.Rect(200, 50, 80, 30)
right_tri_btn  = pygame.Rect(290, 50, 80, 30)
equi_tri_btn   = pygame.Rect(380, 50, 120, 30)
rhombus_btn    = pygame.Rect(510, 50, 80, 30)

def draw_ui():
    
    for rect, color in palette_rects:
        pygame.draw.rect(win, color, rect)
        if color == current_color and draw_mode == "brush":
            pygame.draw.rect(win, WHITE, rect, 3)

    
    pygame.draw.rect(win, (200, 200, 200), eraser_btn)
    pygame.draw.rect(win, (200, 200, 200), save_btn)
    pygame.draw.rect(win, (200, 200, 200), square_btn)
    pygame.draw.rect(win, (200, 200, 200), right_tri_btn)
    pygame.draw.rect(win, (200, 200, 200), equi_tri_btn)
    pygame.draw.rect(win, (200, 200, 200), rhombus_btn)

    win.blit(font.render("Eraser", True, BLACK), (eraser_btn.x + 10, eraser_btn.y + 5))
    win.blit(font.render("Save", True, BLACK),   (save_btn.x + 20, save_btn.y + 5))

    win.blit(font.render("Square", True, BLACK), (square_btn.x + 10, square_btn.y + 5))
    win.blit(font.render("Right ⊿", True, BLACK), (right_tri_btn.x + 7, right_tri_btn.y + 5))
    win.blit(font.render("Equi ⊿", True, BLACK),  (equi_tri_btn.x + 20, equi_tri_btn.y + 5))
    win.blit(font.render("Rhombus", True, BLACK), (rhombus_btn.x + 5, rhombus_btn.y + 5))


def save_drawing():
    pygame.image.save(win, "drawing.png")
    print("Saved to drawing.png")


def draw_square(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    side = min(abs(x2 - x1), abs(y2 - y1))  
    rect = pygame.Rect(x1, y1, side, side)
    pygame.draw.rect(win, current_color, rect, 2)


def draw_right_triangle(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    points = [(x1, y1), (x2, y1), (x1, y2)]
    pygame.draw.polygon(win, current_color, points, 2)


def draw_equilateral_triangle(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    size = abs(x2 - x1)

    
    p1 = (x1, y1)
    p2 = (x1 + size, y1)
    p3 = (x1 + size // 2, y1 - int(size * 0.866))  # высота = side * √3/2

    pygame.draw.polygon(win, current_color, [p1, p2, p3], 2)


def draw_rhombus(pos1, pos2):
    
    x1, y1 = pos1
    x2, y2 = pos2

    cx = (x1 + x2) // 2  
    cy = (y1 + y2) // 2  

    w = abs(x2 - x1)
    h = abs(y2 - y1)

    points = [
        (cx, y1),       
        (x2, cy),       
        (cx, y2),       
        (x1, cy)        
    ]
    pygame.draw.polygon(win, current_color, points, 2)


run = True
while run:
    draw_ui()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                start_pos = mouse_pos  

                
                for rect, color in palette_rects:
                    if rect.collidepoint(mouse_pos):
                        current_color = color
                        draw_mode = "brush"
                        start_pos = None

                
                if eraser_btn.collidepoint(mouse_pos):
                    current_color = ERASER_COLOR
                    draw_mode = "brush"
                    start_pos = None

                
                if save_btn.collidepoint(mouse_pos):
                    save_drawing()
                    start_pos = None

                if square_btn.collidepoint(mouse_pos):
                    draw_mode = "square"
                if right_tri_btn.collidepoint(mouse_pos):
                    draw_mode = "right_tri"
                if equi_tri_btn.collidepoint(mouse_pos):
                    draw_mode = "equi_tri"
                if rhombus_btn.collidepoint(mouse_pos):
                    draw_mode = "rhombus"

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and start_pos is not None:
                end_pos = pygame.mouse.get_pos()

                
                if draw_mode == "square":
                    draw_square(start_pos, end_pos)
                elif draw_mode == "right_tri":
                    draw_right_triangle(start_pos, end_pos)
                elif draw_mode == "equi_tri":
                    draw_equilateral_triangle(start_pos, end_pos)
                elif draw_mode == "rhombus":
                    draw_rhombus(start_pos, end_pos)

                start_pos = None   # reset

    
    if pygame.mouse.get_pressed()[0] and draw_mode == "brush":
        mx, my = pygame.mouse.get_pos()
        pygame.draw.circle(win, current_color, (mx, my), brush_size)

pygame.quit()
sys.exit()