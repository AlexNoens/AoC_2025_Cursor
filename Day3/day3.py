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

def check_mirrored(string):
    length = len(string)
    mid = length // 2
    # odd lengths can't have repeated pairs
    if (length % 2 != 0):
        return False
    # check the mirrored parts and compare. If they are the same, add to total
    if (string[0:(mid)] == string[(mid):length]):
        print(f"Mirrored match: {string}")
        return True

def check_all(string):
    length = len(string)
    mid = length // 2
    # Even lengths have been checked by "mirrored", only check odd lengths here
    if (length % 2 != 0):
        for i in range(0, length):
            if (string[i] != string[0]):
                return False
        return True
    else:
        return False

# Half (mirrored) and all (odd length) have been checked, now check for repeated sequences of any length
def check_patterns(string):
    length = len(string)
    patternFound = True
    for i in range(2, length//2):
        patternFound = True
        if (length%i == 0):
            pattern = string[0:i]
            for j in range(0, length//i):
                if (string[j*i:j*i+i] != pattern):
                    patternFound = False
                    break
            if (patternFound):
                print(f"Pattern match: {string} with pattern: {pattern}")
                return patternFound
    return False

def part2():
    ids = open_file()
    total = 0
    for id in ids:
        for i in range(atoi(id[0]), atoi(id[1])+1):
            string = str(i)
            if (len(string) == 1):
                continue
            # Mirrored, and Even all matched
            if (check_mirrored(string)):
                total += i
            # Odd length all matched
            elif (check_all(string)):
                total += i
            # use recursion to check for repeated sequences of any length
            elif (check_patterns(string)):
                total += i
    print(f"Part 2: {total}")

if __name__ == "__main__":
    part1()
    part2()