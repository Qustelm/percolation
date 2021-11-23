import random
import copy
from tqdm import tqdm
import matrix2d_read_v2 as m2d

WIDTH = 500
SIZE = 1000


#probablity = 0.59275
probablity = 0.60

matrix = []

def check_matr():
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
	if 5 in matrix[len(matrix) - 1]:
		return True
	else:
		return False

result = []
fal = 0
tr = 0

for i in tqdm(range(10)):
	res = check_matr()

	if res == True:
		tr += 1
	else:
		fal += 1

print('False: ' + str(fal))
print('True: ' + str(tr))