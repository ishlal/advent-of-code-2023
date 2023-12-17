from day07.parse import parse_input


parsed_input = parse_input()
def sol_p1():
    data = parsed_input
    ans = 1
    for i in data:
        time = i[0]
        distance = i[1]
        count = 0
        for j in range(1, time):
            # j will be the speed of the thingy
            if (distance < (time - j)*j):
                count += 1
        ans *= count 
    print(ans)

def sol_p2():
    data = parsed_input
    time = ""
    distance = ""
    for i in data:
        time += str(i[0])
        distance += str(i[1])
    count = 0
    time = int(time)
    distance = int(distance)
    for j in range(1, time):
        if (distance < (time - j) * j):
            count += 1
    print(count)


sol_p1()
sol_p2()