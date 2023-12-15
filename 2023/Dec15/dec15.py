"""Advent of Code, 2023, Day 15"""

def part1(filename):
    """Solution to part 1"""
    with open(filename, encoding="ascii") as file:
        data = file.read() # .strip()+','
        total = 0
        current = 0
        for c in data:
            if c in ",\n":
                total += current
                current = 0
            else:
                current = ((ord(c)+current)*17)%256
        print(f"Part 1 : {total}")

def part2(filename):
    """Solution to part 2"""
    with open(filename, encoding="ascii") as file:
        data = file.read()
        current = 0
        boxes = []
        box_nr = -1
        label = ""
        read_lense = False        
        for _ in range(256):
            boxes.append({})
        for c in data:
            if read_lense:
                focal_length = int(c)
                boxes[box_nr][label] = focal_length
                read_lense = False
            elif c in ",\n":
                current = 0
                label = ""
            elif c == '-':
                box_nr = current
                if label in boxes[box_nr]:
                    boxes[box_nr].pop(label)
            elif c == '=':
                box_nr = current
                read_lense = True
            else:
                label += c
                current = ((ord(c)+current)*17)%256
        total = 0
        for box_nr, box in enumerate(boxes):
            if box:
                number = 0
                for slot, name in enumerate(box):
                    number += (box_nr+1) * (slot+1) * box[name]
                total += number
        print(f"Part 2 : {total}")

if __name__ == "__main__":
    part1("input.txt")
    part2("input.txt")
