import random
import py5

WIDTH = 640
HEIGHT = 480
CELL_SIZE = 30
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = CELL_SIZE
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed = random.uniform(2, 5)
        self.angle = random.uniform(0, 360)
        self.shape_type = random.choice(["circle", "square", "letter"])
        
    def display(self):
        py5.fill(*self.color)
        if self.shape_type == "circle":
            py5.circle(self.x, self.y, self.size)
        elif self.shape_type == "square":
            py5.rect(self.x - self.size/2, self.y - self.size/2, self.size, self.size)
        elif self.shape_type == "letter":
            if random.random() < 0.5:
                py5.text(chr(random.randint(65, 90)), self.x, self.y)
            else:
                py5.text(chr(random.randint(1040, 1071)), self.x, self.y)

    def move(self):
        self.x += self.speed * py5.cos(py5.radians(self.angle))
        self.y += self.speed * py5.sin(py5.radians(self.angle))
        if self.x < 0 or self.x > WIDTH:
            self.angle = 180 - self.angle
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if self.shape_type == "circle":
                self.size = CELL_SIZE * 5
            elif self.shape_type == "square":
                self.size = CELL_SIZE * 5
            elif self.shape_type == "letter":
                self.size = CELL_SIZE * 10
        if self.y < 0 or self.y > HEIGHT:
            self.angle = -self.angle
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if self.shape_type == "circle":
                self.size = CELL_SIZE
            elif self.shape_type == "square":
                self.size = CELL_SIZE * 2
            elif self.shape_type == "letter":
                self.size = CELL_SIZE * 20

shapes = []

def setup():
    py5.size(WIDTH, HEIGHT)
    py5.background(255)
    py5.stroke(0)
    py5.text_size(30)
    for i in range(100):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        shapes.append(Shape(x, y))

def draw():
    py5.background(255)

    for shape in shapes:
        shape.move()
        shape.display()

py5.run_sketch()



