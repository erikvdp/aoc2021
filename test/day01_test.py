"""--- Day 1: Sonar Sweep ---
https://adventofcode.com/2021/day/1
"""
from aoc.day01 import count_increases, sliding_window_count_increases
from aoc.util import read_file_as_list

TEST_INPUT = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

PUZZLE_INPUT = [int(x) for x in read_file_as_list("data/day01.txt")]


def test_part_1():
    assert count_increases(TEST_INPUT) == 7
    assert count_increases(PUZZLE_INPUT) == 1722


def test_part_2():
    assert sliding_window_count_increases(TEST_INPUT, 3) == 5
    assert sliding_window_count_increases(PUZZLE_INPUT, 3) == 1748
