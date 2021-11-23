import random
import copy
import pygame
import matrix2d_read_v2 as m2d

pygame.init()
WIDTH = 1000
SIZE = 100
screen = pygame.display.set_mode((WIDTH, WIDTH))


#probablity = 0.59275
probablity = 0.59275

matrix = []

for y in range(SIZE):
	matrix.append([])
	for x in range(SIZE):
		if random.random() < probablity:
			matrix[y].append(1)
		else:
			matrix[y].append(0)
		if y == 0 and matrix[y][x] == 1:
			matrix[y][x] = 5

matrix = m2d.Matrix2d(matrix).return_new()

while 1:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()

	screen.fill((255, 255, 255))
	for y in range(len(matrix)):
		for x in range(len(matrix[y])):
			if matrix[y][x] == 5:
				pygame.draw.rect(screen, (0, 0, 255), (x*WIDTH/SIZE, y*WIDTH/SIZE, WIDTH/SIZE, WIDTH/SIZE))
			elif matrix[y][x] == 1:
				pygame.draw.rect(screen, (255, 0, 0), (x*WIDTH/SIZE, y*WIDTH/SIZE, WIDTH/SIZE, WIDTH/SIZE))

			pygame.draw.rect(screen, (0, 0, 0), (x*WIDTH/SIZE, y*WIDTH/SIZE, WIDTH/SIZE, WIDTH/SIZE), 1)

	pygame.display.update()