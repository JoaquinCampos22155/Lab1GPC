import pygame
import sys

pygame.init()

# Configurar pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rellenar Polígono")

poligono1 = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]
poligono2 = [(321, 335), (288, 286), (339, 251), (374, 302)]
poligono3 = [(377, 249), (411, 197), (436, 249)]
poligono4 = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),
             (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),
             (597, 215), (552, 214), (517, 144), (466, 180)]
poligono5 = [(682, 175), (708, 120), (735, 148), (739, 170)]

# Función para dibujar líneas 
def poligono_lineas(screen, points):
    for i in range(len(points)):
        pygame.draw.line(screen, (255, 255, 255), points[i], points[(i + 1) % len(points)], 1)

# Función para rellenar el polígono 
def poligono_llenar(screen, points, color):
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
            pygame.draw.line(screen, color, (intersecciones[i], y), (intersecciones[i + 1], y))

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((1, 1, 1))
    
    poligono_lineas(screen, poligono1)
    poligono_llenar(screen, poligono1, (225, 225, 225))  
    poligono_lineas(screen, poligono2)
    poligono_llenar(screen, poligono2, (225, 225, 225))  
    poligono_lineas(screen, poligono3)
    poligono_llenar(screen, poligono3, (225, 225, 225))  
    poligono_lineas(screen, poligono4)
    poligono_llenar(screen, poligono4, (225, 225, 225))  
    poligono_lineas(screen, poligono5)
    poligono_llenar(screen, poligono5, (2.5, 2.5, 2.5))  
    
    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
