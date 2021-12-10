from typing import List, Text, Tuple


def parse_input(raw_input):
    return [(x.split()[0], int(x.split()[1])) for x in raw_input]


def traverse_path(commands: List[Tuple[Text, int]]) -> int:
    x = 0
    y = 0
    for direction, distance in commands:
        if direction == "forward":
            x += distance
        elif direction == "down":
            y += distance
        elif direction == "up":
            y -= distance
    return x * y


def traverse_path_2(commands: List[Tuple[Text, int]]) -> int:
    x = 0
    y = 0
    aim = 0
    for direction, distance in commands:
        if direction == "forward":
            x += distance
            y += aim * distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
    return x * y
