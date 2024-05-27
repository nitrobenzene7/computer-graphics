import pygame


pygame.init()

#defining colors
WIDTH, HEIGHT = 1900/2, 1700/2
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.draw.circle(screen, YELLOW, (WIDTH // 2, HEIGHT // 2), 50)
pygame.draw.circle(screen, BLUE, (WIDTH // 2 + 100, HEIGHT // 2), 20)
pygame.draw.circle(screen, GREEN, (WIDTH // 2 + 200, HEIGHT // 2), 15)
pygame.draw.circle(screen, ORANGE, (WIDTH // 2 + 300, HEIGHT // 2), 10)
pygame.draw.circle(screen, RED, (WIDTH // 2 + 400, HEIGHT // 2), 5)


pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 100, 1)
pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 200, 1)
pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 300, 1)
pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 400, 1)


pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()