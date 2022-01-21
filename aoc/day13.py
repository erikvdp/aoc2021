from typing import Dict, List, Set, Text, Tuple
from collections import Counter


def parse_input(lines) -> Tuple[Set, List]:
    folds = list()
    dots = set()
    for line in lines:
        if line != "":
            if line.startswith("fold"):
                fold = line.split(" ")[-1].split("=")
                folds.append((str(fold[0]), int(fold[1])))
            else:
                x, y = line.split(",")
                dots.add((int(x), int(y)))
    return dots, folds


def print_code(coords):
    # get max x and y
    with open("day13_code.txt", "w") as f:

        max_x = max(coords, key=lambda x: x[0])[0]
        max_y = max(coords, key=lambda x: x[1])[1]
        for y in range(100):
            line = ""
            for x in range(100):
                if (x, y) in coords:
                    line += "#"
                else:
                    line += "."
            f.write(line + "\n")


def perform_folds(dots, folds, lim=None) -> int:
    lim = lim or len(folds)
    for i in range(lim):
        direction, mirror = folds[i]
        for dot in list(dots):
            dots.remove(dot)
            if direction == "x":
                if mirror < dot[0]:
                    new_x = dot[0] - 2 * (dot[0] - mirror)
                else:
                    new_x = dot[0]
                dots.add((new_x, dot[1]))
            elif direction == "y":
                if mirror < dot[1]:
                    new_y = dot[1] - 2 * (dot[1] - mirror)
                else:
                    new_y = dot[1]
                dots.add((dot[0], new_y))
    print_code(dots)
    return len(dots)
