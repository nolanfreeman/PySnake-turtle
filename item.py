# item.py

from entity import Entity

class Item(Entity):
    def __init__(self, size, color, shape, coordinates):
        super().__init__(size, color, shape, coordinates)

