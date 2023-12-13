"""Advent of Code, 2023, Day 13"""

def check_vert(block, c = 0):
    """Check if block is symmetric with horizontal mirror"""
    if (len(block[0])-c)%2 == 1 or len(block[0])-1<=abs(c):
        return 100
    number = 0
    for line in block:
        if c >= 0:
            number += sum([0 if line[i+c] == line[-1-i] else 1 for i in range((len(line)-c))])
        else:
            number += sum([0 if line[i] == line[-1-i+c] else 1 for i in range(len(line)+c)])
    return number//2

def check_horz(block, r = 0):
    """Check if block is symmetric with horizontal mirror"""
    if (len(block)-r)%2 == 1 or len(block)-1 <= abs(r):
        return 100
    if r >= 0:
        return sum([sum([0 if block[i+r][l] == block[-1-i][l] else 1 \
                    for l in range(len(block[0]))]) for i in range(len(block)-r)])//2
    else:
        return sum([sum([0 if block[i][l] == block[-1-i+r][l] else 1 for \
                    l in range(len(block[0]))]) for i in range(len(block)+r)])//2

def process_block(block, smudge_count):
    """Block processor"""
    for r in range(len(block)):
        if check_horz(block, r) == smudge_count:
            break
        elif check_horz(block, -r) == smudge_count:
            r = -r
            break
    else:
        r = -100

    for c in range(len(block[0])):
        if check_vert(block, c) == smudge_count:
            break
        elif check_vert(block, -c) == smudge_count:
            c = -c
            break
    else:
        c = -100
    value = 0
    if r>-100:
        if r >= 0:
            value = 100*(len(block)-(len(block)-r)//2)
        if r < 0:
            value = 100*((len(block)+r)//2)
    if c>-100:
        if c >= 0:
            value = len(block[0])-(len(block[0])-c)//2
        if c < 0:
            value = (len(block[0])+c)//2
    return value


def main(filename, smudge_count=0, title=""):
    """Solution to part 1 and part 2"""
    with open(filename, encoding="UTF-8") as file:
        block = []
        my_sum  = 0
        for line in file.readlines():
            if len(line.strip())>0:
                block.append(line.strip())
            else:
                my_sum += process_block(block, smudge_count)
                block = []
        if block:
            # Process the last block if present
            my_sum += process_block(block, smudge_count)
            block = []
        print(f"{title}sum of lines = {my_sum}")

if __name__ == "__main__":
    main("input.txt", title="Part 1 : ")
    main("input.txt", title="Part 2 : ", smudge_count = 1)
