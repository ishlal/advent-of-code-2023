from parse import parse_input

galaxy = parse_input("input.txt")

def is_empty(line):
    for i in line:
        if i != '.':
            return False
    return True

def is_empty_col(col, galaxy):
    for i in range(len(galaxy)):
        if galaxy[i][col] != '.':
            return False 
    return True

def sol_p1():
    empty_rows = []
    updated_galaxy = []
    blank_row = ['.']*len(galaxy[0])

    for row in range(len(galaxy)):
        updated_galaxy.append(galaxy[row])
        if is_empty(galaxy[row]):
            updated_galaxy.append(blank_row.copy())
            empty_rows.append(row)

    for i in updated_galaxy:
        print(i)
    empty_cols = []
    for col in range(len(galaxy[0])):
        if is_empty_col(col, galaxy):
            empty_cols.append(col)
    print(empty_cols)
    for i in empty_cols[::-1]:
        print(i)
        # expand cols
        for row in range(len(updated_galaxy)):
            updated_galaxy[row].insert(i, '.')
    tags = []
    for i in range(len(updated_galaxy)):
        for j in range(len(updated_galaxy[0])):
            if updated_galaxy[i][j] == '#':
                tags.append((i, j))
    ans = 0
    for i in range(len(tags)):
        for j in range(i, len(tags)):
            ans += abs(tags[i][0] - tags[j][0])
            ans += abs(tags[i][1] - tags[j][1])
    print(ans)

    
sol_p1()
