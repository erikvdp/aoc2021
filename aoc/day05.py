from collections import defaultdict
from typing import Iterable


def parse_input(lines) -> Iterable[tuple]:
    for line in lines:
        parts = line.strip().split()
        x1, y1 = [int(x) for x in parts[0].split(",")]
        x2, y2 = [int(x) for x in parts[2].split(",")]
        yield (x1, y1), (x2, y2)


def _is_vertical(x1, y1, x2, y2):
    return abs(x1 - x2) == abs(y1 - y2)


def _print_grid(points, grid_size=9):
    for i in range(0, grid_size + 1):
        print("".join([str(points[(j, i)]) for j in range(0, grid_size + 1)]))


def traverse_lines(lines, use_vertical=False):
    grid_size = 0
    points = defaultdict(int)
    for i, ((x1, y1), (x2, y2)) in enumerate(lines):
        print(i)
        grid_size = max([x1, x2, y1, y2, grid_size])
        if use_vertical and _is_vertical(x1, y1, x2, y2):
            # determine if there is a 45 angle vertical line between the 2 points
            diagonal_points = zip(
                list(range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)),
                list(range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)),
            )
            for x, y in diagonal_points:
                points[(x, y)] += 1
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points[(x, y1)] += 1
    # only keep the points which have a larger value than 1
    return len({k: v for k, v in points.items() if v > 1}.keys())
