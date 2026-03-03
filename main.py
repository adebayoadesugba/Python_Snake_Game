import random
from turtle import Turtle, Screen
import turtle as t
import time
from snake_game import Snake, Move, Food, Scoreboard
screen = Screen()
screen.bgcolor("Black")
screen.setup(width=600, height=600)
screen.title("The Snake Game")
screen.tracer(0)
# dimension = [-20, 0, 20]

color_list = ["Blue", "Green", "Red", "Orange", "Yellow", "SlateGray", "SeaGreen"]
my_snake = Snake()
food = Food()
scores = Scoreboard()
# snake_body = []
# for d in range(3):
#     snake = Turtle(shape="square",)
#     snake.color("white")
#     snake.penup()
#     snake.goto(x=dimension[d], y=0)
#     snake_body.append(snake)


snake_game = True
snake_movement = Move(my_snake.snake_body)
screen.listen()
screen.onkey(snake_movement.up, "Up")
screen.onkey(snake_movement.down, "Down")
screen.onkey(snake_movement.left, "Left")
screen.onkey(snake_movement.right, "Right")

score_update = scores.update_scoreboard()

while snake_game:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
    

    ## Detecting Collision with Food
    if my_snake.snake_body[0].distance(food) < 15:
        food.color(random.choice(color_list))
        food.goto(random.randint(-280,280), random.randint(-280,280))
        scores.increase_score()

        tail = my_snake.snake_body[-1]

        new_body = Turtle("square")
        new_body.penup()
        new_body.color("red")
        new_body.goto(tail.position())

        my_snake.snake_body.append(new_body)

    
     ## Detecting Collision with Wall
    if my_snake.snake_body[0].xcor() > 280 or my_snake.snake_body[0].xcor() < -280 or my_snake.snake_body[0].ycor() > 280 or my_snake.snake_body[0].ycor() < -280:
        scores.game_over()
        snake_game = False

    # Detecting Collision with body
    head = my_snake.snake_body[0]

    for segment in my_snake.snake_body[1:]:
        
        if head.distance(segment) < 10:
            scores.game_over()
            snake_game = False


    






screen.exitonclick()


















  #     for s in range(len(snake_body)-1, 0, -1):
        #         new_x = snake_body[s-1].xcor()
        #         new_y = snake_body[s-1].ycor()
        #         snake_body[s].goto(new_x, new_y)
        #     snake_body[0].forward(20)
        #     screen.listen()
        #     screen.onkey(key="a", fun=turn_left)
        #     screen.onkey(key="d", fun=turn_right)
