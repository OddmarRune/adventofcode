"""Advent of Code, 2023, Day 10"""

DIRECTIONS = ["|7F ", "L- F", "J -7", " JL|"]
DR = [-1, 0, 0, 1]
DC = [ 0,-1, 1, 0]
PIPES = {'|':'║', 'F':'╔', '-':'═', '7':'╗', 'J':'╝', 'L':'╚', 'S':'S' }

UNDETERMINED = 0
CLOCKWISE = 1
COUNTERCLOCKWISE = -1

def main(filename):
    """Solution to both part 1 and part 2"""
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

        # Follow the loop, store step-counter in pipe and determine loop direction
        lower_row_limit = rows
        loop_direction = UNDETERMINED
        while table[row][col] != 'S':
            data[row][col] = steps
            direction = DIRECTIONS[direction].find(table[row][col])
            if direction<0:
                break
            row += DR[direction]
            col += DC[direction]
            if row<lower_row_limit and DC[direction] != 0:
                lower_row_limit = row
                loop_direction = DC[direction]
            steps += 1

        print(f"Part 1 : steps to the middle of the loop : {int(steps/2)}")

        # Find all enclosed cells
        count = 0
        for row in range(rows):
            delta_count = 0
            for search_col in range(cols):
                col = search_col
                if data[row][search_col] >= 0:
                    output[row][search_col] = PIPES[table[row][search_col]]
                    delta_count = 0
                    continue
                elif delta_count == 1:
                    count += delta_count
                    output[row][search_col] = 'I'
                    continue
                delta_count = 0

                while col<cols and data[row][col]<0:
                    col += 1
                if col<cols:
                    if 0 < row < rows-1:
                        if data[row-1][col] == (data[row][col]+1)%steps \
                            or data[row+1][col] == (data[row][col]-1)%steps:
                            if loop_direction == COUNTERCLOCKWISE:
                                delta_count = 1
                        else:
                            if loop_direction == CLOCKWISE:
                                delta_count = 1
                else:
                    delta_count = 0
                count += delta_count
                if delta_count == 1:
                    output[row][search_col] = 'I'
        print("The Map:")
        for line in output:
            print(''.join(line))
        print(f"Part 2: number of cells inside the loop : {count}")

if __name__ == "__main__":
    main("input.txt")
