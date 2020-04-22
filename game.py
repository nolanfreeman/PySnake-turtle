# game.py

states = {'menu':0, 'play':1, 'paused':2, 'gameover':3}

class Game:
    def __init__(self):
        # enviroment setup variables
        self.window = {'width': 600, 'height': 600}
        self.entity_size = 20
        self.boundries = {'left' : -1 * window['width']/2 + entity_size/2,
                          'right' : window['width']/2 - entity_size/2,
                          'top' : -1 * window['height']/2 + entity_size/2,
                          'bottom' : window['height']/2 - entity_size/2}
        self.theme = {'bgcolor': 'green'}

        # score gameplay variables
        self.high_score = 0
        self.score = 0

        self.state = states['play']

    # getter methods
    def get_window_dim():
        return self.window

    def get_theme():
        return self.theme

    # Where the whole game runs
    def start():
        pass
