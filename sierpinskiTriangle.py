import pygame
import random

white = (255, 241, 232)
black = (0, 0, 0)
blue = (29, 43, 83)
cyan = (41, 173, 255)
brown = (171, 82, 54)
pink = (255, 0, 77)
gray = (95, 87, 79)
orange = (255, 163, 0)
lightpurple = (131, 118, 156)
darkpurple = (126, 37, 83)
lightgray = (194, 195, 199)
yellow = (255, 236, 39)
lightpink = (255, 119, 168)
darkgreen = (0, 135, 81)
lightgreen = (0, 228, 54)
skin = (255, 204, 170)

width = 1920
height = 1020
tam = 2
distancia = .5

n = 0 #3 vertices

try:
    pygame.init()
except:
    print("Não foi possível iniciar o programa.")
    exit(1)

back = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chaos Game")

#Desenhar os Pontos na tela
def drawPoint(cor, x, y):
    pygame.draw.rect(back, cor, [x, y, tam, tam])

#Loop do jogo
def loop(current, points):
    cont = 0
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(1)
        
        for i in range(100):
            new = random.randint(0, n+2)
                
            current[0] = int((current[0] + points[new][1][0])*distancia)
            current[1] = int((current[1] + points[new][1][1])*distancia)
            drawPoint(points[new][0], current[0], current[1])
        
        cont +=1

        pygame.display.update()

        if cont == 1000:
            return

#Definir os pontos iniciais
def chaos():
    back.fill(gray)

    points = [[cyan], [yellow], [lightgreen]]
    current = [0,0]

    '''
    positions = [[(width/2 - tam, 0), (0, height - tam), (width - tam, height - tam)], 
        [(0, 0), (width - tam, 0), (0, height - tam), (width - tam, height - tam)]]
    
    for i in range(n+3):
        points[i].append(positions[n][i])
        drawPoint(points[i][0], points[i][1][0], points[i][1][1])

    '''

    tupla1 = (random.randrange(0, width-tam, tam), random.randrange(0, height-tam))
    points[0].append(tupla1)
    drawPoint(points[0][0], points[0][1][0], points[0][1][1])

    tupla2 = (random.randrange(0, width-tam, tam), random.randrange(0, height-tam))
    points[1].append(tupla2)
    drawPoint(points[1][0], points[1][1][0], points[1][1][1])

    tupla3 = (random.randrange(0, width-tam, tam), random.randrange(0, height-tam))
    points[2].append(tupla3)
    drawPoint(points[2][0], points[2][1][0], points[2][1][1])

    current[0] = random.randrange(0, width-tam, tam)
    current[1] = random.randrange(0, height-tam, tam)
    drawPoint(orange, current[0], current[1])

    loop(current, points)

while(1):
    chaos()