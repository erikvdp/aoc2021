import numpy as np


def parse_input(lines) -> np.ndarray:
    return np.array(list(list(map(int, line)) for line in lines))


def calculate_risk_level(grid: np.ndarray) -> int:
    low_points = []
    # add border arround existing map
    grid = np.pad(grid, pad_width=1, mode="constant", constant_values=9)
    for row in range(1, grid.shape[0] - 1):
        for col in range(1, grid.shape[1] - 1):
            if grid[row, col] < min(
                (
                    grid[row - 1, col],
                    grid[row + 1, col],
                    grid[row, col - 1],
                    grid[row, col + 1],
                )
            ):
                low_points.append(grid[row, col])
    return sum(low_point + 1 for low_point in low_points)


def calculate_basins(grid: np.ndarray) -> int:
    grid = np.pad(grid, pad_width=1, mode="constant", constant_values=9)
    # fetch lowest points
    low_points = []
    for row in range(1, grid.shape[0] - 1):
        for col in range(1, grid.shape[1] - 1):
            if grid[row, col] < min(
                (
                    grid[row - 1, col],
                    grid[row + 1, col],
                    grid[row, col - 1],
                    grid[row, col + 1],
                )
            ):
                low_points.append((row, col))
    size = 0

    def _flood_fill(row, col):
        visited.add((row, col))
        if grid[row, col] == 9:
            return
        else:
            nonlocal size
            size += 1
        _flood_fill(row - 1, col) if (
            row - 1,
            col,
        ) not in visited else None
        _flood_fill(row + 1, col) if (
            row + 1,
            col,
        ) not in visited else None
        _flood_fill(row, col - 1) if (
            row,
            col - 1,
        ) not in visited else None
        _flood_fill(row, col + 1) if (
            row,
            col + 1,
        ) not in visited else None

    basin_sizes = []
    for row, col in low_points:
        size = 0
        visited = set()
        _flood_fill(row, col)
        basin_sizes.append(size)

    return np.prod(sorted(basin_sizes, reverse=True)[:3])
