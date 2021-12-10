"""--- Day 9: Smoke Basin ---
https://adventofcode.com/2021/day/9
"""
from aoc.day09 import parse_input, calculate_risk_level, calculate_basins
from aoc.util import read_file_as_list

TEST_INPUT = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]


PUZZLE_INPUT = read_file_as_list("data/day09.txt")


def test_part_1():
    assert calculate_risk_level(parse_input(TEST_INPUT)) == 15
    assert calculate_risk_level(parse_input(PUZZLE_INPUT)) == 448


def test_part_2():
    assert calculate_basins(parse_input(TEST_INPUT)) == 1134
    assert calculate_basins(parse_input(PUZZLE_INPUT)) == 1417248
