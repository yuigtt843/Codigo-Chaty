import pygame
import sys
import random

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Real vs Barca")

real_madrid_img = pygame.image.load("real_madrid.png")
barcelona_img = pygame.image.load("barcelona.png")

real_madrid_img = pygame.transform.scale(real_madrid_img, (50, 50))
barcelona_img = pygame.transform.scale(barcelona_img, (50, 50))

background_color = (100, 0, 0)

square_size = 50
x = width // 2 - square_size // 2
y = height // 2 - square_size // 2

speed = 7 
target_speed = 3 
running = True

targets = []
projectiles = []  

score = 0

font = pygame.font.Font(None, 36)

class Projectile:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.speed = 5

    def update(self):
        self.rect.x += self.speed

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                projectiles.append(Projectile(x + square_size // 2, y + square_size // 2))

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
        target_y = random.randint(0, height - target_size)
        targets.append(pygame.Rect(width, target_y, target_size, target_size))
    
    for target in targets[:]:
        target.x -= target_speed
        if target.right < 0:
            targets.remove(target)
        if pygame.Rect(x, y, square_size, square_size).colliderect(target):
            running = False
            break
    
    for projectile in projectiles[:]:
        projectile.update()
        if projectile.rect.x > width:
            projectiles.remove(projectile)
        for target in targets[:]:
            if projectile.rect.colliderect(target):
                targets.remove(target)
                projectiles.remove(projectile)
                score += 1
    
    screen.fill(background_color)
    
    screen.blit(real_madrid_img, (x, y))
    
    for target in targets:
        screen.blit(barcelona_img, target)
    
    for projectile in projectiles:
        pygame.draw.rect(screen, (255, 255, 255), projectile.rect)  
    
    text = font.render(f"Puntuación: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
