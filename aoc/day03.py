from typing import Collection, Counter, List, Text, Tuple


def parse_input(raw_input):
    """transponate a list of strings"""
    transposed_input = ["" for x in range(len(raw_input[0]))]
    for line in raw_input:
        for i, char in enumerate(line):
            transposed_input[i] += char
    return transposed_input


def calculate_power_consumption(lines) -> int:
    lines = parse_input(lines)
    gamma = ""
    for line in lines:
        # count the occurence of each character in the line
        counter = Counter(line)
        if counter["1"] > counter["0"]:
            gamma += "1"
        else:
            gamma += "0"
    epsilon = "".join(["0" if ch == "1" else "1" for ch in gamma])
    return int(epsilon, 2) * int(gamma, 2)


def calculate_life_support_rating(lines) -> int:
    def _loop_lines(lines, mode):
        i = 0
        while len(lines) > 1:
            counter = Counter(parse_input(lines)[i])
            if counter["1"] > counter["0"]:
                if mode == "oxigen":
                    lines = [line for line in lines if line[i] != "0"]
                if mode == "co2":
                    lines = [line for line in lines if line[i] != "1"]
            if counter["1"] < counter["0"]:
                if mode == "oxigen":
                    lines = [line for line in lines if line[i] != "1"]
                if mode == "co2":
                    lines = [line for line in lines if line[i] != "0"]
            else:
                if mode == "oxigen":
                    lines = [line for line in lines if line[i] != "0"]
                if mode == "co2":
                    lines = [line for line in lines if line[i] != "1"]
            i += 1
        return int(lines[0], 2)

    oxygen_generator_rating = _loop_lines(lines, "oxigen")
    co2_rating = _loop_lines(lines, "co2")
    return co2_rating * oxygen_generator_rating
