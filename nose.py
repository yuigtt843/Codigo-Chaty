import pygame
import sys
import random

pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Quiz Bird")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
GREEN = (0, 255, 0)

# Fuentes
font = pygame.font.Font(None, 36)

# Preguntas y respuestas
questions = [
    {"question": "¿Capital de Francia?", "options": ["3", "4", "5"], "answer": 1},
    {"question": "¿2 + 2?", "options": ["París", "Londres", "Madrid"], "answer": 1},
    {"question": "¿Color del cielo?", "options": ["Verde", "Azul", "Rojo"], "answer": 1},
    {"question": "¿Capital de España?", "options": ["Lisboa", "Madrid", "Roma"], "answer": 1},
    {"question": "¿5 * 6?", "options": ["11", "30", "25"], "answer": 1}
]

current_question = 0

# Bird
bird_size = 20
bird_x = 100
bird_y = SCREEN_HEIGHT // 2
bird_y_velocity = 0

# Obstacles
obstacle_width = 100
obstacle_gap = 175
obstacle_velocity = 4
obstacles = []

# Function to reset the game
def reset_game():
    global bird_y, bird_y_velocity, obstacles, current_question
    bird_y = SCREEN_HEIGHT // 2
    bird_y_velocity = 0
    obstacles = []
    current_question = 0
    generate_obstacle()

# Function to generate a new obstacle
def generate_obstacle():
    global obstacles, current_question
    if current_question < len(questions):
        correct_option = questions[current_question]["answer"]
        options = questions[current_question]["options"]
        obstacle_y = random.randint(100, SCREEN_HEIGHT - obstacle_gap - 100)
        obstacles.append({
            "x": SCREEN_WIDTH,
            "y": [0, obstacle_y + obstacle_gap // 2, SCREEN_HEIGHT],
            "options": options,
            "correct": correct_option,
            "limit": obstacle_y + obstacle_gap // 2
        })
        current_question += 1

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main():
    global bird_y, bird_y_velocity, obstacles

    clock = pygame.time.Clock()
    reset_game()

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_y_velocity = -8

        bird_y_velocity += 1
        bird_y += bird_y_velocity

        if bird_y > SCREEN_HEIGHT or bird_y < 0:
            reset_game()

        for obstacle in obstacles:
            obstacle["x"] -= obstacle_velocity

            if obstacle["x"] < -obstacle_width:
                obstacles.remove(obstacle)
                generate_obstacle()

            # Draw the obstacle with limits
            for i in range(3):
                color = GREY
                height = obstacle["y"][1] if i == 0 else SCREEN_HEIGHT - obstacle["y"][1] if i == 2 else SCREEN_HEIGHT
                pygame.draw.rect(screen, color, (obstacle["x"], obstacle["y"][i], obstacle_width, height))
                # Draw the options
                draw_text(obstacle["options"][i], font, BLACK, screen, obstacle["x"] + 10, obstacle["y"][i] + 10)

            # Mark the passage limit
            pygame.draw.line(screen, GREEN, (obstacle["x"], obstacle["limit"]), (obstacle["x"] + obstacle_width, obstacle["limit"]), 5)

            if bird_x + bird_size > obstacle["x"] and bird_x < obstacle["x"] + obstacle_width:
                if bird_y < obstacle["limit"] or bird_y > obstacle["limit"] + obstacle_gap:
                    reset_game()

        pygame.draw.rect(screen, BLACK, (bird_x, bird_y, bird_size, bird_size))

        if current_question < len(questions):
            draw_text(questions[current_question]["question"], font, BLACK, screen, 20, 20)

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
