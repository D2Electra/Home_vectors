# -*- coding: utf-8 -*-
"""
Created on Tue May  2 22:11:17 2023

@author: pushi
"""

import py5
import random

WIDTH = 640
HEIGHT = 480
CELL_SIZE = 100
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
        self.letter = chr(random.choice([ 1071]))

    def display(self):
        py5.fill(*self.color)
        py5.text(self.letter, self.x, self.y)

    def move(self, cursor_x, cursor_y):
        distance = py5.dist(self.x, self.y, cursor_x, cursor_y)
        if distance > 50:
            self.x += self.speed * py5.cos(py5.radians(self.angle))
            self.y += self.speed * py5.sin(py5.radians(self.angle))
            if self.x < 0 or self.x > WIDTH:
                self.angle = 180 - self.angle
                self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                self.letter = chr(random.choice([1058,1067]))
            if self.y < 0 or self.y > HEIGHT:
                self.angle = -self.angle
                self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                self.letter = chr(random.choice([1071]))

letters = []

def setup():
    py5.size(WIDTH, HEIGHT)
    py5.background(255)
    py5.stroke(0)
    py5.text_size(30)
    for i in range(200):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        letters.append(Letter(x, y))

def draw():
    py5.background(255)

    cursor_x = py5.mouse_x
    cursor_y = py5.mouse_y

    for letter in letters:
        letter.move(cursor_x, cursor_y)
        letter.display()

py5.run_sketch()
