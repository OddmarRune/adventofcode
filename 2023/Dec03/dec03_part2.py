"""Advent of Code, 2023, Day 2"""
def main():
    """Solution to part 2"""
    with open('input.txt', encoding="UTF-8") as file:
        prevline = ""
        line = ""
        line_nr = -1
        symbols = []
        for nextline in file.readlines():
            line_nr += 1
            for pos, letter in enumerate(line):
                if letter == "*":
                    symbol = {"line":line_nr, "pos":pos, "numbers":[]}
                    if len(prevline)>0:
                        up = prevline[pos] in '0123456789'
                        for start in range(pos,0,-1):
                            if not prevline[start-1] in '0123456789':
                                break
                        else:
                            start = 0
                        for stop in range(pos,len(prevline)):
                            if not prevline[stop+1] in '0123456789':
                                break
                        if up:
                            symbol["numbers"].append(int(prevline[start:stop+1]))
                        else:
                            if start<pos:
                                symbol["numbers"].append(int(prevline[start:pos]))
                            if stop>pos:
                                symbol["numbers"].append(int(prevline[pos+1:stop+1]))
                    for start in range(pos,0,-1):
                        if not line[start-1] in '0123456789':
                            break
                    else:
                        start = 0
                    if start<pos:
                        symbol["numbers"].append(int(line[start:pos]))
                    for stop in range(pos,len(line)-1):
                        if not line[stop+1] in '0123456789':
                            break
                    if stop>pos:
                        symbol["numbers"].append(int(line[pos+1:stop+1]))
                    if len(nextline)>0:      
                        down = nextline[pos] in '0123456789'
                        for start in range(pos,0,-1):
                            if not nextline[start-1] in '0123456789':
                                break
                        else:
                            start = 0
                        for stop in range(pos,len(nextline)):
                            if not nextline[stop+1] in '0123456789':
                                break
                        if down:
                            symbol["numbers"].append(int(nextline[start:stop+1]))
                        else:
                            if start<pos:
                                symbol["numbers"].append(int(nextline[start:pos]))
                            if stop>pos:
                                symbol["numbers"].append(int(nextline[pos+1:stop+1]))
                    symbols.append(symbol)
            prevline = line
            line = nextline

        sum_of_gear_ratios = 0
        for symbol in symbols:
            if len(symbol["numbers"]) == 2:
                sum_of_gear_ratios += symbol["numbers"][0]*symbol["numbers"][1]
        print(f"part 2 : {sum_of_gear_ratios}")

if __name__ == "__main__":
    main()
