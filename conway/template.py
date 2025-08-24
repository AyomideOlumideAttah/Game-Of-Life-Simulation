from conway.illustration import Illustrator
from turtle import Screen
import time, json

def run(config_name, speed: float=10):
    a = int(input("Recall that 2 is the minimum number of live neighbours a live cell should have in"
                  " order to remain alive.\nWhat should this number be instead? "))
    b = int(input("Recall that 3 is the maximum number of live neighbours a live cell should have in"
                  " order to remain alive.\nWhat should this number be instead? "))
    d = int(input("Recall that a dead cell must have exactly 3 live neighbours in order for"
                  " it to come back to life.\nWhat should this number be instead? "))
    print("Game would load in 7 seconds. Enjoy!")

    time.sleep(7)

    screen = Screen()
    screen.bgcolor("blue")
    screen.title("Conway's Game of Life!")
    screen.tracer(0)

    living_cells = set()
    with open(f"configs.json", "r") as f:
        cells = json.load(f)[config_name]
        for cell in cells:
            living_cells.add(tuple(cell))

    illustrator = Illustrator(living_cells, a, b, d)
    illustrator.show_config()

    screen.update()
    time.sleep(5)

    i = 0
    while i < 2000:
        time.sleep(1 / speed)
        screen.update()

        illustrator.update_config()
        illustrator.show_config()
        i += 1

    screen.mainloop()
