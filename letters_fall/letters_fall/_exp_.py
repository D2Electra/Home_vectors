# -*- coding: utf-8 -*-
"""
Created on Mon May  1 21:25:33 2023

@author: pushi
"""
import py5
import random

x_positions = []
y_positions = []
letters = []

def setup():
    py5.size(500, 500)
    py5.color(255,255,255)
    py5.text_size(10)
    py5.text_align(py5.CENTER)
    py5.frame_rate(30)
    py5.background(0,33,55)
    
def draw():
    py5.background(0,33,55)
    if random.random() < 0.5:
        x_positions.append(random.randint(0, py5.width))
        y_positions.append(0)
        letters.append(chr(random.randint(1040, 1071)))
    
    for i in range(len(y_positions)):
        py5.fill(random.randint(255, 255), 255, 255)
        py5.text(letters[i], x_positions[i], y_positions[i])
        y_positions[i] += 5
        
        if y_positions[i] > py5.height - 20:
            y_positions[i] = py5.height - 20


 
py5.run_sketch()            