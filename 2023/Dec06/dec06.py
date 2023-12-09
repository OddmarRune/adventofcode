"""Advent of Code, 2023, Day 6"""
def main():
    """Solution to both part 1 and part 2"""
    with open('input.txt', encoding="UTF-8") as file:
        table1 = {}
        table2 = {}
        for line in file.readlines():
            name, data = line.split(":")
            table1[name] = [int(number) for number in data.strip().split(" ") if number.strip()!='']
            table2[name] = int(data.replace(" ", ""))
        product1 = 1
        for i in range(len(table1[name])):
            product1 *= 2*int((table1["Time"][i]**2/4-table1["Distance"][i])**.5)+\
                (table1["Time"][i]-1)%2
        product2 = 2*int((table2["Time"]**2/4-table2["Distance"])**.5)+(table2["Time"]-1)%2
        print(f"alternatives part 1 : {product1}")
        print(f"alternatives part 2 : {product2}")

if __name__ == "__main__":
    main()
