"""Advent of Code, 2023, Day 4"""
def main():
    """Solution to both part 1 and part 2"""
    with open('input.txt', encoding="UTF-8") as file:
        points = 0
        total = 0
        extra = []
        for line in file.readlines():
            first, second = line.split('|')
            winning = [int(num) for num in first.split(':')[1].strip().split(' ') if num != '']
            card = [int(num) for num in second.strip().split(' ') if num != '']

            next_extra = []
            cards = 1
            for element in extra:
                cards += 1
                if element>1:
                    next_extra.append(element-1)
            value = 0.5
            count = 0
            for number in card:
                if number in winning:
                    value *= 2
                    count += 1
            if value>=1:
                points += int(value)
            total += 1+cards*count
            if count>0:
                for _ in range(cards):
                    next_extra.append(count)
            extra = next_extra

        print(f"part 1 : {points}")
        print(f"part 2 : {total}")

if __name__ == "__main__":
    main()
