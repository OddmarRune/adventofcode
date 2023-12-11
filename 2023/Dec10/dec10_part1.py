"""Advent of Code, 2023, Day 10"""

DIRECTIONS = ["|7F ", "L- F", "J -7", " JL|"]
DR = [-1, 0, 0, 1]
DC = [ 0,-1, 1, 0]

def main(filename):
    """Solution to part 1"""
    with open(filename, encoding="UTF-8") as file:
        # Read the pipe chart and find the starting position
        table = []
        for line in file.readlines():
            table.append(line.strip())
            if 'S' in line:
                row, col = len(table), line.find('S')
        rows = len(table)
        cols = len(table[0])

        # Find initial direction and move
        for direction in range(4):
            if 0 <= row+DR[direction] < rows and 0 <= col+DC[direction] < cols \
                    and table[row+DR[direction]][col+DC[direction]] in DIRECTIONS[direction]:
                row += DR[direction]
                col += DC[direction]
                break
        steps = 1

        # Follow the loop and count the steps
        while table[row][col] != 'S':
            direction = DIRECTIONS[direction].find(table[row][col])
            if direction<0:
                break
            row += DR[direction]
            col += DC[direction]
            steps += 1
        print(f"steps to the middle of the loop : {int(steps/2)}")

if __name__ == "__main__":
    main("input.txt")
