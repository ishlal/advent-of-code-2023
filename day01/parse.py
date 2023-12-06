from typing import List

def parse_input(filename):
    res = []
    with open(filename) as f:
        for line in f:
            res.append(line)
    return res