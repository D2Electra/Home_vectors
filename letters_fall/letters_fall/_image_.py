# -*- coding: utf-8 -*-
"""
Created on Wed May  3 00:31:15 2023

@author: pushi
"""
import py5
import random
import math

WIDTH = 640
HEIGHT = 480

class FallingImage:
    def __init__(self, x, y, img_path):
        self.x = x
        self.y = y
        self.img = py5.load_image("D:/Processing/py5.projects/letters_fall/letters_fall/dasha.png")
        self.speed = random.uniform(1, 5)

    def display(self):
        py5.image(self.img, self.x, self.y)

    def update(self):
        self.y += self.speed
        if self.y + self.img.height >= HEIGHT:
            self.y = HEIGHT - self.img.height

    def check_bottom_edge(self):
        return self.y >= HEIGHT

    def reset_position(self):
        self.y = 0 - self.img.height

    def magnetize(self, cursor_x, cursor_y, strength):
        distance = math.sqrt((self.x - cursor_x)**2 + (self.y - cursor_y)**2)
        if distance < strength:
            self.x += (cursor_x - self.x) / 10
            self.y += (cursor_y - self.y) / 10

def setup():
    py5.size(WIDTH, HEIGHT)
    py5.background(255)
    py5.stroke(0)
    py5.cursor(True)

    global images
    images = []
    image_path = "D:/Processing/py5.projects/letters_fall/letters_fall/dasha.png"
    for i in range(5):
        x = random.randint(0, WIDTH)
        y = random.randint(-HEIGHT, 0)
        images.append(FallingImage(x, y, image_path))

def draw():
    py5.background(255)

    if py5.frame_count % 30 == 0:
        image_path = "path/to/your/image.png"
        x = random.randint(0, WIDTH)
        y = random.randint(-HEIGHT, 0)
        images.append(FallingImage(x, y, image_path))

    cursor_x = py5.mouse_x
    cursor_y = py5.mouse_y
    for image in images:
        image.magnetize(cursor_x, cursor_y, 300)
        image.display()
        image.update()

        if image.check_bottom_edge():
            image.reset_position()

py5.run_sketch()












