from turtle import Turtle
from conway.logic import next_gen
import random

class Illustrator:
    def __init__(self, live_cells, a: int=2, b: int=3, d: int=3):
        self.live_cells = live_cells
        self.a = a
        self.b = b
        self.d = d
        self.turtles = {}

    def show_config(self):
        for cell in self.live_cells:
            t = Turtle("square")
            t.penup()
            t.hideturtle()
            t.shapesize(0.9, 0.9, 1)
            t.color("yellow")
            t.goto(cell)
            t.showturtle()
            self.turtles[t] = random.randint(1, 10000000)

    def update_config(self):
        self.live_cells = next_gen(self.live_cells, self.a, self.b, self.d)
        for tim in self.turtles.copy():
            tim.hideturtle()
            del self.turtles[tim]