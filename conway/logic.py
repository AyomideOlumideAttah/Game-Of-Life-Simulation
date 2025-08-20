def neighbors(cell: tuple[int, int]):
    x, y = cell
    return {(x + dx, y + dy) for dx in [-20, 0, 20] for dy in [-20, 0, 20]}

def next_gen(live_cells: set[tuple[int, int]], a: int=2, b: int=3, d: int=3):
    new_live_cells = set()
    for live_cell in live_cells:
        neighborhood = neighbors(live_cell)
        for c in neighborhood:
            if c not in new_live_cells:
                live_neighbors_count = sum(int(nb != c) for nb in neighbors(c) if nb in live_cells)
                if (c in live_cells and a <= live_neighbors_count <= b) or (c not in live_cells and live_neighbors_count == d):
                    new_live_cells.add(c)
    return new_live_cells