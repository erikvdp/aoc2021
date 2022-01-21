"""--- Day 13: Transparent Origami ---
https://adventofcode.com/2021/day/13
"""
from aoc.util import read_file_as_list
from aoc.day13 import parse_input, perform_folds

TEST_INPUT = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5",
]

PUZZLE_INPUT = read_file_as_list("data/day13.txt")


def test_part_1():
    dots, folds = parse_input(TEST_INPUT)
    assert perform_folds(dots, folds, 1) == 17
    dots, folds = parse_input(PUZZLE_INPUT)
    assert perform_folds(dots, folds, 1) == 747


def test_part_2():
    dots, folds = parse_input(PUZZLE_INPUT)
    assert perform_folds(dots, folds) == 102
