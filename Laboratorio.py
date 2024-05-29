import pygame
import sys
import random

pygame.init()

width, height = 800, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Real vs Barca")

real_madrid_img = pygame.image.load("real_madrid.png")
barcelona_img = pygame.image.load("barcelona.png")

real_madrid_img = pygame.transform.scale(real_madrid_img, (50, 50))
barcelona_img = pygame.transform.scale(barcelona_img, (50, 50))

background_color = (0, 0, 0)

square_size = 50
x = width // 2 - square_size // 2
y = height // 2 - square_size // 2

speed = 5

running = True

targets = []

bullets = []  

score = 0

font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                bullets.append(pygame.Rect(x + square_size, y + square_size // 2, 10, 5)) 
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed
    
    if x < 0:
        x = 0
    elif x + square_size > width:
        x = width - square_size
    if y < 0:
        y = 0
    elif y + square_size > height:
        y = height - square_size
    
    if random.randint(0, 100) < 3:
        target_size = random.randint(20, 40)
        target_x = width
        target_y = random.randint(0, height - target_size)
        targets.append((target_x, target_y))
    
    for target in targets[:]:
        target_rect = pygame.Rect(target[0], target[1], barcelona_img.get_width(), barcelona_img.get_height())
        if target_rect.colliderect(pygame.Rect(x, y, square_size, square_size)):
            running = False 
            break
        for bullet in bullets:  
            if target_rect.colliderect(bullet):
                targets.remove(target)
                score += 1
                bullets.remove(bullet)  
    
    screen.fill(background_color)
    
    screen.blit(real_madrid_img, (x, y))
    
    for target in targets:
        screen.blit(barcelona_img, (target[0], target[1]))
    
    for bullet in bullets:  # Dibujar todos los disparos
        pygame.draw.rect(screen, (255, 255, 255), bullet)
    
    pygame.display.flip()
    
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
