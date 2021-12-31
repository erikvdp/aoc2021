"""--- Day 12: Passage Pathing ---
https://adventofcode.com/2021/day/12
"""
from aoc.util import read_file_as_list
from aoc.day12 import parse_input, calculate_paths_1, calculate_paths_2

TEST_INPUT_1 = ["start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"]
TEST_INPUT_2 = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc",
]
TEST_INPUT_3 = [
    "fs-end",
    "he-DX",
    "fs-he",
    "start-DX",
    "pj-DX",
    "end-zg",
    "zg-sl",
    "zg-pj",
    "pj-he",
    "RW-he",
    "fs-DX",
    "pj-RW",
    "zg-RW",
    "start-pj",
    "he-WI",
    "zg-he",
    "pj-fs",
    "start-RW",
]

PUZZLE_INPUT = read_file_as_list("data/day12.txt")


def test_part_1():
    assert calculate_paths_1(parse_input(TEST_INPUT_1)) == 10
    assert calculate_paths_1(parse_input(TEST_INPUT_2)) == 19
    assert calculate_paths_1(parse_input(TEST_INPUT_3)) == 226
    assert calculate_paths_1(parse_input(PUZZLE_INPUT)) == 4912


def test_part_2():
    assert calculate_paths_2(parse_input(TEST_INPUT_1)) == 36
    assert calculate_paths_2(parse_input(TEST_INPUT_2)) == 103
    assert calculate_paths_2(parse_input(TEST_INPUT_3)) == 3509
    assert calculate_paths_2(parse_input(PUZZLE_INPUT)) == 150004
