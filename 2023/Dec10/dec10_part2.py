"""Advent of Code, 2023, Day 10"""

DIRECTIONS = ["|7FX", "L-XF", "JX-7", "XJL|"]
DR = [-1, 0, 0, 1]
DC = [ 0,-1, 1, 0]

def main():
    """Solution to part 2"""
    with open('input.txt', encoding="UTF-8") as file:
        table = []
        data = []
        output = []
        for line in file.readlines():
            table.append(line.strip())
            data.append([-1]*len(table[-1]))
            output.append(list(" "*len(table[-1])))
            if 'S' in line:
                row, col = len(table), line.find('S')
        rows = len(table)
        cols = len(table[0])
        data[row][col] = 0
        for direction in range(4):
            if 0 <= row+DR[direction] < rows and 0<= col+DC[direction] < cols \
                    and table[row+DR[direction]][col+DC[direction]] in DIRECTIONS[direction]:
                row += DR[direction]
                col += DC[direction]
                break
        steps = 1
        while table[row][col] != 'S':
            data[row][col] = steps
            direction = DIRECTIONS[direction].find(table[row][col])
            if direction<0:
                break
            row += DR[direction]
            col += DC[direction]
            steps += 1
            
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
                    output[row][search_col] = "+" # table[row][search_col]
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

        #for line in output:
        #    print(''.join(line))
        print(f"number of cells inside the loop : {count}")

if __name__ == "__main__":
    main()
