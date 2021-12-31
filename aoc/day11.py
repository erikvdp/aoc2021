import numpy as np


def parse_input(lines) -> np.ndarray:
    return np.array(list(list(map(int, line)) for line in lines))


def _increase_neighbours(grid, x, y):
    for x_offset, y_offset in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]:
        if (
            0 <= x + x_offset < grid.shape[0] and 0 <= y + y_offset < grid.shape[1]
        ):  # check if not out of bounds
            if grid[x + x_offset, y + y_offset] < 10:  # is already going to flash
                grid[x + x_offset, y + y_offset] += 1
    return grid


def caculate_flashes(grid, num_rounds):
    total_flashes = 0
    for _ in range(num_rounds):
        grid += 1
        remaining_flashers = np.argwhere(grid == 10)
        while len(remaining_flashers) > 0:
            for i in range(len(remaining_flashers)):
                x, y = remaining_flashers[i]
                total_flashes += 1
                grid = _increase_neighbours(grid, x, y)
                grid[x, y] = 11  # flashed!
            remaining_flashers = np.argwhere(grid == 10)
        grid = np.where(grid != 11, grid, 0)
    return total_flashes


def calculate_synchronization(grid):
    iteration = 0
    is_synchronized = False
    while not is_synchronized:
        grid += 1
        remaining_flashers = np.argwhere(grid == 10)
        while len(remaining_flashers) > 0:
            for i in range(len(remaining_flashers)):
                x, y = remaining_flashers[i]
                grid = _increase_neighbours(grid, x, y)
                grid[x, y] = 11  # flashed!
            remaining_flashers = np.argwhere(grid == 10)
        grid = np.where(grid != 11, grid, 0)
        if np.all(grid == 0):
            is_synchronized = True
        iteration += 1
    return iteration
