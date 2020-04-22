# item.py

from entity import Entity

class Item(Entity):
    def __init__(self, size, color, shape, coordinates):
        super().__init__(size, color, shape, coordiantes)

    def transport(self, coordiantes=()):
        if coordiantes == ():
            x = random.randint(boundries['left'], boundries['right']) // size * size
            y = random.randint(boundries['top'], boundries['bottom']) // size * size
        else:
            x, y = coordiantes

        self.head.goto(x, y)
