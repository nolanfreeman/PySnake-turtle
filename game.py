# game.py

from player import Player

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
        self.theme = {'bgcolor': 'green', 'playercolor': 'black', 'playershape':'square'}

        # score gameplay variables
        self.high_score = 0
        self.score = 0

        self.state = states['menu']
        self.entities = []
        self.delay = 0.1

    # getter methods
    def get_window_dim():
        return self.window

    def get_theme():
        return self.theme

    # called when starting a new game
    def play():
        player = Player(self.entity_size, self.theme['playercolor'], self.theme['playershape'], (0,0))

        self.player.clear_segments()

        self.score = 0

        self.delay = 0.1

        self.state = state['play']

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    def gameover():
        time.sleep(1)
        player.transport((0,0))
        player.set_direction('stop')

    # Where the whole game runs
    def start():

        while True:
            window.update()

            if state == states['menu']:

                self.play()

            if state == states['play']:
                # Check for a collision with the border
                if player.xcor()> boundries['right'] or player.xcor()<boundries['left'] or player.ycor()>boundries['bottom'] or player.ycor()<boundries['top']:
                    self.gameover()

                for entity in self.entities:

                    if player.get_distance(entity) < entity_size:

                        # Shorten the delay
                        delay -= 0.001

                        self.score += 10

                        if self.score > self.highscore:
                            self.highscore = self.score

                        pen.clear()
                        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

            if state == states['paused']:
                pass

            if state == states['gameover']:
                pass

            time.sleep(delay)
