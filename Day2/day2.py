import code
from locale import atoi


def open_file():
    with open("Day2\\input\\input.txt") as f:
        line = f.readlines()
        line[0] = line[0].strip()
        line = [line[0].split(",")]
        i = []
        for ids in line[0]:
            i.append(ids.split("-"))
        
    return i


def part1():
    ids = open_file()
    total = 0
    for id in ids:
        for i in range(atoi(id[0]), atoi(id[1])+1):
            string = str(i)
            length = len(string)
            mid = length // 2
            # odd lengths can't have repeated pairs
            if (length % 2 != 0):
                continue
            # check the mirrored parts and compare. If they are the same, add to total
            if (string[0:(mid)] == string[(mid):length]):
                total += i

    print(f"Part 1: {total}")


def part2():
    ids = open_file()
    total = 0
    for id in ids:
        for i in range(atoi(id[0]), atoi(id[1])+1):
            string = str(i)
            length = len(string)
            # use recursion to check for repeated sequences of any length

    print(f"Part 2: {total}")

if __name__ == "__main__":
    part1()
    part2()