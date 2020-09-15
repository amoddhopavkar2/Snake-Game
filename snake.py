import pygame
import math
import random
import tkinter as tk
from tkinter import messagebox


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

	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			keys = pygame.key.get_pressed()
			for key in keys:
				if keys[pygame.K_LEFT]:
					self.dir_x = -1
					self.dir_y = 0
					self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]

				elif keys[pygame.K_RIGHT]:
					self.dir_x = 1
					self.dir_y = 0
					self.turns[self.head.pos[:]] == [self.dir_x, self.dir_y]

				elif keys[pygame.K_UP]:
					self.dir_x = 0
					self.dir_y = -1
					self.turns[self.head.pos[:]] == [self.dir_x, self.dir_y]

				elif keys[pygame.K_DOWN]:
					self.dir_x = 0
					self.dir_y = 1
					self.turns[self.head.pos[:]] == [self.dir_x, self.dir_y]


		for i, c in enumerate(self.body):
			p = c.pos[:]
			if p in self.turns:
				turn = self.turns[p]
				c.move(turn[0], turn[1])
				if i == len(self.body) - 1:
					self.turns.pop(p)

			else:
				if c.dir_x == -1 and c.pos[0] <= 0:
					c.pos = (c.rows - 1, c.pos[1])

				elif c.dir_x == 1 and c.pos[0] >= c.rows - 1:
					c.pos = (0, c.pos[1])

				elif c.dir_y == 1 and c.pos[1] >= c.rows - 1:
					c.pos = (c.pos[0], 0)

				elif c.dir_y == -1 and c.pos[1] <= 0:
					c.pos = (c.pos[0], c.rows - 1)

				else:
					c.move(c.dir_x, c.dir_y)


	def addCube(self):
		tail = self.body[-1]
		dx, dy = tail.dir_x, tail.dir_y

		if dx == 1 and dy == 0:
			self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))

		elif dx == -1 and dy == 0:
			self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))

		elif dx == 0 and dy == 1:
			self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))

		elif dx == 0 and dy == -1:
			self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

		self.body[-1].dir_x = dx
		self.body[-1].dir_y = dy


	def draw(self, surface):
		for i, c in enumerate(self.body):
			if i == 0:
				c.draw(surface, True)
			else:
				c.draw(surface)


def redrawWindow(surface):
	global rows, width, s, snack
	surface.fill((0, 0, 0))
	s.draw(surface)
	snack.draw(surface)
	drawGrid(width, rows, surface)
	pygame.display.update()


def randomSnack(rows, items):
	positions = item.body

	while True:
		x = random.randomrange(rows)
		y = random.randomrange(rows)

		if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
			continue
		else:
			break

	return (x, y)


def message_box(subject, content):
	root = tk.Tk()
	root.attributes("-topmost", True)
	root.withdraw()
	messagebox.showinfo(subject, content)
	try:
		root.destroy()
	except:
		pass


def main():
	global width, rows, s, snack
	width = 500
	rows = 20
	win = pygame.display.set_mode((width, width))
	s = snake((255, 0, 0), (10, 10))
	snack = cube(randomSnack(rows, s), color = (0, 255, 0))
	flag = True
	clock = pygame.time.Clock()

	high_score = 0
	while flag:
		pygame.time.delay(50)
		clock.tick(10)
		s.move()
		if s.body[0].pos == snack.pos:
			s.addCube()
			snack = cube(randomSnack(rows, s), color = (0, 255, 0))

		for x in range(len(s.body)):
			if s.body[x].pos in list(map(lambda z: z.pos, s.body[x+1:])):
				print("\nScore: ", len(s.body))
				if len(s.body) > high_score:
					high_score = s.body
					print("\nNew High Score!!")
				message_box("\nYou Lost!", "Play again...")
				s.reset((10, 10))
				break

		redrawWindow(win)
	pass


