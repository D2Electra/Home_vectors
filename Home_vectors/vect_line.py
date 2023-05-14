import py5
import random

class Line (object):
    def __init__(self, xpos, ypos):
        self.position = py5.Py5Vector(xpos, ypos )#у вектора две координаты!!
        self.velocity = py5.Py5Vector(py5.random(0.6), py5.random(0.9))
        self.acceleration = py5.Py5Vector(py5.random(0.03),py5.random(0.9))
        #self.diameter = random.randint(5, 50)
        self.c = py5.color(255, 255, 255)

        
  
   
    def transform(self, new_height):
            self.height = new_height
      
    def move(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        
        
        
    
    def display(self):
        py5.push_matrix()
        py5.translate(self.position.x, self.position.y)
        py5.rotate(py5.radians(90))
        

        py5.stroke(self.c)
        py5.stroke_weight(0.5)
        py5.line(0, 0, 0, 20)
        py5.line(0, 0, 0, -20)
        
        py5.pop_matrix()# -*- coding: utf-8 -*-
    
   
    # не понимаю как это записать
    def check_edges(self):
        if self.position.x > py5.width:
            self.velocity.x = -self.velocity.x
            self.position.x = py5.width
        if self.position.x < 0:
            self.velocity.x = -self.velocity.x
            self.position.x = 0
        if self.position.y > py5.height or self.position.y + 20 > py5.height or self.position.y - 20 > py5.height:
            self.velocity.y = -self.velocity.y
            self.position.y = py5.height - 20
        if self.position.y < 0 or self.position.y + 50 < 0 or self.position.y - 20 < 0:
            self.velocity.y = -self.velocity.y
            self.position.y = 20
     
        
