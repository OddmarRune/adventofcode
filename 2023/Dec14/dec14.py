"""Advent of Code, 2023, Day 14"""

def north(disc):
    """Tilt North"""
    rows, cols =  len(disc), len(disc[0])
    for c in range(cols):
        o_count = 0
        o_start = 0
        for r in range(rows):
            if disc[r][c] == 'O':
                o_count += 1
            elif disc[r][c] == '#':
                for x in range(o_start, o_start+o_count):
                    disc[x][c] = 'O'
                for x in range(o_start+o_count, r):
                    disc[x][c] = '.'
                o_count = 0
                o_start = r+1
        if o_count > 0:
            for x in range(o_start, o_start+o_count):
                disc[x][c] = 'O'
            for x in range(o_start+o_count, len(disc)):
                disc[x][c] = '.'

def west(disc):
    """Tilt West"""
    rows, cols =  len(disc), len(disc[0])
    for r in range(rows):
        o_count = 0
        o_start = 0
        for c in range(cols):
            if disc[r][c] == 'O':
                o_count += 1
            elif disc[r][c] == '#':
                for x in range(o_start, o_start+o_count):
                    disc[r][x] = 'O'
                for x in range(o_start+o_count, c):
                    disc[r][x] = '.'
                o_count = 0
                o_start = c+1
        if o_count > 0:
            for x in range(o_start, o_start+o_count):
                disc[r][x] = 'O'
            for x in range(o_start+o_count, cols):
                disc[r][x] = '.'

def south(disc):
    """Tilt South"""
    rows, cols =  len(disc), len(disc[0])
    for c in range(cols):
        o_count = 0
        o_start = rows-1
        for r in range(rows-1,-1,-1):
            if disc[r][c] == 'O':
                o_count += 1
            elif disc[r][c] == '#':
                for x in range(o_start, o_start-o_count,-1):
                    disc[x][c] = 'O'
                for x in range(o_start-o_count, r, -1):
                    disc[x][c] = '.'
                o_count = 0
                o_start = r-1
        if o_count > 0:
            for x in range(o_start, o_start-o_count, -1):
                disc[x][c] = 'O'
            for x in range(o_start-o_count, -1, -1):
                disc[x][c] = '.'

def east(disc):
    """Tilt East"""
    rows, cols =  len(disc), len(disc[0])
    for r in range(rows):
        o_count = 0
        o_start = cols-1
        for c in range(cols-1,-1,-1):
            if disc[r][c] == 'O':
                o_count += 1
            elif disc[r][c] == '#':
                for x in range(o_start, o_start-o_count, -1):
                    disc[r][x] = 'O'
                for x in range(o_start-o_count, c, -1):
                    disc[r][x] = '.'
                o_count = 0
                o_start = c-1
        if o_count > 0:
            for x in range(o_start, o_start-o_count, -1):
                disc[r][x] = 'O'
            for x in range(o_start-o_count, -1, -1):
                disc[r][x] = '.'

def cycle(disc, reps=1):
    """Calculate repeated cycles, detecting period"""
    cache = {}
    initial = -1
    period = -1
    for i in range(reps):
        key = "".join(["".join(line) for line in disc])
        if key in cache:
            if initial<0:
                initial = i
                print(f"    initial = {initial:5d}")
            if cache[key] == 2 and period < 0 and i > initial:
                period = i - initial
                print(f"    period =  {period:5d}")
            cache[key] += 1
        else:
            cache[key] = 1  
        if period>0 and initial>=0 and i>initial and (reps-initial)%period == (i-initial)%period:
            print("Calculations:")
            print(f"     {reps:15d} = {initial} + k*{period} + {(i-initial)%period}")            
            print(f"     {i:15d} = {initial} + 1*{period} + {(i-initial)%period}")
            break
        north(disc)
        west(disc)
        south(disc)
        east(disc)

def load(disc):
    """Calculate load"""
    total = 0
    for r, line in enumerate(disc):
        c = 0
        for element in line:
            if element == 'O':
                c += 1
        total += (len(disc)-r)*c
    return total

def main(filename, repetitions=0):
    """Solution to both part 1 and part 2"""
    with open(filename, encoding="UTF-8") as file:
        disc = []
        for line in file.readlines():
            disc.append(list(line.strip()))
        if repetitions < 1:
            print(f"Part 1: {load(disc)}")
            print("")
        else:
            print("Solving part 2:")
            cycle(disc, reps=repetitions)
            print(f"Part 2: {load(disc)}")

if __name__ == "__main__":
    main("input.txt")
    main("input.txt", repetitions=1000000000)
