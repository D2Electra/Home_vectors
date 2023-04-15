# -*- coding: utf-8 -*-
import py5
import random

class Point (object):
    def __init__(self, xpos, ypos):
        self.position = py5.Py5Vector(xpos, ypos)
        self.velocity = py5.Py5Vector(py5.random(0.6), py5.random(0.9))
        self.acceleration = py5.Py5Vector(0, 0)
        #self.diameter = random.randint(5, 50)
        self.c = py5.color(255, 0, 0)
        self.stroke_weight = py5.stroke_weight(3)
    def move(self):
        
        self.position += self.velocity
        
    
    def display(self):
        py5.push_matrix()
        py5.translate(self.position.x, self.position.y)
        py5.stroke_weight(5)
        py5.point(0, 0)
        py5.pop_matrix()


