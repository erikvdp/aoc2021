"""--- Day 13: Transparent Origami ---
https://adventofcode.com/2021/day/13
"""
from aoc.util import read_file_as_list
from aoc.day14 import parse_input, polymerise, polymerise_fast

TEST_INPUT = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C",
]

PUZZLE_INPUT = read_file_as_list("data/day14.txt")


def test_part_1():
    template, rules = parse_input(TEST_INPUT)
    assert polymerise(template, rules, 10) == 1588
    template, rules = parse_input(PUZZLE_INPUT)
    assert polymerise(template, rules, 10) == 3697


def test_part_2():
    template, rules = parse_input(TEST_INPUT)
    assert polymerise_fast(template, rules, 40) == 2188189693529
    template, rules = parse_input(PUZZLE_INPUT)
    assert polymerise_fast(template, rules, 40) == 4371307836157
