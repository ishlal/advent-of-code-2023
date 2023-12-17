from parse import parse_input


parsed_input = parse_input("input.txt")

types = {"FIVE_OF_KIND": 7, 
         "FOUR_OF_KIND": 6, 
         "FULL_HOUSE": 5, 
         "THREE_OF_KIND": 4, 
         "TWO_PAIRS": 3, 
         "ONE_PAIR": 2, 
         "HIGH": 1}

card_to_value = {
    '': 0,
    '2': 1,
    '3' : 2, 
    '4' : 3,
    '5' : 4,
    '6' : 5,
    '7' : 6, 
    '8' : 7,
    '9' : 8,
    'T' : 9,
    'J' : 10,
    'Q' : 11, 
    'K' : 12,
    'A' : 13
}

def get_type(hand_dict):
    # print(hand_dict)
    keys = list(hand_dict.keys())
    # print(keys)
    if len(hand_dict) == 1:
        return types["FIVE_OF_KIND"]
    elif len(hand_dict) == 2:
        # four of a kind or full house
        if hand_dict[keys[0]] == 4 or hand_dict[keys[1]] == 4:
            return types["FOUR_OF_KIND"]
        else:
            return types["FULL_HOUSE"]
    elif len(hand_dict) == 3:
        if hand_dict[keys[0]] == 3 or hand_dict[keys[1]] == 3 or hand_dict[keys[2]] == 3:
            return types["THREE_OF_KIND"]
        else:
            return types["TWO_PAIRS"]
    elif len(hand_dict) == 4:
        return types["ONE_PAIR"]
    else:
        return types["HIGH"]
    


def convert_string_to_dict(hand1):
    # print("aosdhfopasfhd: ", hand1)
    hand1_copy = hand1
    hand1 = ''.join(sorted(hand1))
    hand1_dict = {}
    for cha in hand1:
        if cha not in hand1_dict:
            hand1_dict[cha] = 1
        else:
            hand1_dict[cha] = hand1_dict[cha] + 1
    # print("hand1_dict: ", hand1_dict)
    return hand1_dict


def less_than(hand1_dict, hand2_dict, hand1_copy, hand2_copy):
    # print("hand1_dict: ", hand1_dict)
    # print("hand1_copy: ", hand1_copy)
    # print("hand2_dict: ", hand2_dict)
    # print("hand2_copy: ", hand2_copy)

    type_hand1 = get_type(hand1_dict)
    type_hand2 = get_type(hand2_dict)
    if type_hand1 < type_hand2:
        return True
    elif type_hand1 > type_hand2:
        return False
    else: 
        char_of_first_diff = 0
        for i in range(len(hand1_copy)):
            if hand1_copy[i] != hand2_copy[i]:
                char_of_first_diff = i 
                break
        hand_1_diff_val = card_to_value[hand1_copy[char_of_first_diff]]
        hand_2_diff_val = card_to_value[hand2_copy[char_of_first_diff]]
        return hand_1_diff_val < hand_2_diff_val


def sol_p1():
    data = parsed_input
    sorted_data = [data[0]]
    # insertion sort
    for datum in data[1:]:
        inserted = False
        for j in range(len(sorted_data)):
            elt = sorted_data[j]
            # compare. if datum[i] < elt, insert datum before elt
            # print(elt)
            dict_datum_0 = convert_string_to_dict(datum[0])
            dict_elt_0 = convert_string_to_dict(elt[0])
            if less_than(dict_datum_0, dict_elt_0, datum[0], elt[0]):
                sorted_data.insert(j, datum)
                inserted = True
                break 
        if not inserted:
            sorted_data.append(datum)
    answer = 0
    for i in range(len(sorted_data)):
        answer += ((i+1) * sorted_data[i][1])
    print(answer)

def adjust(datum):
    # takes in a hand, val pair
    hand = datum[0]
    # print("HAND: ", hand)
    max_count = 0
    max_count_key = ''
    hand_as_dict = convert_string_to_dict(hand)
    count_num_j = 0
    for i in list(hand_as_dict.keys()):
        if i == 'J':
            count_num_j += 1
    if 'J' not in list(hand_as_dict.keys()):
        return hand_as_dict, datum[1]
    elif count_num_j == 1 and len(list(hand_as_dict.keys())) == 1:
        return {'A': 5}, datum[1]
    else: 
        for i in list(hand_as_dict.keys()):
            if hand_as_dict[i] > max_count:
                if i != 'J':
                    max_count = hand_as_dict[i]
                    max_count_key = i
            elif hand_as_dict[i] == max_count:
                if (card_to_value[i] > card_to_value[max_count_key]):
                        max_count_key = i
        
        hand_as_dict[max_count_key] += hand_as_dict['J']
        del hand_as_dict['J']
        return hand_as_dict, datum[1]

        

    # less_than takes the two strings

def adjusted_dictionary_to_string(my_dict):
    s = ""
    for i in list(my_dict.keys()):
        for j in range(my_dict[i]):
            s += i 
    return s

def get_most_frequent_letter(my_dict):
    max_count = 0
    for i in list(my_dict.keys()):
        max(max_count, my_dict[i])
    

def replace_string(string_with_js, character):
    s = ""
    for i in string_with_js:
        if i != 'J':
            s += i
        else:
            s += character
    return s


def sol_p2():
    data = parsed_input
    adjust_0 = adjust(data[0])
    # print("ADJUSTED 0 -------- : ", adjust_0)
    sorted_data = [(adjust_0, data[0])]
    # insertion sort
    for datum in data[1:]:
        inserted = False
        print(sorted_data)
        print("\n")
        for j in range(len(sorted_data)):
            elt = sorted_data[j]
            actual_dictionary = elt[0]
            # print("ACTUAL DICTIONARY: ", actual_dictionary)
            actual_string = adjusted_dictionary_to_string(actual_dictionary, elt[2])
            # print("full datum: ", datum)
            # print("DATUM: ", datum[0])
            # print("param 1: ", adjust(datum)[0])
            # print("param 2: ", actual_dictionary)
            # print("param 3: ", datum[0])
            # print("param 4: ", actual_string)
            if less_than(adjust(datum)[0], actual_dictionary, datum[0], actual_string):
                sorted_data.insert(j, (convert_string_to_dict(datum[0]), datum[1]))
                inserted = True
                break 
        if not inserted:
            # print(datum[1])
            sorted_data.append((convert_string_to_dict(datum[0]), datum[1]))
    answer = 0
    for i in range(len(sorted_data)):
        answer += ((i+1) * sorted_data[i][1])
    print(answer)





# sol_p1()
sol_p2()
# print(adjust(['KTJJT', 123]))