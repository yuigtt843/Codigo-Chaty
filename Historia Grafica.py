import pygame
import sys

pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Historia de Johnny")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuente
font = pygame.font.Font(None, 36)

# Función para mostrar texto en pantalla
def draw_text(surface, text, font, color, x, y, max_width):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x_offset, y_offset = x, y
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x_offset + word_width >= max_width:
                x_offset = x
                y_offset += word_height
            surface.blit(word_surface, (x_offset, y_offset))
            x_offset += word_width + space
        x_offset = x
        y_offset += word_height

# Historia
history = {
    "start": {
        "text": "Un día Johnny jugando y corretiando por el mercado central de su pueblo, "
                "en un momento de su día Johnny tenía demasiada hambre pero no tenía dinero para comprar algo de comer, "
                "hasta que vio unas deliciosas donas que vendía un señor.\n\n"
                "1. Johnny prefiere mejor irse a su casa y esperar a ver qué preparó su madre de comer.\n"
                "2. Johnny decide robar una dona y correr y tratar de no ser atrapado.",
        "choices": {
            "1": "home",
            "2": "steal"
        }
    },
    "home": {
        "text": "Johnny llega a su casa y su madre lo está esperando con una gran olla de delicioso Pepian.\n\n"
                "Johnny después de comerse toda la olla de Pepian decide tomar una siesta.",
        "choices": {
            "1": "wake_up",
            "2": "wake_up"
        }
    },
    "steal": {
        "text": "Atrapan a Johnny y lo golpean y lo dejan tirado en el piso golpeado.\n\n"
                "La madre de Johnny lo estaba esperando con un delicioso Pepian pero al verlo golpeado y todo ella también lo golpea.\n\n"
                "Johnny se queda dormido de lo cansado que estaba.",
        "choices": {
            "1": "wake_up",
            "2": "wake_up"
        }
    },
    "wake_up": {
        "text": "Johnny se despierta a las 3 am pero se le fue el sueño pero recuerda que tiene que ir a la escuela esa misma mañana.\n\n"
                "1. Johnny decide poner su serie y ver los últimos capítulos que le quedaban.\n"
                "2. Johnny decide tomar una pasinerva para lograr retomar el sueño y relajarse y así volverse a dormir.",
        "choices": {
            "1": "watch_series",
            "2": "take_pill"
        }
    },
    "watch_series": {
        "text": "Johnny se quedó dormido y el bus que lo pasa a traer todas las mañanas lo dejó.\n\n"
                "Johnny llega a la escuela en una camioneta Esmeralda y ve a todos estresados por el parcial que va a pasar la maestra de Matemáticas.\n\n"
                "1. Johnny decide confiar en sus conocimientos y estar preparado para todo.\n"
                "2. Johnny decide hacer un chivo para el parcial porque no se recuerda de nada.",
        "choices": {
            "1": "confident",
            "2": "cheat"
        }
    },
    "take_pill": {
        "text": "Johnny se despierta con una hora de anticipación y se recuerda de que tiene parcial de matemáticas hoy y mientras va en el bus que lo pasa a traer en la mañana se pone a estudiar y llega listo al examen.\n\n"
                "En una pregunta Bonus del examen que decía que si la respuesta era correcta le podían aumentar su Zona a 60 puntos, la pregunta era: ¿Cuál es el nombre de la perrita de la maestra?\n\n"
                "1. La perrita se llama Abril.\n"
                "2. La perrita se llama Nicky.",
        "choices": {
            "1": "wrong_answer",
            "2": "correct_answer"
        }
    },
    "confident": {
        "text": "Johnny ve al profesor y él se acerca y le dice que le cae muy bien y le regaló varias respuestas del examen.\n\nFIN",
        "choices": {}
    },
    "cheat": {
        "text": "El profesor vio a Johnny con el chivo y le quitó el examen y ahora solo le queda a Johnny depender de la zona y las tareas que entregó.\n\n"
                "Johnny se encuentra a su madre al final del examen y él sabe que sacó 0.\n\n"
                "1. Johnny decide correr a la montaña para que su madre no lo regañe.\n"
                "2. Johnny decide mostrarle el examen a su madre y serle honesto.",
        "choices": {
            "1": "run_away",
            "2": "be_honest"
        }
    },
    "wrong_answer": {
        "text": "La respuesta es incorrecta y Johnny no se pudo ganar los puntos extras.\n\n"
                "Johnny llega a su casa y piensa en decirle a su madre o no de lo que pasó hoy.\n\n"
                "1. Johnny le cuenta a su madre que le fue bien en el examen.\n"
                "2. Johnny decide quedarse callado e irse a su cuarto, se toma una pasinerva y se queda dormido.",
        "choices": {
            "1": "tell_mother",
            "2": "stay_silent"
        }
    },
    "correct_answer": {
        "text": "La respuesta es correcta y Johnny tiene la mejor nota de su clase.\n\n"
                "Johnny llega a su casa y piensa en decirle a su madre o no de lo que pasó hoy.\n\n"
                "1. Johnny le cuenta a su madre que le fue bien en el examen.\n"
                "2. Johnny decide quedarse callado e irse a su cuarto, se toma una pasinerva y se queda dormido.",
        "choices": {
            "1": "tell_mother",
            "2": "stay_silent"
        }
    },
    "tell_mother": {
        "text": "Su madre lo felicita y le dice que lo quiere invitar a comer al lugar que más le gusta que son los Tacos del Yorch.\n\nFIN",
        "choices": {}
    },
    "stay_silent": {
        "text": "Johnny decide quedarse callado e irse a su cuarto, se toma una pasinerva y se queda dormido.\n\nFIN",
        "choices": {}
    },
    "run_away": {
        "text": "Johnny tropieza con una roca y se cae y se golpea la cabeza y queda desmayado. Después de varias horas desmayado se despierta en un lugar que no conoce y empieza una nueva vida como un superviviente en la selva.\n\nFIN",
        "choices": {}
    },
    "be_honest": {
        "text": "Su madre le dice que no se preocupe y le da un abrazo y le dice que lo ama mucho. Después su madre lo lleva a comer pepian al Comedor La Bendición cerca de su casa y son felices.\n\nFIN",
        "choices": {}
    }
}

current_scene = "start"

# Función principal
def main():
    global current_scene
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and "1" in history[current_scene]["choices"]:
                    current_scene = history[current_scene]["choices"]["1"]
                if event.key == pygame.K_2 and "2" in history[current_scene]["choices"]:
                    current_scene = history[current_scene]["choices"]["2"]

        screen.fill(BLACK)
        draw_text(screen, history[current_scene]["text"], font, WHITE, 20, 20, SCREEN_WIDTH - 40)
        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
