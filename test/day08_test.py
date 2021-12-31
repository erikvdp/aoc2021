"""--- Day 8: Seven Segment Search ---
https://adventofcode.com/2021/day/8
"""
from aoc.day08 import parse_input, calculate_easy_output_values, calculate_output_values
from aoc.util import read_file_as_list

TEST_INPUT_2 = [
    "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
]

TEST_INPUT = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]


PUZZLE_INPUT = read_file_as_list("data/day08.txt")


def test_part_1():
    assert calculate_easy_output_values(parse_input(TEST_INPUT)) == 26
    assert calculate_easy_output_values(parse_input(PUZZLE_INPUT)) == 521


def test_part_2():
    assert calculate_output_values(parse_input(TEST_INPUT)) == 61229
    assert calculate_output_values(parse_input(PUZZLE_INPUT)) == 1016804
