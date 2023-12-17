
from parse import parse_input

data = parse_input("input.txt")

def all_zero(l):
    ok = True
    for i in range(len(l)):
        if l[i] != 0:
            ok = False 
    return ok

def reduce_list(l):
    reduced = []
    for i in range(1, len(l)):
        reduced.append(l[i] - l[i-1])
    return reduced

def sol_p1():
    total = 0
    for datum in data:
        data_history = []
        curr = datum
        while (not all_zero(curr)):
            data_history.append(curr)
            curr = reduce_list(curr)
        for hist in data_history:
            total += hist[-1]
    print(total)

def sol_p2():
    total = 0
    for datum in data:
        data_history = []
        curr = datum
        while (not all_zero(curr)):
            data_history.append(curr)
            curr = reduce_list(curr)
        inter_val = 0
        for hist in data_history[::-1]:
            inter_val = hist[0] - inter_val
        total += inter_val
    print(total)

sol_p1()
sol_p2()