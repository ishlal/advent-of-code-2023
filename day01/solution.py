from day01.parse import parse_input

parsed_input = parse_input("input.txt")
def sol_p1():
    summer = 0
    for line in parsed_input:
        tmp = ""
        for s in line:

            # check if s is a digit
            if s.isdigit():
                tmp += s
                break
        for s in line[::-1]:
            # check if s is a digit
            if s.isdigit():
                tmp += s
                break
        summer += int(tmp)
    return summer

def sol_p2():
    words = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9, "zero" : 0,
             "eno" : 1, "owt" : 2, "eerht" : 3, "ruof" : 4, "evif" : 5, "xis" : 6, "neves" : 7, "thgie" : 8, "enin" : 9, "orez" : 0}
    summer = 0
    for line in parsed_input:
        tmp = ""
        inx = 0
        for s in line:
            if s.isdigit():
                tmp += s
                break
            elif line[inx:inx+3] in words:
                tmp += str(words[line[inx:inx+3]])
                break
            elif line[inx:inx+4] in words:
                tmp += str(words[line[inx:inx+4]])
                break
            elif line[inx:inx+5] in words:
                tmp += str(words[line[inx:inx+5]])
                break
            inx+=1
        inx = 0
        rev = line[::-1]
        for s in rev:
            if s.isdigit():
                tmp += s
                break
            elif rev[inx:inx+3] in words:
                tmp += str(words[rev[inx:inx+3]])
                break
            elif rev[inx:inx+4][::-1] in words:
                tmp += str(words[rev[inx:inx+4][::-1]])
                break
            elif rev[inx:inx+5][::-1] in words:
                tmp += str(words[rev[inx:inx+5][::-1]])
                break
            inx+=1
        summer += int(tmp)

    return summer


# print(sol_p1())
print(sol_p2())