def neighbors(tup: tuple[int, int]):
    x = tup[0]
    y = tup[1]
    return {(x - 20, y - 20), (x - 20, y), (x - 20, y + 20), (x, y + 20), (x + 20, y + 20), (x + 20, y),
            (x + 20, y - 20), (x, y - 20)}

def next_gen(live_cells: {tuple[int, int]}, a=2, b=3, d_set=None):
    if d_set is None:
        d_set = {3}
    new_live_cells = set()
    for live_cell in live_cells:
        neighborhood = neighbors(live_cell)
        neighborhood.add(live_cell)
        for c in neighborhood:
            if c in new_live_cells:
                continue
            live_neighbors_count = sum(1 for nb in neighbors(c) if nb in live_cells)
            if (c in live_cells and a <= live_neighbors_count <= b) or (c not in live_cells and live_neighbors_count in d_set):
                new_live_cells.add(c)
    return new_live_cells