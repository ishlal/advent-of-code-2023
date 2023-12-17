

def parse_input(filename):
    data = []
    with open(filename) as f:
        for line in f:
            datum = []
            for i in line.strip():
                datum.append(i)
            data.append(datum)
    return data