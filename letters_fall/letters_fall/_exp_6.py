# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:59:45 2023

@author: pushi
"""

import py5
import random

WIDTH = 640
HEIGHT = 480
CELL_SIZE = 200
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

class Letter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = CELL_SIZE
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed = random.uniform(2, 5)
        self.angle = random.uniform(0, 360)
        self.letter = chr(random.randint(65, 90))

    def display(self):
        py5.fill(*self.color)
        py5.text(self.letter, self.x, self.y)

    def move(self):
        dx = self.x - py5.mouse_x
        dy = self.y - py5.mouse_y
        distance = py5.sqrt(dx*dx + dy*dy)
        if distance < 50:
            self.angle = py5.atan2(dy, dx) + py5.PI
            self.x += self.speed * py5.cos(self.angle)
            self.y += self.speed * py5.sin(self.angle)
        else:
            self.x += self.speed * py5.cos(py5.radians(self.angle))
            self.y += self.speed * py5.sin(py5.radians(self.angle))
        if self.x < 0 or self.x > WIDTH:
            self.angle = 180 - self.angle
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.letter = chr(random.randint(65, 90))
        if self.y < 0 or self.y > HEIGHT:
            self.angle = -self.angle
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.letter = chr(random.randint(65, 90))


letters = []

def setup():
    py5.size(WIDTH, HEIGHT)
    py5.background(255)
    py5.stroke(0)
    py5.text_size(30)

    for i in range(50):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        letters.append(Letter(x, y))

def draw():
    py5.background(255)

    for letter in letters:
        letter.move()
        letter.display()

    if py5.mouse_x > 0 and py5.mouse_x < WIDTH and py5.mouse_y > 0 and py5.mouse_y < HEIGHT:
        for i in range(10):
            x = py5.mouse_x + random.randint(-50, 50)
            y = py5.mouse_y + random.randint(-50, 50)
            letters.append(Letter(x, y))

py5.run_sketch()
