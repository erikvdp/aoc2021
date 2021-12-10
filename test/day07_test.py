"""--- Day 6: Lanternfish ---
https://adventofcode.com/2021/day/6
"""
from aoc.day07 import (
    calculate_cheapest_outcome_2,
    parse_input,
    calculate_cheapest_outcome,
)
from aoc.util import read_file_as_list

TEST_INPUT = ["16,1,2,0,4,2,7,1,2,14"]


PUZZLE_INPUT = read_file_as_list("data/day07.txt")


def test_part_1():
    assert calculate_cheapest_outcome(parse_input(TEST_INPUT)) == 37
    assert calculate_cheapest_outcome(parse_input(PUZZLE_INPUT)) == 323647


def test_part_2():
    assert calculate_cheapest_outcome_2(parse_input(TEST_INPUT)) == 168
    assert calculate_cheapest_outcome_2(parse_input(PUZZLE_INPUT)) == 87640209
