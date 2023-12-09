#!/usr/bin/python
with open('input.txt') as file:
    prevline = ""
    line = ""
    line_nr = -1
    symbols = []    
    for nextline in file.readlines():        
        line_nr += 1
        for pos, letter in enumerate(line):
            if letter == "*":                
                symbol = {"line":line_nr, "pos":pos, "numbers": []}
                if len(prevline)>0:      
                    up = prevline[pos] in '0123456789'
                    for pos1 in range(pos,0,-1):
                        if not prevline[pos1-1] in '0123456789':
                            break
                    else:
                        pos1 = 0
                    for pos2 in range(pos,len(prevline)):
                        if not prevline[pos2+1] in '0123456789':
                            break
                    if up:
                        symbol["numbers"].append(int(prevline[pos1:pos2+1]))
                    else:
                        if pos1<pos:
                            symbol["numbers"].append(int(prevline[pos1:pos]))
                        if pos2>pos:
                            symbol["numbers"].append(int(prevline[pos+1:pos2+1]))
                for pos3 in range(pos,0,-1):
                    if not line[pos3-1] in '0123456789':
                        break
                else:
                    pos3 = 0
                if pos3<pos:
                    symbol["numbers"].append(int(line[pos3:pos]))
                for pos4 in range(pos,len(line)-1):
                    if not line[pos4+1] in '0123456789':
                        break
                if pos4>pos:
                    symbol["numbers"].append(int(line[pos+1:pos4+1]))
                if len(nextline)>0:      
                    down = nextline[pos] in '0123456789'
                    for pos5 in range(pos,0,-1):
                        if not nextline[pos5-1] in '0123456789':
                            break
                    else:
                        pos5 = 0
                    for pos6 in range(pos,len(nextline)):
                        if not nextline[pos6+1] in '0123456789':
                            break
                    if down:
                        symbol["numbers"].append(int(nextline[pos5:pos6+1]))
                    else:
                        if pos5<pos:
                            symbol["numbers"].append(int(nextline[pos5:pos]))
                        if pos6>pos:                            
                            symbol["numbers"].append(int(nextline[pos+1:pos6+1]))
                symbols.append(symbol)
        prevline = line
        line = nextline

sum = 0
for symbol in symbols:    
    if len(symbol["numbers"]) == 2:        
        sum += symbol["numbers"][0]*symbol["numbers"][1]
print("part 2 : {}".format(sum))
                    
