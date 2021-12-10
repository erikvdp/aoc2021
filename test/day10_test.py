"""--- Day 10: Syntax Scoring ---
https://adventofcode.com/2021/day/10
"""
from aoc.util import read_file_as_list
from aoc.day10 import calculate_score, calculate_score_2

TEST_INPUT = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


PUZZLE_INPUT = read_file_as_list("data/day10.txt")


def test_part_1():
    assert calculate_score(TEST_INPUT) == 26397
    assert calculate_score(PUZZLE_INPUT) == 462693


def test_part_2():
    assert calculate_score_2(TEST_INPUT) == 288957
    assert calculate_score_2(PUZZLE_INPUT) == 3094671161
