from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5 , stretch_wid=1)
        self.color("brown")
        self.speed("fastest")
    def refresh(self):
        randome_x = random.randint(-280 , 280)
        randome_y = random.randint(-280 , 280)
        self.goto(randome_x , randome_y)
f = Food()
