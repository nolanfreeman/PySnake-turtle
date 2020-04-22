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

    def add_segment(self):
        new = turtle.Turtle()
        new.speed(0)
        new.shape(self.shape)
        new.color(self.color) # TODO make color lighter version of head
        new.penup()
        self.segments.append(new)
