"""--- Day 6: Lanternfish ---
https://adventofcode.com/2021/day/6
"""
from aoc.day06 import simulate_days, simulate_days_2, parse_input
from aoc.util import read_file_as_list

TEST_INPUT = ["3,4,3,1,2"]


PUZZLE_INPUT = read_file_as_list("data/day06.txt")


def test_part_1():
    assert simulate_days_2(parse_input(TEST_INPUT), 80) == 5934
    assert simulate_days_2(parse_input(PUZZLE_INPUT), 80) == 386755


def test_part_2():
    assert simulate_days_2(parse_input(TEST_INPUT), 256) == 26984457539
    assert simulate_days_2(parse_input(PUZZLE_INPUT), 256) == 1732731810807
