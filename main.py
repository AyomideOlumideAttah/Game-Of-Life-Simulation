from conway.template import run

options = ["R-Pentomino", "Simple Oscillator", "Light Weight Space Ship", "Heavy Weight Space Ship", "Pulsar", "Glider"]
print("Welcome to Life - more specifically, Conway's Game of Life. This is a cellular automata created by legendary mathematician J.H. Conway who aimed to study self-replicating"
      "\nsystems. In this application, we would implement the rules that govern how any one instance of Conway's game evolves - with a twist: you'll have the option to"
      "\ntweak the numbers behind the game, in any way you like! By doing so, the hope is that you gain a general appreciation of the complexity that arises from"
      "\nsimple self-replication rules, as well as maybe discover your own algorithms. Let's see what you can do!\n")

print("Here are the possible initial configurations you can explore: ")

for option in options:
    print(option)

config_name = input("Choose one from the above!\n")
run(config_name, speed=5)