# player.py

from entity import Entity

class Player(Entity):
    def __init__(self, size, color, shape, coordinates):
        super().__init__(size, color, shape, coordiantes)

    def add_segment(self):
        if self.score > self.highscore:
            self.highscore = self.score

        new = turtle.Turtle()
        new.speed(0)
        new.shape(self.shape)
        new.color(self.color) # TODO make color lighter version of head
        new.penup()
        self.segments.append(new)
