import random
import pygame

# Initialize pygame
pygame.init()

# Define colors (RGB)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Window dimensions
WIDTH = 1000
HEIGHT = 700

# Initialize screen and title
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Pygame Edition")

# Clock to control game speed
clock = pygame.time.Clock()

# Snake settings
BLOCK_SIZE = 20
SNAKE_SPEED = 8  # Slower speed

# Fonts for score and messages
font_style = pygame.font.SysFont("bahnschrift", 22)
score_font = pygame.font.SysFont("comicsansms", 22)


def display_score(score):
  """Displays the current score on the screen."""
  value = score_font.render(f"Score: {score}", True, YELLOW)
  screen.blit(value, [10, 10])


def draw_snake(block_size, snake_list):
  """Draws each segment of the snake."""
  for x in snake_list:
    pygame.draw.rect(screen, GREEN, [x[0], x[1], block_size, block_size])
    pygame.draw.rect(screen, BLACK, [x[0], x[1], block_size, block_size], 1)


def show_message(msg, color):
  """Displays game over messages."""
  mesg = font_style.render(msg, True, color)
  screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])


def game_loop():
  game_over = False
  game_close = False

  # Starting coordinates of the snake (aligned to grid)
  x1 = (WIDTH // 2 // BLOCK_SIZE) * BLOCK_SIZE
  y1 = (HEIGHT // 2 // BLOCK_SIZE) * BLOCK_SIZE

  # Movement changes per frame
  x1_change = 0
  y1_change = 0

  snake_list = []
  snake_length = 1

  # Clean grid-aligned random initial food position
  foodx = random.randrange(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE
  foody = random.randrange(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE

  while not game_over:

    while game_close:
      screen.fill(BLUE)
      show_message("You Lost! Press C-Play Again or Q-Quit", RED)
      display_score(snake_length - 1)
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
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and x1_change == 0:
          x1_change = -BLOCK_SIZE
          y1_change = 0
        elif event.key == pygame.K_RIGHT and x1_change == 0:
          x1_change = BLOCK_SIZE
          y1_change = 0
        elif event.key == pygame.K_UP and y1_change == 0:
          y1_change = -BLOCK_SIZE
          x1_change = 0
        elif event.key == pygame.K_DOWN and y1_change == 0:
          y1_change = BLOCK_SIZE
          x1_change = 0

    if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
      game_close = True

    x1 += x1_change
    y1 += y1_change

    # Food collision check (now guaranteed to match grid steps)
    if x1 == foodx and y1 == foody:
      foodx = random.randrange(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE
      foody = random.randrange(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE
      snake_length += 1

    screen.fill(BLUE)
    pygame.draw.rect(screen, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])

    snake_head = [x1, y1]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
      del snake_list[0]

    for x in snake_list[:-1]:
      if x == snake_head:
        game_close = True

    draw_snake(BLOCK_SIZE, snake_list)
    display_score(snake_length - 1)

    pygame.display.update()
    clock.tick(SNAKE_SPEED)

  pygame.quit()
  quit()


if __name__ == "__main__":
  game_loop()