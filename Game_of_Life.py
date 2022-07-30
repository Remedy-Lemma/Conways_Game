# # John Conway's game of life
import pygame
import numpy
from time import sleep
# # matrix represents a grid, 0s are dead cells and 1s are live
# 0s become 1s if they have three live neighbours
# 1s become 0s if they have >3 or <2 live neighbours

matriss = [] ; cellstates = [] # matriss is the grid, cellstates is the next frame

# Creates a 2s array of 0s given its dimensions
def grid(width, height):
    i = j = 0 ; wideln = [] ; global matriss

    while i < width:
        wideln.append(0)
        i += 1

    while j < height:
       matriss.append(list(wideln))
       j += 1

# Fills in the screen with black and white cells according to the 2d array
def griddraw():
    i = j = 0 ; global matriss, cellstates
    matriss = duplicate(cellstates)

    for row in matriss:
        i = 0
        for cell in row:
            if cell == 0 and screen.get_at((1+25*i, 1+25*j))[:3] == (255,255,255):
                pygame.draw.rect(screen, (0,0,0), (1+25*i,1+25*j,23,23))

            elif cell == 1 and screen.get_at((1+25*i, 1+25*j))[:3] == (0,0,0):
                pygame.draw.rect(screen, (255,255,255), (1+25*i,1+25*j,23,23))
            i += 1
        j += 1
    

def duplicate(matrix):
    newmatrix = []
    for row in matrix:
        newline = []
        for cell in row:
            newline.append(cell)
        newmatrix.append(newline)

    return newmatrix

def logic():
    rown = celln = 0 ; global matriss, cellstates
    for row in matriss:
        for cell in row:
            live8 = 0

            # If the cell to the right exists
            if celln + 1 < len(row):
                if row[celln+1] == 1:
                    live8 += 1
                if rown - 1 >= 0 and matriss[rown-1][celln+1] == 1:
                    live8 += 1
                if rown + 1 < len(matriss) and matriss[rown+1][celln+1] == 1:
                    live8 += 1

            # If the cell to the left exists
            if celln - 1 >= 0:
                if matriss[rown][celln-1] == 1:
                    live8 += 1
                if rown - 1 >= 0 and matriss[rown-1][celln-1] == 1:
                    live8 += 1
                if rown + 1 < len(matriss) and matriss[rown+1][celln-1] == 1:
                    live8 += 1

            # If the cell above exists
            if rown - 1 >= 0:
                if matriss[rown-1][celln] == 1:
                    live8 += 1

            # If the cell below exists
            if rown + 1 < len(matriss):
                if matriss[rown+1][celln] == 1:
                    live8 += 1
            
            # Finally our condition
            if cell == 0 and live8 == 3:
                cellstates[rown][celln] = 1
            elif cell == 1 and live8 != 2 and live8 != 3:
                cellstates[rown][celln] = 0

            celln += 1
        celln = 0 
        rown += 1

# # TODO: Done woooooooo!!

pygame.init()

screen = pygame.display.set_mode([1300, 650])
screen.fill((200, 200, 200))
grid(1300/25, 650/25)

i = j = 0
for row in matriss:
    i = 0
    for cell in row:
        if cell == 0:
            pygame.draw.rect(screen, (0,0,0), (1+25*i,1+25*j,23,23))
        elif cell == 1:
            pygame.draw.rect(screen, (255,255,255), (1+25*i,1+25*j,23,23))
        i += 1
    j += 1

cellstates = duplicate(matriss)

running = True ; update = False
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and update == False:
            pos = pygame.mouse.get_pos() ; pis = 0  # Pis is so you only fill valid spots
            for coord in pos:

                if coord % 25 != 1: # See griddraw() for how this chunk gives the matrix indices
                    pis += 1

                if pis == 1:
                    column = int(numpy.floor(coord/25))

                if pis == 2:
                    row = int(numpy.floor(coord/25))

                    if cellstates[row][column] == 0:
                        cellstates[row][column] = 1
                        pygame.draw.rect(screen, (255,255,255), (1+25*column,1+25*row,23,23))
                    
                    else:
                        cellstates[row][column] = 0
                        pygame.draw.rect(screen, (0,0,0), (1+25*column,1+25*row,23,23))
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and update == True:
                update = False

            elif event.key == pygame.K_RETURN:
                mattress = numpy.array(matriss)
                update = True
            
    if update:
        logic()
        if cellstates == matriss:
            update = False

        griddraw()
        sleep(0.1)

        if numpy.all((mattress == 0)):
            update = False

    pygame.display.flip() # Updates entire screen. Slow, but the game is slow


# If you have any questions message me on discord: R. Emma-dy#8967
# This is my first pygame thing, it might be bad


# lines intentionally left blank :)