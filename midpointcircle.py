import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 720))
running = True

def midPointAlgo(xinp, yinp, r):
    x = 0
    y = r
    p = 1 - r
    while x <= y:
        # Drawing only the white color
        screen.set_at((y + xinp, x + yinp), "white")
        screen.set_at((x + xinp, y + yinp), "white")
        screen.set_at((x + xinp, -y + yinp), "white")
        screen.set_at((y + xinp, -x + yinp), "white")
        screen.set_at((-y + xinp, -x + yinp), "white")
        screen.set_at((-x + xinp, -y + yinp), "white")
        screen.set_at((-x + xinp, y + yinp), "white")
        screen.set_at((-y + xinp, x + yinp), "white")

        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    midPointAlgo(int(1200 / 2), int(720 / 2), 50)
    # midPointAlgo(int(660), int(360), 50)
    # midPointAlgo(int(540), int(360), 50)
    # midPointAlgo(int(480), int(360), 50)

    # text_content = "AUDI"
    # font2 = pygame.font.SysFont(text_content, 72)
    # img2 = font2.render(text_content, True, ("lightsteelblue4"))

    # text_width, text_height = font.size(text_content)
    # text_x = 50 // 2 - text_width // 2
    # text_y = 50 // 2 - text_height // 2

    # Blit text onto the screen
    # screen.blit(img2, (510, 415))

    pygame.display.update()

pygame.quit()
