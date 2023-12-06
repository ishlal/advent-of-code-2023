from typing import List

def parse_input(filename):
    res = []
    with open(filename) as f:
        for line in f:
            all_cards = []
            title, card = line.split(":")
            lucky, actual = card.split("|")
            lucky = lucky.strip()
            actual = actual.strip()
            lucky_nums = lucky.split()
            # strip all vals in lucky_nums
            for i in range(len(lucky_nums)):
                lucky_nums[i] = lucky_nums[i].strip()
            actual_nums = actual.split()
            # strip all vals in actual_nums
            for i in range(len(actual_nums)):
                actual_nums[i] = actual_nums[i].strip()
            all_cards.append(lucky_nums)
            all_cards.append(actual_nums)
            res.append(all_cards)
    return res

def parse_input2(filename):
    res = []
    with open(filename) as f:
        for line in f:
            all_cards = []
            title, card = line.split(":")
            num = title.split()[1]
            lucky, actual = card.split("|")
            lucky = lucky.strip()
            actual = actual.strip()
            lucky_nums = lucky.split()
            # strip all vals in lucky_nums
            for i in range(len(lucky_nums)):
                lucky_nums[i] = lucky_nums[i].strip()
            actual_nums = actual.split()
            # strip all vals in actual_nums
            for i in range(len(actual_nums)):
                actual_nums[i] = actual_nums[i].strip()
            all_cards.append(num)
            all_cards.append(lucky_nums)
            all_cards.append(actual_nums)
            res.append(all_cards)
    return res
                



