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
    {"question": "¿Capital de Francia?", "options": ["París", "Londres", "Madrid"], "answer": 0},
    {"question": "¿2 + 2?", "options": ["3", "4", "5"], "answer": 1},
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
        question_data = questions[current_question]
        question = question_data["question"]
        options = question_data["options"]
        correct_option = question_data["answer"]
        option_height = SCREEN_HEIGHT // 3
        obstacles.append({
            "x": SCREEN_WIDTH,
            "y": [0, option_height, option_height * 2],
            "options": options,
            "correct": correct_option,
            "limits": [
                option_height,
                2 * option_height,
                3 * option_height
            ]
        })

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main():
    global bird_y, bird_y_velocity, obstacles, current_question

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
                current_question += 1
                if current_question >= len(questions):
                    current_question = 0
                generate_obstacle()

            # Draw the obstacle with limits
            for i in range(3):
                color = GREY
                height = SCREEN_HEIGHT // 3
                pygame.draw.rect(screen, color, (obstacle["x"], obstacle["y"][i], obstacle_width, height))
                # Draw the options
                draw_text(obstacle["options"][i], font, BLACK, screen, obstacle["x"] + 10, obstacle["y"][i] + height // 2 - 18)

            # Mark the passage limit
            for limit in obstacle["limits"]:
                pygame.draw.line(screen, GREEN, (obstacle["x"], limit), (obstacle["x"] + obstacle_width, limit), 5)

            # Check for collision
            if bird_x + bird_size > obstacle["x"] and bird_x < obstacle["x"] + obstacle_width:
                correct_limit = obstacle["limits"][obstacle["correct"]]
                if bird_y < correct_limit - obstacle_gap // 2 or bird_y > correct_limit + obstacle_gap // 2:
                    reset_game()

        pygame.draw.rect(screen, BLACK, (bird_x, bird_y, bird_size, bird_size))

        if current_question < len(questions):
            question = questions[current_question]["question"]
            draw_text(question, font, BLACK, screen, 20, 20)

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
