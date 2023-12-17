from day07.parse import parse_input
from day07.parse import parse_input2

parsed_input = parse_input("input.txt")
parsed_input2 = parse_input2("input.txt")
def sol_p1():
    cards = parsed_input
    # print(cards)
    ans = 0
    for i in cards:
        count = 0
        lucky_nums = i[0]
        actual_nums = i[1]
        for num in actual_nums:
            if num in lucky_nums:
                count += 1
        if count != 0:
            ans += (2**(count - 1))
    return ans



def sol_p2():
    ans = 0
    cards = parsed_input2
    counts = [1] * len(cards)
    for i in range(len(cards)):
        lucky_nums = cards[i][1]
        actual_nums = cards[i][2]
        count = 0
        for num in actual_nums:
            if num in lucky_nums:
                count += 1
        for j in range(i+1, min(i+1+count, len(counts))):
            counts[j] += counts[i]
    for i in range(len(counts)):
        ans += counts[i]
    return ans
        


# print(sol_p1())
print(sol_p2())