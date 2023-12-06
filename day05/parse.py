from typing import List

def parse_input(filename):
    res = [[], [], [], [], [], [], [], []]
    with open(filename) as f:
        curr_indx = 0
        for line in f:
            if ":" in line:
                label, vals = line.split(":")
                if label == "seeds":
                    split_vals = vals.strip().split()
                    for i in range(len(split_vals)):
                        split_vals[i] = int(split_vals[i])
                    res[0] = split_vals
                elif label == "seed-to-soil map":
                    curr_indx = 1
                elif label == "soil-to-fertilizer map":
                    curr_indx = 2
                elif label == "fertilizer-to-water map":
                    curr_indx = 3
                elif label == "water-to-light map":
                    curr_indx = 4
                elif label == "light-to-temperature map":
                    curr_indx = 5
                elif label == "temperature-to-humidity map":
                    curr_indx = 6
                elif label == "humidity-to-location map":
                    curr_indx = 7
            elif line != '\n':
                nums = line.split()
                for i in range(len(nums)):
                    nums[i] = int(nums[i])
                curr_res = res[curr_indx]
                curr_res.append(nums)
                res[curr_indx] = curr_res
    return res
            
            


                



