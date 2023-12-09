#!/usr/bin/python
bag = { "red" : 12, "blue" : 14, "green" : 13}
sum_of_possible_games = 0
sum_of_powers = 0
with open('input.txt') as file:
    for line in file.readlines():
        game, samples = line.split(":")
        nr = int(game[4:])
        numbers = { "red" : 0, "blue" : 0, "green" : 0}
        for sample in samples.split(";"):
            for color in sample.split(","):
                number, name = color.strip().split(" ")
                numbers[name] = max(numbers[name], int(number))
        if numbers["red"]<=bag["red"] and numbers["green"]<=bag["green"] and numbers["blue"]<=bag["blue"]:
            sum_of_possible_games += nr
        sum_of_powers += numbers["red"]*numbers["green"]*numbers["blue"]
    print("part1 : {}".format(sum_of_possible_games))
    print("part2 : {}".format(sum_of_powers))
