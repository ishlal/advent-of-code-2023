from typing import List

def parse_input(filename):
    data = []
    with open(filename) as f:
        for line in f:
            datum = []
            hand, val = line.split(" ")
            datum.append(hand)
            datum.append(int(val))
            data.append(datum)
    return data

            
            


                



