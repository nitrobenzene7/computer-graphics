import pygame

pygame.init()
screen = pygame.display.set_mode((1200,720))
running =True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36) 

def draw_line(x1, y1, x2, y2, thickness):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1

    if dx > dy:
        err = dx / 2.0
        while x != x2:
            pygame.draw.circle(screen, WHITE, (x, y), thickness // 2)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            pygame.draw.circle(screen, WHITE, (x, y), thickness // 2)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    pygame.draw.circle(screen, WHITE, (x, y), thickness // 2)

def midPointAlgo(xinp, yinp, r):
    x = 0
    y = r
    p = 1-r
    while x<=y:
        screen.set_at((y + xinp, x + yinp),"white")
        screen.set_at((x + xinp ,y + yinp ),"white")
        screen.set_at((x + xinp, -y + yinp),"white")
        screen.set_at((y + xinp, -x + yinp),"white")
        screen.set_at((-y + xinp, -x + yinp),"white")
        screen.set_at((-x + xinp, -y + yinp),"white")
        screen.set_at((-x + xinp, y + yinp),"white")

        screen.set_at((-y + xinp, x + yinp),"white")
        


        
        x+=1
        if p<0:
            p+=2*x+1
        else:
            y-=1
            p+=2*(x-y)+1

    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    #midPointAlgo(int(1200/2), int(720/2) ,50)
    midPointAlgo(int(430), int(360) ,50)
    midPointAlgo(int(540), int(360) ,50)
    midPointAlgo(int(650), int(360) ,50)

    midPointAlgo(int(480), int(410) ,50)
    midPointAlgo(int(600), int(410) ,50)
    draw_line(430, 360, 540, 360, 3)
    draw_line(540, 360, 650, 360, 3)  
    draw_line(480, 410, 600, 410, 3)
    draw_line(430, 360, 480, 410, 3)
    draw_line(650, 360, 600, 410, 3)


    
    text_content = ""
    font2 = pygame.font.SysFont(text_content, 72)
   
    img2 = font2.render(text_content, True, ("lightsteelblue4"))


    text_width, text_height = font.size(text_content)
    text_x = 50 // 2 - text_width // 2
    text_y = 50 // 2 - text_height // 2

# Blit text onto the screen
    screen.blit(img2,(510,415))

    pygame.display.update()

pygame.quit()
