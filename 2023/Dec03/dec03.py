#!/usr/bin/python
sum = 0
allparts = []
with open('input.txt') as file:
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
                            sum += part["number"]
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
                        sum += int(number)
                        symbols.append(pos)
                        for part in prevparts[:]:
                            if part["start"]<=(pos+1) and part["stop"]>=(pos-1):
                                allparts.append(part["number"])
                                sum += part["number"]
                                prevparts.remove(part)
                    elif symbol_found:
                        symbol_found = False
                        allparts.append(int(number))
                        sum += int(number)                        
                    else:
                        symbol_found = False
                        for symbol_pos in prevsymbols:
                            if start<=(symbol_pos+1) and pos-1>=(symbol_pos-1):
                                allparts.append(int(number))
                                sum += int(number)
                                break
                        else:
                            parts.append({"number":int(number), "start":start, "stop":pos-1})
        
        prevparts = parts
        prevsymbols = symbols

newsum = 0
for partnumber in allparts:
    newsum += partnumber

print("part 1 : {}".format(newsum))
                


        
