"""Advent of Code, 2023, Day 10"""

def initial(table, row, col):
    """Find an initial direction"""
    rows = len(table)
    cols = len(table[0])
    if 0 < row < rows and table[row-1][col] in '|F7':
        return 0, row-1, col # up
    elif 0 < col < cols and table[row][col-1] in '-LF':
        return 1, row, col-1 # left
    elif 0 <= col < cols-1 and table[row][col+1] in '-J7':
        return 2, row, col+1 # right
    elif 0 <= row < rows-1 and table[row+1][col] in '|JL':
        return 3, row+1, col # down
    return -1, row, col

DIRECTIONS = ["|7F ", "L- F", "J -7", " JL|"]
DR = [-1, 0, 0, 1]
DC = [ 0,-1, 1, 0]

def follow(table, row, col, direction):
    """Follow the loop"""
    next_direction = DIRECTIONS[direction].find(table[row][col])
    return next_direction, row+DR[next_direction], col+DC[next_direction]

def main():
    """Solution to part 2"""
    with open('input.txt', encoding="UTF-8") as file:
        table = []
        data = []
        output = []
        rows = 0
        for line in file.readlines():
            table.append(line.strip())
            data.append([-1]*len(table[-1]))
            output.append(list(" "*len(table[-1])))
            if 'S' in line:
                start = (rows, line.find('S'))
            rows += 1
        steps = 1
        row, col = start
        data[row][col] = 0
        direction, row, col = initial(table, row, col)
        while table[row][col] != 'S':
            data[row][col] = steps
            direction, row, col = follow(table, row, col, direction)
            steps += 1
            if direction<0:
                break
        circle = 0
        cols = len(table[0])
        for row in range(rows):
            if data[row][0] < 0:
                for col in range(cols):
                    if data[row][col] >= 0:
                        if 0 < row < rows-1:
                            if data[row-1][col] == data[row][col]+1 \
                                or data[row+1][col] == data[row][col]-1:
                                circle = -1
                            else:
                                circle = 1
                        elif row == 0 and col < len(data[row])-1:
                            if data[row][col+1] == data[row][col]+1 \
                                or data[row+1][col] == data[row][col]-1:
                                circle = -1
                            else:
                                circle = 1
                        elif row == rows-1 and col < cols-1:
                            if data[row-1][col] == data[row][col]+1 \
                                or data[row][col+1] == data[row][col]-1:
                                circle = -1
                            else:
                                circle = 1
                    if circle != 0:
                        break
            if circle != 0:
                break
        count = 0
        for row in range(rows):
            for search_col in range(cols):
                col = search_col
                if data[row][col] >= 0:
                    output[row][search_col] = '+'
                    continue
                while col<cols and data[row][col]<0:
                    col += 1
                dcount = 0
                if col<cols:
                    if 0 < row < rows-1:
                        if data[row-1][col] == data[row][col]+1 \
                            or data[row+1][col] == data[row][col]-1:
                            if circle == 1:
                                dcount = 1
                        else:
                            if circle == -1:
                                dcount = 1
                    elif row == 0 and col < cols-1:
                        if data[row][col+1] == data[row][col]+1 \
                            or data[row+1][col] == data[row][col]-1:
                            if circle == 1:
                                dcount = 1
                        else:
                            if circle == -1:
                                dcount = 1
                    elif row == rows-1 and col < cols-1:
                        if data[row-1][col] == data[row][col]+1 \
                            or data[row][col+1] == data[row][col]-1:
                            if circle == 1:
                                dcount = 1
                        else:
                            if circle == -1:
                                dcount = 1
                else:
                    dcount = 0
                count += dcount
                if dcount == 1:
                    output[row][search_col] = 'X'

        # for line in output:
        #     print(''.join(line))
        print(f"number of cells inside the loop : {count}")

if __name__ == "__main__":
    main()