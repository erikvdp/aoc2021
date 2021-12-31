"""--- Day 11: Dumbo Octopus ---
https://adventofcode.com/2021/day/11
"""
from aoc.util import read_file_as_list
from aoc.day11 import caculate_flashes, parse_input, calculate_synchronization

TEST_INPUT = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
]


PUZZLE_INPUT = read_file_as_list("data/day11.txt")


def test_part_1():
    assert caculate_flashes(parse_input(TEST_INPUT), 100) == 1656
    assert caculate_flashes(parse_input(PUZZLE_INPUT), 100) == 1697


def test_part_2():
    assert calculate_synchronization(parse_input(TEST_INPUT)) == 195
    assert calculate_synchronization(parse_input(PUZZLE_INPUT)) == 344
