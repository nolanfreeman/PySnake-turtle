# player.py

from entity import Entity

class Player(Entity):
    def __init__(self, size, color, shape, coordinates):
        super().__init__(size, color, shape, coordinates)

    def add_segment(self):
        new = turtle.Turtle()
        new.speed(0)
        new.shape(self.shape)
        new.color(self.color) # TODO make color lighter version of head
        new.penup()
        self.segments.append(new)
