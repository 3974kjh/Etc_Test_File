from datetime import datetime
import pygame, sys
import time

SIZE = width,height = 640,240

screen = pygame.display.set_mode(SIZE)
screen.fill((0,0,0))
pygame.init()

# Text Editing

text1 = 'admin'
font1 = pygame.font.Font('freesansbold.ttf',20)
img1 = font1.render(text1,True,(255,255,255))

rect1 = img1.get_rect()
rect1.topleft = (width//2 - 75,120)
cursor1 = pygame.Rect(rect1.topright,(3,rect1.height))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(text1)> 0:
                    text1 = text1[:-1]
            elif len(text1) == 10:
                break
            elif event.key == pygame.K_SPACE:
                sys.exit()
            else:
                text1 += event.unicode

            img1 = font1.render(text1,True,(255,255,255))
            rect1.size = img1.get_size()
            cursor1.topleft = rect1.topright

    screen.fill((0,0,0))
    screen.blit(img1,rect1)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, (255,255,0), cursor1)
    pygame.draw.rect(screen, (0,255,0), (width//2 - 75, 120, 150, 30), 3)
    pygame.display.update()

pygame.quit()