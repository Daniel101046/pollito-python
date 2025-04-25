import pygame
import random
import time

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255,255,0)
GRISOSCURO = (80, 81, 81)
CAFE = (125, 33, 0)

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("El Pollo Cruza las Carreteras")

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Configuración del pollo
pollo_ancho = 25
pollo_alto = 25
pollo_x = ANCHO // 2 - pollo_ancho // 2
pollo_y = ALTO - pollo_alto - 10
pollo_velocidad = 5

# Configuración de las carreteras
carro_ancho = 25
carro_alto = 25
carro_velocidad = 3.5
carros = []

# Posiciones de las 4 carreteras horizontales
carretera1_y = ALTO // 5
carretera2_y = 2 * ALTO // 3
carretera3_y = 3 * ALTO // 5
carretera4_y = 4 * ALTO // 15

# Número de vidas
vidas = 3

# Fuente para mostrar el marcador de vidas
fuente = pygame.font.SysFont("Arial", 25)

# Función para dibujar el pollo
def dibujar_pollo(x, y):
    pygame.draw.rect(screen, AMARILLO, (x, y, pollo_ancho, pollo_alto))

# Función para dibujar los carros
def dibujar_carros(carros):
    for carro in carros:
        pygame.draw.rect(screen, ROJO, carro)

# Función para crear nuevos carros
def crear_carro(y):
    x = -carro_ancho  # Comienza fuera de la pantalla (de izquierda a derecha)
    return pygame.Rect(x, y, carro_ancho, carro_alto)

# Función para reiniciar el juego
def reiniciar_juego():
    global pollo_x, pollo_y, carros
    pollo_x = ANCHO // 2 - pollo_ancho // 2
    pollo_y = ALTO - pollo_alto - 10
    carros = []

# Función para dibujar el marcador de vidas
def dibujar_vidas(vidas):
    texto = fuente.render(f'Vidas: {vidas}', True, NEGRO)
    screen.blit(texto, (9,9))  # Mostrar en la esquina superior izquierda

# Función principal del juego
def juego():
    global pollo_x, pollo_y, carros, vidas
    game_over = False
    while not game_over:
        screen.fill(BLANCO)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Movimiento del pollo
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and pollo_x > 0:
            pollo_x -= pollo_velocidad
        if keys[pygame.K_RIGHT] and pollo_x < ANCHO - pollo_ancho:
            pollo_x += pollo_velocidad
        if keys[pygame.K_UP] and pollo_y > 0:
            pollo_y -= pollo_velocidad
        if keys[pygame.K_DOWN] and pollo_y < ALTO - pollo_alto:
            pollo_y += pollo_velocidad

        # Crear nuevos carros y mover los existentes
        if random.random() < 0.08:  # Probabilidad de crear un carro
            carretera = random.choice([carretera1_y, carretera2_y, carretera3_y, carretera4_y])  # El carro aparecerá en una de las dos carreteras
            carros.append(crear_carro(carretera))
        
        for carro in carros:
            carro.x += carro_velocidad  # Los carros se mueven hacia la derecha
            if carro.x > ANCHO:  # Si el carro se sale de la pantalla, lo eliminamos
                carros.remove(carro)

        # Comprobar colisiones
        pollo_rect = pygame.Rect(pollo_x, pollo_y, pollo_ancho, pollo_alto)
        for carro in carros:
            if pollo_rect.colliderect(carro):
                vidas -= 1  # Restar una vida
                reiniciar_juego()
                time.sleep(1)  # Pausa breve antes de reiniciar

        # Comprobar si las vidas llegaron a 0
        if vidas <= 0:
            game_over = True  # Termina el juego cuando no hay más vidas

        # Dibujar las carreteras
        pygame.draw.rect(screen, GRISOSCURO, (0, carretera1_y - 10, ANCHO, 40)) 
        pygame.draw.rect(screen, GRISOSCURO, (0, carretera2_y - 10, ANCHO, 40)) 
        pygame.draw.rect(screen, GRISOSCURO, (0, carretera3_y - 10, ANCHO, 40))
        pygame.draw.rect(screen, GRISOSCURO, (0, carretera4_y - 10, ANCHO, 40))
        pygame.draw.rect(screen, CAFE, (110,30, 50, 50))
        pygame.draw.rect(screen, CAFE, (210,30, 50, 50))
        pygame.draw.rect(screen, CAFE, (310,30, 50, 50))
        pygame.draw.rect(screen, CAFE, (410,30, 50, 50))
        pygame.draw.rect(screen, CAFE, (510,30, 50, 50))
        pygame.draw.rect(screen, CAFE, (610,30, 50, 50))
        pygame.draw.rect(screen, CAFE, (710,30, 50, 50))
        pygame.draw.rect(screen, CAFE, (110,500, 50, 50))
        pygame.draw.rect(screen, CAFE, (210,500, 50, 50))
        pygame.draw.rect(screen, CAFE, (310,500, 50, 50))
        pygame.draw.rect(screen, CAFE, (410,500, 50, 50))
        pygame.draw.rect(screen, CAFE, (510,500, 50, 50))
        pygame.draw.rect(screen, CAFE, (610,500, 50, 50))
        pygame.draw.rect(screen, CAFE, (710,500, 50, 50))

        # Dibujar el pollo y los carros
        dibujar_pollo(pollo_x, pollo_y)
        dibujar_carros(carros)

        # Dibujar el marcador de vidas
        dibujar_vidas(vidas)

        # Actualizar la pantalla
        pygame.display.update()

        # Controlar los FPS
        clock.tick(60)

# Iniciar el juego
juego()

# Salir de Pygame
pygame.quit()