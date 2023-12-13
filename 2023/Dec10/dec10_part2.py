"""Advent of Code, 2023, Day 10"""

DIRECTIONS = ["|7F ", "L- F", "J -7", " JL|"]
DR = [-1, 0, 0, 1]
DC = [ 0,-1, 1, 0]
PIPES = {'|':'║', 'F':'╔', '-':'═', '7':'╗', 'J':'╝', 'L':'╚', 'S':'@' }

UNDETERMINED = 0
CLOCKWISE = -1
COUNTERCLOCKWISE = 1

def main(filename):
    """Solution to part 2"""
    with open(filename, encoding="UTF-8") as file:
        # Read the pipe chart and find the starting position
        table = []
        for line in file.readlines():
            table.append(line.strip())
            if 'S' in line:
                row, col = len(table)-1, line.find('S')
        rows = len(table)
        cols = len(table[0])

        data = [[-1] * cols for _ in range(rows)]
        output = [[' '] * cols for _ in range(rows)]

        # Find initial direction and move
        data[row][col] = 0
        for direction in range(4):
            if 0 <= row+DR[direction] < rows and 0<= col+DC[direction] < cols \
                    and table[row+DR[direction]][col+DC[direction]] in DIRECTIONS[direction]:
                row += DR[direction]
                col += DC[direction]
                break
        steps = 1

        # Follow the loop and store step-counter in pipe
        while table[row][col] != 'S':
            data[row][col] = steps
            direction = DIRECTIONS[direction].find(table[row][col])
            if direction<0:
                break
            row += DR[direction]
            col += DC[direction]
            steps += 1

        # Determine the loop direction
        loop_direction = UNDETERMINED
        cols = len(table[0])
        for row in range(rows):
            for col in range(cols):
                if data[row][col] < 0:
                    continue
                if 0 < row < rows-1:
                    if data[row-1][col] == (data[row][col]+1)%steps \
                        or data[row+1][col] == (data[row][col]-1)%steps:
                        loop_direction = CLOCKWISE
                    else:
                        loop_direction = COUNTERCLOCKWISE
                elif row == 0 and col < len(data[row])-1:
                    if data[row][col+1] == (data[row][col]+1)%steps \
                        or data[row+1][col] == (data[row][col]-1)%steps:
                        loop_direction = CLOCKWISE
                    else:
                        loop_direction = COUNTERCLOCKWISE
                elif row == rows-1 and col < cols-1:
                    if data[row-1][col] == (data[row][col]+1)%steps \
                        or data[row][col+1] == (data[row][col]-1)%steps:
                        loop_direction = CLOCKWISE
                    else:
                        loop_direction = COUNTERCLOCKWISE
                if loop_direction != UNDETERMINED:
                    break
            if loop_direction != UNDETERMINED:
                break

        # Find all enclosed cells
        count = 0
        for row in range(rows):
            for search_col in range(cols):
                col = search_col
                if data[row][search_col] >= 0:
                    output[row][search_col] = PIPES[table[row][search_col]]
                    continue
                while col<cols and data[row][col]<0:
                    col += 1
                dcount = 0
                if col<cols:
                    if 0 < row < rows-1:
                        if data[row-1][col] == (data[row][col]+1)%steps \
                            or data[row+1][col] == (data[row][col]-1)%steps:
                            if loop_direction == COUNTERCLOCKWISE:
                                dcount = 1
                        else:
                            if loop_direction == CLOCKWISE:
                                dcount = 1
                    elif row == 0 and col < cols-1:
                        if data[row][col+1] == (data[row][col]+1)%steps \
                            or data[row+1][col] == (data[row][col]-1)%steps:
                            if loop_direction == COUNTERCLOCKWISE:
                                dcount = 1
                        else:
                            if loop_direction == CLOCKWISE:
                                dcount = 1
                    elif row == rows-1 and col < cols-1:
                        if data[row-1][col] == (data[row][col]+1)%steps \
                            or data[row][col+1] == (data[row][col]-1)%steps:
                            if loop_direction == COUNTERCLOCKWISE:
                                dcount = 1
                        else:
                            if loop_direction == CLOCKWISE:
                                dcount = 1
                else:
                    dcount = 0
                count += dcount
                if dcount == 1:
                    output[row][search_col] = 'I'

        for line in output:
            print(''.join(line))
        print(f"number of cells inside the loop : {count}")

if __name__ == "__main__":
    main("input.txt")
