from conway.illustration import Illustrator
from turtle import Screen
from time import sleep
import csv



def run(config_name):
    screen = Screen()
    screen.bgcolor("blue")
    screen.title("Conway's Game of Life!")
    screen.tracer(0)

    a = int(input("Recall that 2 is the minimum number of live neighbours a live cell should have\nin"
                  " order to remain alive. What should this number be instead? "))
    b = int(input("Recall that 3 is the maximum number of live neighbours a live cell should have\nin"
                  "order to remain alive. What should this number be instead? "))
    d_set = eval(input("Recall that a dead cell must have exactly 3 live neighbours in order\nfor"
                       "it to come back to life. Here, you can modify 3 to be any set of numbers! Enter a set (like {3, 4}): "))
    print("Enjoy!")
    living_cells = set()
    with open(f"C:/Users/ayomi/PycharmProjects/Conway's-Game-Of-Life/Initial Configs/{config_name}.csv", "r") as f:
        cells = list(csv.DictReader(f))
        for cell in cells:
            living_cells.add((int(cell["x"]), int(cell["y"])))


    illustrator = Illustrator(living_cells, a, b, d_set)
    illustrator.show_config()

    screen.update()
    sleep(5)


    i = 0
    while i < 200:
        sleep(0.1)
        screen.update()

        illustrator.update_config()
        illustrator.show_config()
        i += 1

    screen.mainloop()
