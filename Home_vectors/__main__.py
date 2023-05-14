# -*- coding: utf-8 -*-
import py5
import random
import vect_point
import vect_line

def setup():
    global delta_x, delta_y, x_coord, y_coord, my_point, another_point,one_point,red_line,green_point,many_line
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
    
    #могу ли я создать массив из моих же уже созданных объектов,таких как my_point?
    
    green_point=[]
    for i in range(200):
    #было: green_point.append(vect_point.Point(py5.random(150,200),py5.Py5Vector(py5.random(50,100),py5.random(50,100))))
        
        green_point.append(vect_point.Point(py5.random(0,500),py5.random(0,500)))
    many_line =[]
    for i in range(500):
        many_line.append(vect_line.Line(py5.random(0,500),py5.random(0,500)))
   
        
        
    #py5.no_loop()

def draw():
    global delta_x, delta_y, x_coord, y_coord, my_point, another_point,one_point,my_line,green_point,many_line
    py5.background(0)
    
    mouse_point=py5.Py5Vector (100,200)
    force1 =mouse_point-my_point.position
    force1=force1.norm * 0.003
    force2 =mouse_point-another_point.position
    force2=force2.norm * 0.003
    force3 =mouse_point-one_point.position
    force3=force3.norm * 0.003
    my_point.apply_force(force1)
    another_point.apply_force(force2)
    one_point.apply_force(force3)
    my_point.move()
    another_point.move()
    one_point.move()
    red_line.move()
    my_point.check_edges()
    another_point.check_edges()
    one_point.check_edges()
    red_line.check_edges()
    my_point.display()
    another_point.display()
    one_point.display()
    red_line.display()
    for i in range(len(green_point)):
        green_point[i].move()
    #исправил неправильно названный метод
        green_point[i].check_edges()
        green_point[i].display()
    for i in range(len(many_line)):
        many_line[i].move()
    #исправил неправильно названный метод
        many_line[i].check_edges()
        
        
        many_line[i].display()
        

py5.run_sketch()
