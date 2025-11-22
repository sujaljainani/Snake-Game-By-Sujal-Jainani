import pygame
import random

pygame.init()

# Screen
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake properties
snake_size = 10
snake_speed = 15
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)


def message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [WIDTH/4, HEIGHT/2])


def game_loop():
    game_over = False
    game_close = False

    x = WIDTH / 2
    y = HEIGHT / 2
    dx = 0
    dy = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, WIDTH - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press C to play again or Q to quit.", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_size
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_size
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_size
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_size
                    dx = 0

        # move snake
        x += dx
        y += dy

        # boundary check
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        screen.fill(BLACK)

        # draw food
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_size, snake_size])

        # update snake list
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # collision with itself
        for part in snake_list[:-1]:
            if part == snake_head:
                game_close = True

        # draw snake
        for part in snake_list:
            pygame.draw.rect(screen, GREEN, [part[0], part[1], snake_size, snake_size])

        # eating food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - snake_size) / 10.0) * 10.0
            snake_length += 1

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()


game_loop()