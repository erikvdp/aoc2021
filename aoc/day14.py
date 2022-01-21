from typing import Dict, Text, Tuple
from collections import Counter
import copy


def parse_input(lines) -> Tuple[Text, Dict]:
    template = lines[0]
    rules = dict()
    for line in lines[2:]:
        key, _, value = line.split(" ")
        rules[key] = value
    return template, rules


def polymerise(template, rules, n_rounds) -> int:
    counts = Counter()
    starting_kmers = [template[i : i + 2] for i in range(len(template) - 1)]
    for c in starting_kmers:
        for i in range(n_rounds):
            new_template = c[0]
            # generate kmers
            kmers = [c[i : i + 2] for i in range(len(c) - 1)]
            for kmer in kmers:
                new_template += rules[kmer] + kmer[1]
            c = new_template
        counts += Counter(c)
    return max(counts.values()) - min(counts.values())


def polymerise_fast(template, rules, n_rounds) -> int:
    totals = Counter()
    kmers = Counter([template[i : i + 2] for i in range(len(template) - 1)])
    for i in range(n_rounds):
        for kmer, amount in copy.deepcopy(kmers).items():
            if amount > 0:
                new_kmer_1 = kmer[0] + rules[kmer]
                new_kmer_2 = rules[kmer] + kmer[1]
                kmers.update({new_kmer_1: amount})
                kmers.update({new_kmer_2: amount})
                kmers.update({kmer: -amount})
    totals = Counter()
    for kmer, amount in kmers.items():
        totals.update({kmer[0]: amount})
    totals.update({template[-1]: 1})
    return max(totals.values()) - min(totals.values())
