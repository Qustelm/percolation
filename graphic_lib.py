import random
import copy
import bpy
import matrix3d_read as m3d

SIZE = 10
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

probablity = 0.7

def add_cube(x, y, z, color):
    bpy.ops.mesh.primitive_cube_add(location=(x*2,y*2,z*2))
    ob = bpy.context.object
    material = bpy.data.materials.new('Red')
    material.diffuse_color = color
    material.specular_hardness = 200
    ob.data.materials.append(material)

matrix = []
for z in range(SIZE):
	matrix.append([])
	for y in range(SIZE):
		matrix[z].append([])
		for x in range(SIZE):
			if random.random() < probablity:
				matrix[z][y].append(1)
			else:
				matrix[z][y].append(0)

			if z == 0 and matrix[z][y][x] == 1:
				matrix[z][y][x] = 5

matrix = m3d.Matrix3d(matrix).return_new()

for z in range(SIZE):
	for y in range(SIZE):
		for x in range(SIZE):
			if matrix[z][y][x] == 5:
				add_cube(x, y, z, (1, 0, 0))
			elif matrix[z][y][x] == 1:
				add_cube(x, y, z, (0, 0, 1))