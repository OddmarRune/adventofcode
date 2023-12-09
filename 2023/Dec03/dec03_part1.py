"""Advent of Code, 2023, Day 2"""
def main():
    """Solution to part 1"""
    with open('input.txt', encoding="UTF-8") as file:
        allparts = []
        prevparts = []
        prevsymbols = []
        for line in file.readlines():
            parts = []
            symbols = []
            state = 0
            number = ""
            start = 0
            symbol_found = False
            for pos, letter in enumerate(line):
                if state == 0:
                    if letter in '0123456789':
                        state = 1
                        number = letter
                        start = pos
                    elif letter != '.' and letter !='\n':
                        symbol_found = True
                        symbols.append(pos)
                        for part in prevparts[:]:
                            if part["start"]<=(pos+1) and part["stop"]>=(pos-1):
                                allparts.append(part["number"])
                                prevparts.remove(part)
                    else:
                        symbol_found = False
                elif state == 1:
                    if letter in '0123456789':
                        number += letter
                    else:
                        state = 0
                        if letter != '.' and letter !='\n':
                            symbol_found = True
                            allparts.append(int(number))
                            symbols.append(pos)
                            for part in prevparts[:]:
                                if part["start"]<=(pos+1) and part["stop"]>=(pos-1):
                                    allparts.append(part["number"])
                                    prevparts.remove(part)
                        elif symbol_found:
                            symbol_found = False
                            allparts.append(int(number))   
                        else:
                            symbol_found = False
                            for symbol_pos in prevsymbols:
                                if start<=(symbol_pos+1) and pos-1>=(symbol_pos-1):
                                    allparts.append(int(number))
                                    break
                            else:
                                parts.append({"number":int(number), "start":start, "stop":pos-1})

            prevparts = parts
            prevsymbols = symbols

        sum_of_part_numbers = 0
        for part_number in allparts:
            sum_of_part_numbers += part_number

        print(f"part 1 : {sum_of_part_numbers}")

if __name__ == "__main__":
    main()
