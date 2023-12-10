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
    """Solution to part 1"""
    with open('input.txt', encoding="UTF-8") as file:
        table = []
        rows = 0
        for line in file.readlines():
            table.append(line.strip())
            if 'S' in line:
                start = (rows, line.find('S'))
            rows += 1
        steps = 1
        row, col = start
        print(f"start : {row}, {col}, {table[row][col]}")
        direction, row, col = initial(table, row, col)
        while table[row][col] != 'S':
            direction, row, col = follow(table, row, col, direction)
            steps += 1
            if direction<0:
                break

        print(f"steps to the middle of loop : {int(steps/2)}") # 7173

if __name__ == "__main__":
    main()
