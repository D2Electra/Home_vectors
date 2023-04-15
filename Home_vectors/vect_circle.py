# -*- coding: utf-8 -*-
import py5
import random

class Circle (object):
    def __init__(self, xpos, ypos):
        self.position = py5.Py5Vector(xpos, ypos)
        self.velocity = py5.Py5Vector(py5.random(0.6), py5.random(0.9))
        self.acceleration = py5.Py5Vector(0, 0)
        self.diameter = random.randint(5, 50)
        self.c = py5.color(255, 0, 0)
    
    def move(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0
    
    def display(self):
        py5.push_matrix()
        py5.translate(self.position.x, self.position.y)
        py5.circle(0, 0, self.diameter)
        py5.pop_matrix()
    
    def apply_force(self, force):
        self.acceleration += force
    
    def check_edges(self):
        if self.position.x + self.diameter / 2 > py5.width:
            self.velocity.x = -self.velocity.x
            self.position.x = py5.width - self.diameter / 2
        if self.position.x - self.diameter / 2 < 0:
            self.velocity.x = -self.velocity.x
            self.position.x = self.diameter / 2
        if self.position.y + self.diameter / 2 > 500:
            self.velocity.y = -self.velocity.y
            self.position.y + self.diameter / 2
        if self.position.y - self.diameter / 2 < 0:
            self.velocity.y = -self.velocity.y
            self.position.y = self.diameter / 2
            
py5.run_sketch()
