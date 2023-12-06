from day02.parse import parse_input

parsed_input = parse_input("input.txt")
def sol_p1():
    ans = 0
    for x in parsed_input:
        indx = x[0]
        game = x[1:]
        okay = True
        for g in game:
            for val in g:
                quant, color = val.split(" ")
                if color == "red" and int(quant) > 12:
                    okay = False
                elif color == "blue" and int(quant) > 14:
                    okay = False 
                elif color == "green" and int(quant) > 13:
                    okay = False
        if okay:
            ans += indx
    return ans



def sol_p2():
    ans = 0
    for x in parsed_input:
        indx = x[0]
        games = x[1:]
        okay = True
        blue = 0
        green = 0
        red = 0
        for game in games:
            for obs in game:
                quant, color = obs.split(" ")
                if color == "red":
                    red = max(red, int(quant))
                elif color == "blue":
                    blue = max(blue, int(quant))
                elif color == "green":
                    green = max(green, int(quant))
        ans += (red * blue * green)
    return ans


print(sol_p1())
print(sol_p2())