import random

import pygame

FPS = 60
SPEED = 5

LEFT = 0
RIGHT = 1
NONE = -1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (63, 72, 204)

window_width = 1080
window_height = 720
flags = pygame.RESIZABLE
background_color = WHITE

platform_pos = []
platform_width = 0
platform_height = 0

level = list()


def main():
    global screen
    pygame.init()
    window_size = (window_width, window_height)
    screen = pygame.display.set_mode(window_size, flags)
    pygame.display.set_caption("ZzeRoTiMe Project")
    window_update()
    while True:
        run_arch(0)


def window_update():
    screen.fill(background_color)
    create_platform()
    pygame.display.update()


def create_platform():
    global platform_pos, platform_width, platform_height
    platform_width = window_width // 14
    platform_height = 10
    if len(platform_pos) == 0:
        platform_x = window_width // 2 - platform_width // 2
        platform_y = window_height - 50
        platform_pos = [platform_x, platform_y]
    pygame.draw.rect(screen, BLACK, (platform_pos[0], platform_pos[1], platform_width, platform_height))


def show_pause_text():
    font_pause = pygame.font.Font(None, 72)
    text_pause = font_pause.render("Пауза", False, BLACK)
    text_width, text_height = font_pause.size("Пауза")
    screen.blit(text_pause, (window_width // 2 - text_width // 2, window_height // 2 - text_height))

    font_continue = pygame.font.Font(None, 36)
    text_continue = font_continue.render("Нажмите пробел, чтобы продолжить", False, BLACK)
    text_width, text_height = font_continue.size("Нажмите пробел, чтобы продолжить")
    screen.blit(text_continue, (window_width // 2 - text_width // 2, window_height // 1.75))


def show_pause_screen():
    global window_width, window_height
    pause = pygame.Surface((window_width, window_height), pygame.SRCALPHA)
    pause.fill((63, 72, 204, 127))
    show_pause_text()
    screen.blit(pause, (0, 0))
    pygame.display.update()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                info_object = pygame.display.Info()
                window_width = info_object.current_w
                window_height = info_object.current_h
                window_update()
                show_pause_screen()
                return
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    return


def generate_level():
    for i in range(random.randint(1, 5)):
        for j in range(random.randint(1, 10)):
            pass


def run_arch(speed):
    global window_height, window_width, platform_pos
    direction = NONE
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_a]:
                    direction = LEFT
                if keys[pygame.K_d]:
                    direction = RIGHT
                if keys[pygame.K_SPACE]:
                    show_pause_screen()
            if event.type == pygame.VIDEORESIZE:
                info_object = pygame.display.Info()
                window_width = info_object.current_w
                window_height = info_object.current_h
                if direction == NONE:
                    platform_pos[0] = window_width // 2 - platform_width // 2
                    platform_pos[1] = window_height - 50
                window_update()
        if platform_pos[0] <= 0 or platform_pos[0] + platform_width >= window_width:
            direction = not direction
        if direction == RIGHT:
            speed = SPEED
        if direction == LEFT:
            speed = -SPEED
        platform_pos[0] += speed
        window_update()
        pygame.time.Clock().tick(FPS)


if __name__ == '__main__':
    main()
