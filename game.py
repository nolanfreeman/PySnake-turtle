# game.py

class Game:
    def __init__(self):
        # enviroment setup variables
        self.window = {'width': 600, 'height': 600}
        self.entity_size = 20
        self.boundries = {'left' : -1 * window_width/2 + entity_size/2,
                          'right' : window_width/2 - entity_size/2,
                          'top' : -1 * window_height/2 + entity_size/2,
                          'bottom' : window_height/2 - entity_size/2}

        # score gameplay variables
        self.high_score = 0
        self.score = 0

        self.state = states['play']
