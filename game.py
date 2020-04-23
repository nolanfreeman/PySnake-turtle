# game.py

from player import Player
from item import Item
import turtle
import time

states = {'menu':0, 'play':1, 'paused':2, 'gameover':3}

class Game:
    def __init__(self):
        # enviroment setup variables
        self.window = {'width': 600, 'height': 600}
        self.entity_size = 20
        self.boundries = {'left' : -1 * self.window['width']/2 + self.entity_size/2,
                          'right' : self.window['width']/2 - self.entity_size/2,
                          'top' : -1 * self.window['height']/2 + self.entity_size/2,
                          'bottom' : self.window['height']/2 - self.entity_size/2}
        self.theme = {'bgcolor': 'green', 'playercolor': 'black', 'playershape':'square', 'foodcolor':'red', 'foodshape':'circle'}

        # score gameplay variables
        self.highscore = 0
        self.score = 0

        self.state = states['menu']
        self.entities = []
        self.delay = 0.1
        self.player = None

        self.screen = turtle.Screen()
        self.screen.title("PySnake by @NolanFreeman")
        self.screen.bgcolor(self.theme['bgcolor'])
        self.screen.setup(self.window['width'], self.window['height'])
        self.screen.tracer(0) # Turns off the screen updates

        # Pen
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


    # getter methods
    def get_window_dim(self):
        return self.window

    def get_theme(self):
        return self.theme

    # called when starting a new game
    def play(self):
        self.player = Player(self.entity_size, self.theme['playercolor'], self.theme['playershape'], (0,0))

        food = Item(self.entity_size, self.theme['foodcolor'], self.theme['foodshape'], (0,0))
        food.transport(self.boundries, ())
        self.entities.append(food)

        self.player.clear_segments()

        self.score = 0

        self.delay = 0.1

        self.state = states['play']

        self.pen.clear()
        self.pen.write("Score: {}  High Score: {}".format(self.score, self.highscore), align="center", font=("Courier", 24, "normal")) 

        # Keyboard bindings
        self.screen.listen()
        self.screen.onkeypress(self.player.go_up, "w")
        self.screen.onkeypress(self.player.go_down, "s")
        self.screen.onkeypress(self.player.go_left, "a")
        self.screen.onkeypress(self.player.go_right, "d")

    def gameover(self):
        time.sleep(1)
        self.player.transport(self.boundries, (0,0))
        self.player.set_direction('stop')

    # Where the whole game runs
    def start(self):

        while True:
            self.screen.update()

            if self.state == states['menu']:

                self.play()

            if self.state == states['play']:
                # Check for a collision with the border
                if self.player.xcor()> self.boundries['right'] or self.player.xcor()<self.boundries['left'] or self.player.ycor()>self.boundries['bottom'] or self.player.ycor()<self.boundries['top']:
                    self.gameover()

                for entity in self.entities:

                    if self.player.get_distance(entity) < self.entity_size:

                        entity.transport(self.boundries, ())
                        self.player.add_segment()
                        # Shorten the delay
                        self.delay -= 0.001

                        self.score += 10

                        if self.score > self.highscore:
                            self.highscore = self.score

                        self.pen.clear()
                        self.pen.write("Score: {}  High Score: {}".format(self.score, self.highscore), align="center", font=("Courier", 24, "normal")) 

                self.player.body_coll(self)

                self.player.move_body()

                self.player.move()

            if self.state == states['paused']:
                pass

            if self.state == states['gameover']:
                pass

            time.sleep(self.delay)

        self.screen.mainloop()
