# -*- coding: utf-8 -*-
import py5
import random



x_positions = []
y_positions = []
letters = []
magnet_range = 100  # радиус области притяжения курсора мыши

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)
    py5.text_size(15)
    py5.text_align(py5.CENTER)
    py5.frame_rate(30)
    py5.background(0)

def draw():
    py5.background(0)
    if random.random() < 0.1:
        x_positions.append(random.randint(0, py5.width))
        y_positions.append(0)
        letters.append(chr(random.randint(1040, 1071)))

    for i in range(len(y_positions)):
        py5.fill(random.randint(0, 255), 255, 255)
        py5.text(letters[i], x_positions[i], y_positions[i])
        y_positions[i] += 5

        # Определяем, достигла ли буква дна экрана
        if y_positions[i] > py5.height - 15:
            y_positions[i] = py5.height - 15

        # Проверяем, находится ли буква на другой букве
        for j in range(len(y_positions)):
            if i != j and abs(x_positions[i] - x_positions[j]) < 20 and abs(y_positions[i] - y_positions[j]) < 20:
                y_positions[i] += random.choice([-1, 1]) * random.randint(0, 10)

        # Проверяем, находится ли курсор мыши рядом с буквой
        distance_to_mouse = py5.dist(x_positions[i], y_positions[i], py5.mouse_x, py5.mouse_y)
        if distance_to_mouse < magnet_range:
            # Буква прилипает к курсору мыши
            x_positions[i] = py5.lerp(x_positions[i], py5.mouse_x, 0.1)
            y_positions[i] = py5.lerp(y_positions[i], py5.mouse_y, 0.1)

    # Перерисовываем все буквы в новых позициях
    for i in range(len(y_positions)):
        py5.fill(random.randint(0, 255), 255, 255)
        py5.text(letters[i], x_positions[i], y_positions[i])





py5.run_sketch()



