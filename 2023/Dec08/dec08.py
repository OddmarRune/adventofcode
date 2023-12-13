"""Advent of Code, 2023, Day 8"""
import math

def follow(route, mymap, start='AAA', stop=lambda x: x=='ZZZ', k=0):
    """ Follow route function """
    m = len(route)
    pos = start
    i = k
    while i == k or not stop(pos):
        l,r = mymap[pos]
        if route[i%m] == 'L':
            pos = l
        else:
            pos = r
        i += 1
    return i, pos

def main():
    """ Solution to part 1 and part 2 """
    with open("input.txt", encoding="UTF-8") as file:
        route = file.readline().strip()
        mymap = {}
        for line in (tmp.strip() for tmp in file.readlines()):
            if line:
                start, lr = line.split("=")
                l,r = lr.replace("(","").replace(")","").strip().split(",")
                mymap[start.strip()] = (l.strip(), r.strip())
        print(f"Part 1 : Number of steps {follow(route, mymap)[0]}")

        check = lambda y: lambda x: x[2]==y
        lengths = {}
        for pos in mymap.keys():
            if check('A')(pos):
                lengths[pos] = follow(route, mymap, start=pos, stop=check('Z'))
        lcm = 1
        for _,(steps,_) in lengths.items():
            lcm = math.lcm(lcm, steps)
        print(f"Part 2 : Number of steps {lcm}")

        # This was kind of a long shot, and there is really no good reason for this to
        # be correct. Worst case is that they never reach Z at the same time.
        # Checking all routes 10 times to see if period is consistant.

        route_length = len(route)
        ok = 0
        fail = 0
        for pos in mymap:
            if check('A')(pos):
                p = lengths[pos][1]
                n = 0
                for _ in range(10):
                    n1, p1 = follow(route, mymap, start=p, stop=check('Z'), k=n)
                    if n1%route_length == 0 and n1-n == lengths[pos][0] and p1 == p:
                        ok += 1
                    else:
                        print(p, p1, n1-n, lengths[pos][0])
                        fail += 1
                    n = n1
                    p = p1
        print(f"ok = {ok}, fail={fail}")

if __name__ == "__main__":
    main()
