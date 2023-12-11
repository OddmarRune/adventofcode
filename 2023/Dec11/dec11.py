"""Advent of Code, 2023, Day 11"""

def main(filename, inflation=1):
    """Solution to both part 1 and part 2"""
    with open(filename, encoding="UTF-8") as file:
        galaxy_chart = []
        row = 0
        galaxy_columns = []
        for line in file.readlines():
            col = line.find('#')
            while col >-1 :
                galaxy_chart.append((row, col))
                if not col in galaxy_columns:
                    galaxy_columns.append(col)
                col = line.find('#', col+1)
            if not '#' in line:
                row += inflation
            row += 1
        galaxy_columns = sorted(galaxy_columns)
        empty_columns = [c for c in range(max(galaxy_columns)) if not c in galaxy_columns]
        galaxy_chart = [(row, col+inflation*sum(col > cols for cols in empty_columns)) \
                        for (row, col) in galaxy_chart]
        sum_of_distances = 0
        for i, galaxy1 in enumerate(galaxy_chart):
            for j, galaxy2 in enumerate(galaxy_chart):
                if i>=j:
                    continue
                row1, col1 = galaxy1
                row2, col2 = galaxy2
                sum_of_distances += abs(row2-row1)+abs(col2-col1)
        print(f"sum of all shortest distances : {sum_of_distances}")

if __name__ == "__main__":
    main("input.txt")
    main("input.txt", inflation=999999)
