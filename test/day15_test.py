"""--- Day 15: Chiton ---
https://adventofcode.com/2021/day/15
"""
from aoc.util import read_file_as_list
from aoc.day15 import calculate_min_cost_path, parse_input, parse_input_2

TEST_INPUT = [
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581",
]

TEST_INPUT_2 = ["19999", "19111", "11191"]

PUZZLE_INPUT = read_file_as_list("data/day15.txt")


def test_part_1():
    assert calculate_min_cost_path(parse_input(TEST_INPUT)) == 40
    assert calculate_min_cost_path(parse_input(TEST_INPUT_2)) == 8
    assert calculate_min_cost_path(parse_input(PUZZLE_INPUT)) == 656


def test_part_2():
    assert calculate_min_cost_path(parse_input_2(TEST_INPUT)) == 315
    assert calculate_min_cost_path(parse_input_2(PUZZLE_INPUT)) == 2979
