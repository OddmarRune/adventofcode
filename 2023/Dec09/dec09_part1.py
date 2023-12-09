"""Advent of Code, 2023, Day 7"""

def diff(numbers):
    """ First difference """
    d = [None]*(len(numbers)-1)
    for i in range(len(numbers)-1):
        d[i] = numbers[i+1]-numbers[i]
    return d

def main():
    """ Solution to part 1 """
    with open("input.txt", encoding="UTF-8") as file:
        sum_of_next_numbers = 0
        for line in (tmp.strip() for tmp in file.readlines()):
            numbers = [[int(item) for item in line.split() if item.strip() != '']]
            while not all(number==0 for number in numbers[-1]):
                numbers.append(diff(numbers[-1]))
            k = len(numbers)
            numbers[k-1].append(0)
            for i in range(k-1):
                numbers[k-2-i].append(numbers[k-2-i][-1]+numbers[k-1-i][-1])
            sum_of_next_numbers += numbers[0][-1]
        print(f" Part 1 : The sum of extrapolated values are {sum_of_next_numbers}")

if __name__ == "__main__":
    main()
