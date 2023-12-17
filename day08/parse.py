

def parse_input(filename):
    map = {}
    with open(filename) as f:
        move_seq = f.readline().strip()
        f.readline()
        count = 0
        start = ""
        for line in f:
            key, values = line.split("=")
            key = key.strip()
            values = values.strip()
            value_1 = values[1:4]
            value_2 = values[6:9]
            map[key] = [value_1, value_2]
            if (count == 0):
                count+=1
                start = key
    return move_seq, start, map
