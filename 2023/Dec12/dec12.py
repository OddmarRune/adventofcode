"""Advent of Code, 2023, Day 12"""

def get_samples(template, vector):
    """Recursive function for generating all possibilities using yield"""
    tail = vector[-1]
    head = vector[:-1]
    start = sum(head)+len(head)
    stop = len(template)-tail
    for i in range(start, stop+1):
        if (i>0 and template[i-1] == '#') or \
                '.' in template[i:i+tail] or \
                '#' in template[i+tail:]:
            continue
        if len(head)>0:
            for prev in get_samples(template[:(i-1)],head):
                yield prev+[i]
        else:
            if not '#' in template[:i]:
                yield [i]
            else:
                return

def keyify(template, vector):
    """Key generator"""
    return template+f"{vector}"

def get_count(template, vector):
    """Recursive function for counting possibilities, with hashed cache"""
    if keyify(template, vector) in get_count.cache:
        return get_count.cache[keyify(template, vector)]
    tail = vector[-1]
    head = vector[:-1]
    start = sum(head)+len(head)
    stop = len(template)-tail
    counter = 0
    for i in range(start, stop+1):
        if (i>0 and template[i-1] == '#') or \
                '.' in template[i:i+tail] or \
                '#' in template[i+tail:]:
            continue
        if len(head)>0:
            counter += get_count(template[:(i-1)],head)
        elif not '#' in template[:i]:
            counter += 1
    get_count.cache[keyify(template, vector)] = counter
    return counter
get_count.cache = {}

def main(filename, factor=1, title=""):
    """Solutions to part 1 and part 2"""
    with open(filename, encoding="UTF-8") as file:
        sum_of_possibilities = 0
        for line in file.readlines():
            template, counts = line.strip().split(' ')
            vector = [int(v) for v in counts.split(',')]
            if factor>1:
                vector0 = vector[:]
                template0 = template
                for _ in range(factor-1):
                    template +="?"+template0
                    vector += vector0
            if factor == 1:
                sum_of_possibilities += sum(1 for _ in get_samples(template, vector))
            else:
                sum_of_possibilities += get_count(template, vector)
        print(f"{title}number of possibilities = {sum_of_possibilities}")

if __name__ == "__main__":
    main("input.txt", factor=1, title="Part 1 : ")
    main("input.txt", factor=5, title="Part 2 : ")
    
