# entity.py

import turtle

class Entity:
    def __init__(self, size, color, shape, coordinates):
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
        if self.head.direction != "down" or len(self.segments) < 1:
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up" or len(self.segments) < 1:
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right" or len(self.segments) < 1:
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left" or len(self.segments) < 1:
            self.head.direction = "right"

    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + self.size)

        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - self.size)

        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - self.size)

        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + self.size)

    def xcor(self):
        return self.head.xcor()

    def ycor(self):
        return self.head.ycor()

    def transport(self, boundries, coordiantes=()):
        if coordiantes == ():
            x = random.randint(boundries['left'], boundries['right']) // self.size * self.size
            y = random.randint(boundries['top'], boundries['bottom']) // self.size * self.size
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
        self.segments = []

    def move_body(self):
        for index in range(len(self.segments)-1, 0, -1):
            x = self.segments[index-1].xcor()
            y = self.segments[index-1].ycor()
            self.segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(self.segments) > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.segments[0].goto(x,y)

    def body_coll(self):
        for segment in self.segments:
            if segment.distance(head) < self.entity_size:
                time.sleep(1)
                self.head.goto(0,0)
                self.head.direction = "stop"

                # Hide the segments
                for segment in self.segments:
                    # segment.goto(window_width, window_height) # sends them to out past the bottom right corner
                    segment.clear()
                    segment.ht()
                    del segment

                # Clear the segments list
                self.segments.clear()

                # Reset the score
                score = 0

                # Reset the delay
                delay = 0.1

                # Update the score display
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
