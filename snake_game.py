import pygame
import random
import time
import os

pygame.init()

# Set up the game window
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")
width = 500
height = 500

def draw_grid():
    """
    Draws the grid on the game window.
    """
    for x in range(0, width, 10):
        pygame.draw.line(window, (40, 40, 40), (x, 0), (x, height))
    for y in range(0, height, 10):
        pygame.draw.line(window, (40, 40, 40), (0, y), (width, y))

# Initialize the snake
snake_head = [250, 250]
snake_body = [[250, 250], [240, 250], [230, 250], [220, 250]]
direction = 'RIGHT'
change_to = direction
snake_block = 10
snake_speed = 15

# Initialize the bait
bait_pos = [random.randrange(1, int(width / 10)) * 10, random.randrange(1, int(height / 10)) * 10]
bait_size = 10
bait_color = (255, 0, 0)
bait_width = 10
bait_height = 10

def bait_position():
    """
    Generates a new random position for the bait.
    """
    bait_pos[0] = random.randrange(1, int(width / 10)) * 10
    bait_pos[1] = random.randrange(1, int(height / 10)) * 10
    return bait_pos

# Initialize the score
score = 0
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_score(score):
    """
    Displays the current score on the game window.
    """
    value = score_font.render("Your Score: " + str(score), True, (255, 255, 255))
    window.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    """
    Draws the snake on the game window.
    """
    for x in snake_list:
        pygame.draw.rect(window, (0, 255, 0), [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """
    Displays a message on the game window.
    """
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

def eat_bait(snake_head, bait_pos):
    """
    Checks if the snake has eaten the bait.
    """
    if snake_head[0] == bait_pos[0] and snake_head[1] == bait_pos[1]:
        return True
    else:
        return False

def snake_collision(snake_head, snake_body):
    """
    Checks if the snake has collided with itself or the walls.
    """
    if snake_head in snake_body[1:]:
        return True
    else:
        if snake_head[0] < 0 or snake_head[0] >= width:
            return True
        if snake_head[1] < 0 or snake_head[1] >= height:
            return True
        return False

time.sleep(1)
clock = pygame.time.Clock()

def pause():
    """
    Pauses the game.
    """
    paused = True
    message("Paused", (255, 255, 255))
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        clock.tick(5)

def game_over():
    """
    Handles the game over state.
    """
    game_over = True
    message("Game Over, Continue = C, Quit = Q ", (255, 255, 255))
    pygame.display.update()
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    game_over = False
                    newgame()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        clock.tick(5)

def newgame():
    """
    Resets the game to start a new game.
    """
    global snake_head, snake_body, direction, change_to, bait_pos, score
    snake_head = [250, 250]
    snake_body = [[250, 250], [240, 250], [230, 250], [220, 250]]
    direction = 'RIGHT'
    change_to = direction
    bait_pos = [random.randrange(1, int(width / 10)) * 10, random.randrange(1, int(height / 10)) * 10]
    score = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_p:
                pause()
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if direction == 'LEFT':
        snake_head[0] -= 10
    if direction == 'RIGHT':
        snake_head[0] += 10
    if direction == 'UP':
        snake_head[1] -= 10
    if direction == 'DOWN':
        snake_head[1] += 10
    snake_body.insert(0, list(snake_head))
    if eat_bait(snake_head, bait_pos):
        score += 1
        bait_position()
    else:
        snake_body.pop()
    window.fill((0, 0, 0))
    draw_grid()
    if snake_collision(snake_head, snake_body):
        game_over()
    our_snake(snake_block, snake_body)
    pygame.draw.rect(window, bait_color, [bait_pos[0], bait_pos[1], bait_width, bait_height])
    our_score(score)
    pygame.display.update()
    clock.tick(snake_speed)
