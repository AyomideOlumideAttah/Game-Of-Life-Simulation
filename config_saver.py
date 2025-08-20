import csv, json

def name_format(s: str):
    s_list = s.split(" ")
    if len(s_list) == 1:
        return s
    tokens = [s_list[0]]
    for word in s_list[1:]:
        tokens.append("_")
        tokens.append(word)
    return "".join(tokens)

options = ["R-Pentomino", "Simple Oscillator", "Light Weight Space Ship", "Heavy Weight Space Ship", "Pulsar", "Glider"]

for config_name in options:
    file_path = f"Initial Configs/{name_format(config_name.lower())}.csv"
    with open(file_path, 'r') as f:
        cells = [(int(cell["x"]), int(cell["y"])) for cell in list(csv.DictReader(f))]

    with open("configs.json", "r") as db:
        data = json.load(db)

    data[config_name] = cells

    with open("configs.json", "w") as db:
        json.dump(data, db)
