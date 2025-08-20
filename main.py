from conway.template import run

options = ["R-Pentomino", "Simple Oscillator", "Light Weight Space Ship", "Heavy Weight Space Ship", "Pulsar", "Glider"]
print("Welcome to Conway's Game of Life - Variations! In this project, \nwe will vary the rules in the game.")

print("Here are the possible initial configurations you can explore: ")

for option in options:
    print(option)

config_name = input("Choose one from the above!\n")
run(config_name, speed=5)