

def parse_input(filename):
    data = []
    with open(filename) as f:
        for line in f:
            datum = line.split(" ")
            for i in range(len(datum)):
                datum[i] = int(datum[i])
            data.append(datum)
    return data