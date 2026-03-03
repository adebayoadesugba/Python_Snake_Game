from turtle import Turtle
import random
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

color_list = ["Blue", "Green", "Red", "Orange", "Yellow", "SlateGray", "SeaGreen"]
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()


    def create_snake(self):
        dimension = [0, -20, -40]
        for d in range(3):
            snake = Turtle(shape="square",)
            snake.color("white")
            snake.penup()
            snake.goto(x=dimension[d], y=0)
            self.snake_body.append(snake)

    def move(self):
        for s in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[s-1].xcor()
            new_y = self.snake_body[s-1].ycor()
            self.snake_body[s].goto(new_x, new_y)
        self.snake_body[0].forward(20)


class Move:
    def __init__(self, snake_body_s):
        self.snake_body = snake_body_s
    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)
        

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(random.choice(color_list))
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(10)
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(x=random_x, y=random_y)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        # self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align="center", font=("Arial", 32, "normal"))
