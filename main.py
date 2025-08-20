from conway.template import run

# def name_format(s: str):
#     s_list = s.split(" ")
#     if len(s_list) == 1:
#         return s
#     new_s = s_list[0]
#     for word in s_list[1:]:
#         new_s += "_" + word
#     return new_s

options = ["R-Pentomino", "Simple Oscillator", "Light Weight Space Ship", "Heavy Weight Space Ship", "Pulsar", "Glider"]
print("Welcome to Conway's Game of Life - Variations! In this project, \nwe will vary the rules in the game.")

print("Here are the possible initial configurations you can explore: ")

for option in options:
    print(option)

config_name = input("Choose one from the above!\n")
run(config_name, speed=5)