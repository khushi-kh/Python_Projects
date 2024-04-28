from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()  # inheriting properties of superclass Turtle to subclass Food
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
