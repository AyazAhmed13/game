import pygame
import random
import sys
print('starting...')

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Player
player_width = 100
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 8

# Object
object_width = 30
object_height = 30
object_x = random.randint(0, WIDTH - object_width)
object_y = 0
object_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_width, player_height))

def draw_object(x, y):
    pygame.draw.rect(screen, RED, (x, y, object_width, object_height))

def show_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

def game_over():
    screen.fill(WHITE)
    over_text = font.render("Game Over! Final Score: " + str(score), True, BLACK)
    screen.blit(over_text, (WIDTH//2 - 150, HEIGHT//2))
    pygame.display.update()
    pygame.time.wait(3000)

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # Add this block
            if event.key == pygame.K_ESCAPE:  # Quit on ESC key
                running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    
    # Object movement
    object_y += object_speed
    if object_y > HEIGHT:
        object_y = 0
        object_x = random.randint(0, WIDTH - object_width)
    
    # Collision detection
    if (player_y < object_y + object_height and
        player_y + player_height > object_y and
        player_x < object_x + object_width and
        player_x + player_width > object_x):
        score += 1
        object_y = 0
        object_x = random.randint(0, WIDTH - object_width)
        object_speed += 0.5  # Increase difficulty
    
    draw_player(player_x, player_y)
    draw_object(object_x, object_y)
    show_score()
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
