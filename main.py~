import turtle
import time
from game import Game


game = Game()

game.start()



# Main game loop
while True:
    window.update()

    if state == states['menu']:
        s = 1

    if state == states['play']:
        # # Check for a collision with the border
        # if head.xcor()> boundries['right'] or head.xcor()<boundries['left'] or head.ycor()>boundries['bottom'] or head.ycor()<boundries['top']:
            # time.sleep(1)
            # head.goto(0,0)
            # head.direction = "stop"

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
        # if head.distance(food) < entity_size:
            # # Move the food to a random spot
# 
            # # Shorten the delay
            # delay -= 0.001
# 
            # # Increase the score
            # score += 10
# 
            # if score > high_score:
                # high_score = score
# 
            # pen.clear()
            # pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 
# 
        # Move the end segments first in reverse order
        # for index in range(len(segments)-1, 0, -1):
            # x = segments[index-1].xcor()
            # y = segments[index-1].ycor()
            # segments[index].goto(x, y)
# 
        # # Move segment 0 to where the head is
        # if len(segments) > 0:
            # x = head.xcor()
            # y = head.ycor()
            # segments[0].goto(x,y)
# 
        # move()    

        # Check for head collision with the body segments
        # for segment in segments:
            # if segment.distance(head) < entity_size:
                # time.sleep(1)
                # head.goto(0,0)
                # head.direction = "stop"
# 
                # # Hide the segments
                # for segment in segments:
                    # # segment.goto(window_width, window_height) # sends them to out past the bottom right corner
                    # segment.clear()
                    # segment.ht()
                    # del segment
# 
                # # Clear the segments list
                # segments.clear()
# 
                # # Reset the score
                # score = 0
# 
                # # Reset the delay
                # delay = 0.1
# 
                # # Update the score display
                # pen.clear()
                # pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
# 
    if state == states['paused']:
        s = 3

    if state == states['gameover']:
        s = 4

    time.sleep(delay)

