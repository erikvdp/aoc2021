"""--- Day 3: Binary Diagnostic ---
https://adventofcode.com/2021/day/3
"""
from aoc.day03 import calculate_life_support_rating, calculate_power_consumption
from aoc.util import read_file_as_list

TEST_INPUT = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

PUZZLE_INPUT = read_file_as_list("data/day03.txt")


def test_part_1():
    assert calculate_power_consumption(TEST_INPUT) == 198
    assert calculate_power_consumption(PUZZLE_INPUT) == 3374136


def test_part_2():
    assert calculate_life_support_rating(TEST_INPUT) == 230
    assert calculate_life_support_rating(PUZZLE_INPUT) == 4432698
