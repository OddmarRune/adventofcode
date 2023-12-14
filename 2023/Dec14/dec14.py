"""Advent of Code, 2023, Day 14"""

def north(disc):
    for i in range(len(disc[0])):
        o_count = 0
        o_start = 0
        for l in range(len(disc)):
            if disc[l][i] == 'O':
                o_count += 1
            elif disc[l][i] == '#':
                for c in range(o_start, o_start+o_count):
                    disc[c][i] = 'O'
                for c in range(o_start+o_count, l):
                    disc[c][i] = '.'
                o_count = 0
                o_start = l+1
        if o_count > 0:
            for c in range(o_start, o_start+o_count):
                disc[c][i] = 'O'
            for c in range(o_start+o_count, len(disc)):
                disc[c][i] = '.'

def west(disc):
    for i in range(len(disc)):
        o_count = 0
        o_start = 0
        for l in range(len(disc[0])):
            if disc[i][l] == 'O':
                o_count += 1
            elif disc[i][l] == '#':
                for c in range(o_start, o_start+o_count):
                    disc[i][c] = 'O'
                for c in range(o_start+o_count, l):
                    disc[i][c] = '.'
                o_count = 0
                o_start = l+1
        if o_count > 0:
            for c in range(o_start, o_start+o_count):
                disc[i][c] = 'O'
            for c in range(o_start+o_count, len(disc[0])):
                disc[i][c] = '.'

def south(disc):
    for i in range(len(disc[0])):
        o_count = 0
        o_start = len(disc)-1
        for l in range(len(disc)-1,-1,-1):
            if disc[l][i] == 'O':
                o_count += 1
            elif disc[l][i] == '#':
                for c in range(o_start, o_start-o_count,-1):
                    disc[c][i] = 'O'
                for c in range(o_start-o_count, l, -1):
                    disc[c][i] = '.'
                o_count = 0
                o_start = l-1
        if o_count > 0:
            for c in range(o_start, o_start-o_count, -1):
                disc[c][i] = 'O'
            for c in range(o_start-o_count, -1, -1):
                disc[c][i] = '.'

def east(disc):
    for i in range(len(disc)):
        o_count = 0
        o_start = len(disc[0])-1
        for l in range(len(disc[0])-1,-1,-1):
            if disc[i][l] == 'O':
                o_count += 1
            elif disc[i][l] == '#':
                for c in range(o_start, o_start-o_count, -1):
                    disc[i][c] = 'O'
                for c in range(o_start-o_count, l, -1):
                    disc[i][c] = '.'
                o_count = 0
                o_start = l-1
        if o_count > 0:
            for c in range(o_start, o_start-o_count, -1):
                disc[i][c] = 'O'
            for c in range(o_start-o_count, -1, -1):
                disc[i][c] = '.'

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
    for i in range(len(disc)):
        c = 0
        for l in range(len(disc[i])):            
            if disc[i][l] == 'O':
                c += 1
        #print(len(disc)-i, c)
        total += (len(disc)-i)*c
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
