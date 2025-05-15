from turtle import Turtle
from conway.logic import next_gen

class Illustrator:
    def __init__(self, live_cells, a=2, b=3, d_set: {int}=None):
        self.live_cells = live_cells
        self.a = a
        self.b = b
        self.d_set = d_set
        self.turtles = []

    def show_config(self):
        for cell in self.live_cells:
            t = Turtle("square")
            t.penup()
            t.hideturtle()
            t.shapesize(0.9, 0.9, 1)
            t.color("yellow")
            t.goto(cell)
            t.showturtle()
            self.turtles.append(t)


    def update_config(self):
        self.live_cells = next_gen(self.live_cells, self.a, self.b, self.d_set)
        for tim in self.turtles.copy():
            tim.hideturtle()
            self.turtles.remove(tim)