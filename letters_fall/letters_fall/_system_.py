# -*- coding: utf-8 -*-
"""
Created on Mon May  1 21:44:14 2023

@author: pushi
"""

import py5
import random

WIDTH = 640
HEIGHT = 480
CELL_SIZE = 100
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = CELL_SIZE
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed = random.uniform(2, 5)
        self.angle = random.uniform(0, 360)

    def display(self):
        py5.fill(*self.color)
        py5.circle(self.x, self.y, self.size)

    def move(self):
        self.x += self.speed * py5.cos(py5.radians(self.angle))
        self.y += self.speed * py5.sin(py5.radians(self.angle))
        if self.x < 0 or self.x > WIDTH:
            self.angle = 180 - self.angle
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.size = CELL_SIZE
        if self.y < 0 or self.y > HEIGHT:
            self.angle = -self.angle
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.size = CELL_SIZE

circles = []

def setup():
    py5.size(WIDTH, HEIGHT)
    py5.background(255)
    py5.stroke(0)

    for i in range(100):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        circles.append(Circle(x, y))

def draw():
    py5.background(255)

    for circle in circles:
        circle.move()
        circle.display()

py5.run_sketch()
