from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment(0-20*i, 0)

    def add_segment(self, x, y):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(x, y)
        self.snake_segments.append(snake)

    def move(self):
        # range(start= len(snake_segments)-1, stop=0, step=-1
        for segment_num in range(len(self.snake_segments)-1, 0, -1):
            new_x = self.snake_segments[segment_num-1].xcor()
            new_y = self.snake_segments[segment_num-1].ycor()
            self.snake_segments[segment_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def update_snake(self):
        self.add_segment(self.snake_segments[-1].xcor(), self.snake_segments[-1].ycor())
