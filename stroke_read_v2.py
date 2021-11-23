import copy
class MatrixStroke:
	#init variables
	def __init__(self, stroke):
		self.stroke = stroke
	def return_new(self):
		#init stroke
		start_stroke = []
		#start cycle, if last stroke != start stroke => next loop
		while start_stroke != self.stroke:
			#copy stroke
			start_stroke = copy.copy(self.stroke)
			#go throught stroke
			for i in range(len(start_stroke)):
				#if now element is + charge
				if self.stroke[i] == 5:
					#if left element is copper
					if self.stroke[max(0, i - 1)] == 1:
						#he + charge
						self.stroke[i - 1] = 5

					#if right element is copper
					if self.stroke[min(i + 1, len(self.stroke) - 1)] == 1:
						#he + charge
						self.stroke[i + 1] = 5
			for i in range(len(start_stroke) - 1, -1, -1):
				#if now element is + charge
				if self.stroke[i] == 5:
					#if left element is copper
					if self.stroke[max(0, i - 1)] == 1:
						#he + charge
						self.stroke[i - 1] = 5

					#if right element is copper
					if self.stroke[min(i + 1, len(self.stroke) - 1)] == 1:
						#he + charge
						self.stroke[i + 1] = 5

		#return result
		return self.stroke