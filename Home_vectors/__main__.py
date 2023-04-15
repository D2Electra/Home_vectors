# -*- coding: utf-8 -*-
import py5
import random
import vect_point

def setup():
    global delta_x, delta_y, x_coord, y_coord, my_point, another_point
    py5.size(500, 500)
    py5.background(0)
    #py5.stroke(255, 0, 0)
    py5.fill(255, 0, 0)
    delta_x = 2
    delta_y = 3
    x_coord = 60
    y_coord = 60
    my_point = vect_point.Point(50, 50)
    another_point = vect_point.Point(70, 150)
    #py5.no_loop()

def draw():
    global delta_x, delta_y, x_coord, y_coord, my_point, another_point
    py5.background(0)
    my_point.move()
    another_point.move()
    my_point.display()
    another_point.display()


py5.run_sketch()
