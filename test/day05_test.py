"""--- Day 5: Hydrothermal Venture ---
https://adventofcode.com/2021/day/5
"""
from aoc.day05 import parse_input, traverse_lines
from aoc.util import read_file_as_list

TEST_INPUT = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]


PUZZLE_INPUT = read_file_as_list("data/day05.txt")


def test_part_1():
    assert traverse_lines(parse_input(TEST_INPUT)) == 5
    assert traverse_lines(parse_input(PUZZLE_INPUT)) == 5774


def test_part_2():
    assert traverse_lines(parse_input(TEST_INPUT), use_vertical=True) == 12
    assert traverse_lines(parse_input(PUZZLE_INPUT), use_vertical=True) == 18423
