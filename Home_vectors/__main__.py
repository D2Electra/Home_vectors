# -*- coding: utf-8 -*-
import py5
import random
import vect_point
import vect_line

def setup():
    global delta_x, delta_y, x_coord, y_coord, my_point, another_point,one_point,red_line
    py5.size(500, 500)
    py5.background(0)
    #py5.stroke(255, 0, 0)
    py5.fill(255, 211, 0)
    delta_x = 2
    delta_y = 3
    x_coord = 60
    y_coord = 60
    my_point = vect_point.Point(50, 50)
    another_point = vect_point.Point(70, 150)
    one_point = vect_point.Point(20, 100)
    red_line = vect_line.Line(100,200)
    
    #py5.no_loop()

def draw():
    global delta_x, delta_y, x_coord, y_coord, my_point, another_point,one_point,my_line
    py5.background(0)
    my_point.move()
    another_point.move()
    one_point.move()
    red_line.move()
    my_point.check_edges()
    another_point.check_edges()
    one_point.check_edges()
    my_point.display()
    another_point.display()
    one_point.display()
    red_line.display()
    

py5.run_sketch()
