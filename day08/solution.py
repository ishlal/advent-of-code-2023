from parse import parse_input
import numpy as np

move_seq, start, map = parse_input("input.txt")

def sol_p1():
    count = 0
    curr = 'AAA'
    while curr != 'ZZZ':
        step = move_seq[count % len(move_seq)]
        count += 1
        curr = map[curr][0 if step == 'L' else 1]
    print(count)

def sol_p2():
    ends_in_a = []
    for x in list(map.keys()):
        if x[2] == 'A':
            ends_in_a.append(x)
    counts = []
    for elt in ends_in_a:
        count = 0
        curr = elt
        while curr[2] != 'Z':
            step = move_seq[count % len(move_seq)]
            count += 1
            curr = map[curr][0 if step == 'L' else 1]
        counts.append(count)
    lcm = np.lcm.reduce(counts)
    print(lcm)
    


sol_p1()
sol_p2()