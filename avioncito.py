import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuraciones de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Preguntas")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fuentes
font = pygame.font.Font(None, 36)

# Preguntas y opciones
questions = [
    {"question": "¿Cuál es la capital de Francia?", "options": ["Madrid", "París", "Berlín"], "answer": "París"},
    {"question": "¿Cuánto es 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
    {"question": "¿Cuál es el océano más grande?", "options": ["Atlántico", "Índico", "Pacífico"], "answer": "Pacífico"},
    {"question": "¿Quién escribió 'Cien años de soledad'?", "options": ["Mario Vargas Llosa", "Gabriel García Márquez", "Pablo Neruda"], "answer": "Gabriel García Márquez"},
    {"question": "¿Cuál es el planeta más cercano al sol?", "options": ["Venus", "Marte", "Mercurio"], "answer": "Mercurio"},
    {"question": "¿Cuál es el animal terrestre más rápido?", "options": ["León", "Guepardo", "Tigre"], "answer": "Guepardo"},
    {"question": "¿En qué año llegó el hombre a la luna?", "options": ["1965", "1969", "1972"], "answer": "1969"},
    {"question": "¿Cuál es el elemento químico con símbolo 'O'?", "options": ["Oro", "Oxígeno", "Osmio"], "answer": "Oxígeno"},
]

# Función para mostrar un mensaje en la pantalla
def show_message(message, color, y_displace=0):
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 + y_displace))
    screen.blit(text_surface, text_rect)

# Función principal del juego
def main():
    running = True
    current_question_index = 0
    questions_order = random.sample(range(len(questions)), len(questions))
    question_speed = 2  # Velocidad de movimiento de las preguntas y opciones

    while running:
        screen.fill(WHITE)

        # Movimiento del avión

        # Obtener la pregunta y opciones actuales
        current_question = questions[questions_order[current_question_index]]
        question_text = current_question["question"]
        options = current_question["options"]

        # Mostrar la pregunta y opciones
        show_message(question_text, BLACK, -200)
        question_rect = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 - 200, 400, 50)
        question_rect.x -= question_speed

        # Mostrar las opciones
        option_rects = []
        for i, option in enumerate(options):
            option_text = f"{i + 1}. {option}"
            show_message(option_text, BLACK, -50 + (i * 50))
            option_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50 + (i * 50), 200, 50)
            option_rect.x -= question_speed
            option_rects.append(option_rect)

        # Dibujar las paredes
        left_wall_rect = pygame.Rect(0, 0, 10, HEIGHT)
        right_wall_rect = pygame.Rect(WIDTH - 10, 0, 10, HEIGHT)
        pygame.draw.rect(screen, BLACK, left_wall_rect)
        pygame.draw.rect(screen, BLACK, right_wall_rect)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, option_rect in enumerate(option_rects):
                    if option_rect.collidepoint(mouse_pos):
                        selected_option = options[i]
                        if selected_option == current_question["answer"]:
                            current_question_index += 1
                            if current_question_index == len(questions):
                                screen.fill(WHITE)
                                show_message("¡Felicidades, has ganado!", GREEN)
                                pygame.display.flip()
                                pygame.time.wait(3000)
                                running = False
                        else:
                            screen.fill(WHITE)
                            show_message("Respuesta incorrecta. Volviendo al inicio...", RED)
                            pygame.display.flip()
                            pygame.time.wait(2000)
                            current_question_index = 0
                            questions_order = random.sample(range(len(questions)), len(questions))

        pygame.display.flip()

# Ejecutar el juego
if __name__ == "__main__":
    main()
    pygame.quit()
