from parse import parse_input

def get_output(input, list_of_lists):
    # given input x, return coded version:
    for rang in list_of_lists:
        if input <= rang[1] + rang[2] and input >= rang[1]:
            # print("HSDf")
            return rang[0] + (input - rang[1])
    return input

parsed_input = parse_input("input.txt")
def sol_p1():
    res = parsed_input
    # print(res)
    seeds = res[0]
    asdf = []
    for i in seeds:
        v1 = get_output(i, res[1])
        v2 = get_output(v1, res[2])
        v3 = get_output(v2, res[3])
        v4 = get_output(v3, res[4])
        v5 = get_output(v4, res[5])
        v6 = get_output(v5, res[6])
        v7 = get_output(v6, res[7])
        asdf.append(v7)
    print(min(asdf))

def sol_p2():
    res = parsed_input
    seeds = res[0]
    asdf = []
    for i in range(0, len(seeds), 2):
        seed = seeds[i]
        length = seeds[i+1]
        for j in range(seed, seed+length):
            v1 = get_output(i, res[1])
            v2 = get_output(v1, res[2])
            v3 = get_output(v2, res[3])
            v4 = get_output(v3, res[4])
            v5 = get_output(v4, res[5])
            v6 = get_output(v5, res[6])
            v7 = get_output(v6, res[7])
            asdf.append(v7)
    print(min(asdf))

sol_p1()
sol_p2()
# print(get_output(79, [[50, 98, 2], [52, 50, 48]]))