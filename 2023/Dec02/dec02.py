"""Advent of Code, 2023, Day 2"""
def main():
    """Solution to both part 1 and part 2"""
    with open('input.txt', encoding="UTF-8") as file:
        bag = { "red" : 12, "blue" : 14, "green" : 13}
        sum_of_possible_games = 0
        sum_of_powers = 0
        for line in file.readlines():
            game, samples = line.split(":")
            nr = int(game[4:])
            numbers = { "red" : 0, "blue" : 0, "green" : 0}
            for sample in samples.split(";"):
                for color in sample.split(","):
                    number, name = color.strip().split(" ")
                    numbers[name] = max(numbers[name], int(number))
            if numbers["red"]   <= bag["red"] and \
            numbers["green"] <= bag["green"] and \
            numbers["blue"]  <= bag["blue"]:
                sum_of_possible_games += nr
            sum_of_powers += numbers["red"]*numbers["green"]*numbers["blue"]
        print(f"part 1 : {sum_of_possible_games:7d}")
        print(f"part 2 : {sum_of_powers:7d}")

if __name__ == "__main__":
    main()
