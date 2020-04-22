import turtle
import time
import random

delay = 0.1

states = {'menu', 'play', 'paused', 'gameover'}

# Score
score = 0
high_score = 0
window_width, window_height = 600, 600
entity_size = 20
boundries = {'left' : -1 * window_width/2 + entity_size/2,
             'right' : window_width/2 - entity_size/2,
             'top' : -1 * window_height/2 + entity_size/2,
             'bottom' : window_height/2 - entity_size/2}
state = states['play']

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=window_width, height=window_height)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down" or len(segments) < 1:
        head.direction = "up"

def go_down():
    if head.direction != "up" or len(segments) < 1:
        head.direction = "down"

def go_left():
    if head.direction != "right" or len(segments) < 1:
        head.direction = "left"

def go_right():
    if head.direction != "left" or len(segments) < 1:
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + entity_size)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - entity_size)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - entity_size)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + entity_size)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    if state == states['menu']:
        s = 1

    if state == states['play']:
        # Check for a collision with the border
        if head.xcor()> boundries['right'] or head.xcor()<boundries['left'] or head.ycor()>boundries['bottom'] or head.ycor()<boundries['top']:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


        # Check for a collision with the food
        if head.distance(food) < entity_size:
            # Move the food to a random spot
            x = random.randint(boundries['left'], boundries['right']) // entity_size * entity_size
            y = random.randint(boundries['top'], boundries['bottom']) // entity_size * entity_size
            food.goto(x,y)

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            # Shorten the delay
            delay -= 0.001

            # Increase the score
            score += 10

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

        # Move the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

        move()    

        # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < entity_size:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"

                # Hide the segments
                for segment in segments:
                    segment.goto(window_width, window_height) # sends them to out past the bottom right corner

                # Clear the segments list
                segments.clear()

                # Reset the score
                score = 0

                # Reset the delay
                delay = 0.1

                # Update the score display
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    if state == states['paused']:
        s = 3

    if state == states['gameover']:
        s = 4

    time.sleep(delay)

wn.mainloop()
