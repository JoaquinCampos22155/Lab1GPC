import pygame
import sys

pygame.init()

# Configurar pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rellenar Polígono")

poligono1 = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]

# Función para dibujar líneas 
def poligono_lineas(screen, points):
    for i in range(len(points)):
        pygame.draw.line(screen, (255, 255, 255), points[i], points[(i + 1) % len(points)], 1)

# Función para rellenar el polígono 
def poligono_llenar(screen, points):
    # Limites del polígono
    ymin = min(points, key=lambda p: p[1])[1]
    ymax = max(points, key=lambda p: p[1])[1]
    
    for y in range(ymin, ymax + 1):
        # Bordes del polígono
        intersecciones = []
        for i in range(len(points)):
            p1 = points[i]
            p2 = points[(i + 1) % len(points)]
            if p1[1] < p2[1]:
                y1, y2 = p1[1], p2[1]
                x1, x2 = p1[0], p2[0]
            else:
                y1, y2 = p2[1], p1[1]
                x1, x2 = p2[0], p1[0]
            if y1 <= y < y2:
                if y1 != y2:
                    x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                    intersecciones.append(int(x))
        intersecciones.sort()
        
        for i in range(0, len(intersecciones), 2):
            pygame.draw.line(screen, (255, 255, 255), (intersecciones[i], y), (intersecciones[i + 1], y))

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((1, 1, 1))
    
    poligono_lineas(screen, poligono1)
    poligono_llenar(screen, poligono1)
    
    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
