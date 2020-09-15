import pygame
import math
import random


class cube(object):
	rows = 20
	width = 500

	def __init__(self, start, dir_x = 1, dir_y = 0, color=(255, 0, 0)):
		self.pos = start
		self.dir_x = 1
		self.dir_y = 0
		self.color = color

	def move(self, dir_x, dir_y):
		self.dir_x = dir_x
		self.dir_y = dir_y
		self.pos = (self.pos[0] + self.dir_x, self.pos[1] + self.dir_y)

	def draw(self, surface, eyes = False):
		distance = self.width // self.rows
		i = self.pos[0]
		j = self.pos[1]

		pygame.draw.rect(surface, self.color, (i * distance + 1, j * distance + 1, distance - 2, distance - 2))
		if eyes:
			centre = distance / 2
			radius = 3
			circleMiddle_1 = (i * distance + centre - radius, j * distance + 8)
			circleMiddle_2 = (i * distance + distance - radius * 2, j * distance + 8)
			pygame.draw.circle(surface, (0, 0, 0), circleMiddle_1, radius)
			pygame.draw.circle(surface, (0, 0, 0), circleMiddle_2, radius)


class snake(object):
	body = []
	turns = {}

	def __init__(self, color, pos):
		self.color = color
		self.head = cube(pos)
		self.body.append(self.head)
		self.dir_x = 0
		self.dir_y = 1