"""Advent of Code, 2023, Day 5"""
def main():
    """Solution to part 2"""
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
                for index in range(1,len(parsed_line),2):
                    seeds.append({"source":int(parsed_line[index]),
                                  "dest":int(parsed_line[index]),
                                  "range":int(parsed_line[index+1])})
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
                maps[current_state]["mappings"].append({"dest":int(parsed_line[0]),
                                                        "source":int(parsed_line[1]),
                                                        "range":int(parsed_line[2])})
        dest_state = "seed"
        reduced_map = seeds

        while dest_state != "location":
            state = dest_state
            current_map = reduced_map
            reduced_map = []
            for map_line in current_map:
                number = map_line
                for the_map_name, the_map in maps.items():
                    if state+"-to" in the_map_name:
                        pos = the_map_name.rfind("-")
                        dest_state = the_map_name[(pos+1):]
                        while number:
                            for rule in the_map["mappings"]:
                                if rule["source"] <= number["dest"] < rule["source"]+rule["range"]:
                                    if number["dest"]+number["range"]<rule["source"]+rule["range"]:
                                        reduced_map.append({
                                            "dest":rule["dest"]-rule["source"]+number["dest"],
                                            "source":number["source"],
                                            "range":number["range"]})
                                        number = {}
                                    else:
                                        range1 = rule["source"]-number["dest"]+rule["range"]
                                        reduced_map.append({
                                            "dest":rule["dest"]-rule["source"]+number["dest"],
                                            "source":number["source"],
                                            "range":range1})
                                        number = {"dest":number["dest"]+range1,
                                                  "source":number["source"]+range1,
                                                  "range":number["range"]-range1}
                                    break
                            else:
                                range1 = number["range"]
                                for rule in the_map["mappings"]:
                                    if number["dest"] < rule["source"] < number["dest"]+number["range"]:
                                        range1 = min(range1, rule["source"]-number["dest"])
                                if range1>0:
                                    reduced_map.append({"dest": number["dest"], 
                                                        "source": number["source"], 
                                                        "range": range1})
                                if range1 < number["range"]:
                                    number = {"dest":number["dest"]+range1,
                                              "source":number["source"]+range1,
                                              "range":number["range"]-range1}
                                else:
                                    number = {}
    min_location = -1
    for map_line in reduced_map:
        if min_location < 0:
            min_location = map_line["dest"]
            min_seed = map_line["source"]
        else:
            if min_location > map_line["dest"]:
                min_location = map_line["dest"]
                min_seed = map_line["source"]
    print(f"closest location = {min_location}, corresponding seed = {min_seed}")

if __name__ == "__main__":
    main()
