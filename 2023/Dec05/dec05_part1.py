"""Advent of Code, 2023, Day 5"""
def main():
    """Solution to part 1"""
    with open('input.txt', encoding="UTF-8") as file:
        current_state = ""
        maps = {}
        states = []
        seeds = []    
        for line in file.readlines():
            parsed_line = line.strip().split(" ")
            if len(parsed_line)==0 or parsed_line[0]=='':
                current_state = ""
                continue

            if parsed_line[0] == "seeds:":
                for seed in parsed_line[1:]:
                    seeds.append(int(seed))
                continue            

            if len(parsed_line) == 2 and parsed_line[1] == "map:":
                current_state = parsed_line[0]
                the_map = current_state.split("-")
                maps[current_state] = {"from":the_map[0], "to":the_map[2], "mappings": []}
                if not the_map[0] in states:
                    states.append(the_map[0])
                if not the_map[2] in states:
                    states.append(the_map[2])
                continue

            if current_state != "":
                maps[current_state]["mappings"].append({
                    "dest":int(parsed_line[0]),
                    "source":int(parsed_line[1]),
                    "range":int(parsed_line[2])})

        locations = []
        minimum = -1
        source = -1
        for seed in seeds:
            number = seed
            state = "seed"
            while state != "location":
                for the_map_name, the_map in maps.items():
                    if state+"-to" in the_map_name:
                        for rule in the_map["mappings"]:
                            if rule["source"] <= number < rule["source"]+rule["range"]:
                                number = number-rule["source"]+rule["dest"]
                                state = the_map["to"]
                                break
                        else:
                            state = the_map["to"]
                        break
                else:
                    print("Error")
            locations.append({"from":seed, "to":number})
            if source < 0 or number < minimum:
                minimum = number
                source = seed

        print(f"closest location = {minimum}, corresponding seed = {source}")

if __name__ == "__main__":
    main()
