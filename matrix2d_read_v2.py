import copy
#import stroke checker
import stroke_read_v2 as sr

class Matrix2d:
	def __init__(self, matrix):
		#init variables
		self.matrix = matrix
	def return_new(self):
		#init matrix
		start_matrix = []

		#start cycle, if last matrix != start matrix => next loop
		while start_matrix != self.matrix:
			#copy matrix 
			start_matrix = copy.deepcopy(self.matrix)
			#go throught 2d matrix
			for y in range(len(self.matrix)):
				#calculate now stroke
				stroke = sr.MatrixStroke(self.matrix[y])
				self.matrix[y] = stroke.return_new()
				#go throught stroke
				for x in range(len(self.matrix[y])):
					#if now element is +charge
					if self.matrix[y][x] == 5:
						#if up element is copper
						if self.matrix[max(0, y - 1)][x] == 1:
							#up element +charge
							self.matrix[max(0, y - 1)][x] = 5
						#if down element is copper
						if self.matrix[min(len(self.matrix[y]) - 1, y + 1)][x] == 1:
							#down element +charge
							self.matrix[min(len(self.matrix[y]) - 1, y + 1)][x] = 5

				for y in range(len(self.matrix) - 1, -1, -1):
					#calculate now stroke
					stroke = sr.MatrixStroke(self.matrix[y])
					self.matrix[y] = stroke.return_new()
					#go throught stroke
					for x in range(len(self.matrix[y])):
						#if now element is +charge
						if self.matrix[y][x] == 5:
							#if up element is copper
							if self.matrix[max(0, y - 1)][x] == 1:
								#up element +charge
								self.matrix[max(0, y - 1)][x] = 5
							#if down element is copper
							if self.matrix[min(len(self.matrix[y]) - 1, y + 1)][x] == 1:
								#down element +charge
								self.matrix[min(len(self.matrix[y]) - 1, y + 1)][x] = 5
		return self.matrix