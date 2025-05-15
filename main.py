import pygame

pygame.init()


size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Рисование фигур")
BACKGROUND = (0, 0, 0)
screen.fill(BACKGROUND)


LINE_COLOR = (255, 255, 255)
PREVIEW_COLOR = (192, 192, 192)


all_lines = []
current_line = []
draw_connected = True
drawing = False


FPS = 60
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                if draw_connected:
                    if not all_lines:
                        all_lines.append([])
                    all_lines[-1].append(event.pos)
                else:
                    current_line.append(event.pos)

            elif event.button == 3:
                draw_connected = not draw_connected

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                drawing = False
                if not draw_connected and current_line:
                    all_lines.append(current_line.copy())
                    current_line = []

        elif event.type == pygame.MOUSEMOTION and drawing:
            if draw_connected:
                if all_lines:
                    all_lines[-1].append(event.pos)
            else:
                current_line.append(event.pos)


    screen.fill(BACKGROUND)


    for line in all_lines:
        if len(line) > 1:
            pygame.draw.lines(screen, LINE_COLOR, False, line, 3)


    if not draw_connected and len(current_line) > 1:
        pygame.draw.lines(screen, LINE_COLOR, False, current_line, 3)


    if draw_connected and all_lines and len(all_lines[-1]) > 0:
        last_point = all_lines[-1][-1]
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.aaline(screen, PREVIEW_COLOR, last_point, mouse_pos, 2)


    font = pygame.font.SysFont(None, 36)
    mode_text = "Режим: СВЯЗАННЫЕ линии (ПКМ - переключить режимы)" if draw_connected else "Режим: ОТДЕЛЬНЫЕ линии (ПКМ - переключить режимы)"
    text_surface = font.render(mode_text, True, LINE_COLOR)
    screen.blit(text_surface, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()