"""--- Day 2: Dive! ---
https://adventofcode.com/2021/day/2
"""
from aoc.day02 import parse_input, traverse_path, traverse_path_2
from aoc.util import read_file_as_list

TEST_INPUT = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

PUZZLE_INPUT = read_file_as_list("data/day02.txt")


def test_part_1():
    assert traverse_path(parse_input(TEST_INPUT)) == 150
    assert traverse_path(parse_input(PUZZLE_INPUT)) == 2322630


def test_part_2():
    assert traverse_path_2(parse_input(TEST_INPUT)) == 900
    assert traverse_path_2(parse_input(PUZZLE_INPUT)) == 2105273490
