# entity.py

import turtle

class Entity:
    def __init__(self, size, color, shape, coordiantes):
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.color(color)
        self.head.shape(shape)
        self.head.penup()
        self.head.goto(*coordinates)
        self.head.direction = 'stop'

        # store passed variables for reference
        self.size = size
        self.shape = shape
        self.color = color

        # for an entity that is longer than 1 brick
        # the segments are its body
        self.segments = []

    # movement methods
    def go_up(self):
        if self.head.direction != "down" or len(segments) < 1:
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up" or len(segments) < 1:
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right" or len(segments) < 1:
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left" or len(segments) < 1:
            self.head.direction = "right"

    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + size)

        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - size)

        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - size)

        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + size)

    def xcor():
        return self.head.xcor()

    def ycor():
        return self.head.ycor()

    def transport(self, coordiantes=()):
        if coordiantes == ():
            x = random.randint(boundries['left'], boundries['right']) // size * size
            y = random.randint(boundries['top'], boundries['bottom']) // size * size
        else:
            x, y = coordiantes

        self.head.goto(x, y)

    def set_direction(self, direction):
        self.head.direction = direction

    def get_distance(self, entity):
        return self.head.distance(entity)

    def clear_segments(self):
        for segment in self.segments:
            segment.clear()
            segment.ht()
            del segment
        segments = []
