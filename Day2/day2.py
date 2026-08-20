import code
from locale import atoi


def open_file():
    with open("Day3\\input\\input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        return lines

def part1():
    battArrays = open_file()
    total_joltage = 0
    # Naive approach, check for the higest digit from the left, then check for the highest digit from the right, without crossing the left index.
    for array in battArrays:
        max_tens = 0
        max_ones = 0
        left_index = 0
        for i in range(0, len(array)-1):
            if (atoi(array[i]) > max_tens):
                max_tens = atoi(array[i])
                left_index = i

        for i in range(left_index + 1, len(array)):
            if (atoi(array[i]) > max_ones):
                max_ones = atoi(array[i])
        total_joltage += max_tens*10 + max_ones

    print(f"Part 1: {total_joltage}")



def part2():
    battArrays = open_file()
    total_joltage = 0
    # Naive approach, check for the higest digit from the left, then move the checking window down.
    num_batteries = 12
    batteries = []
    current_max = 0
    for array in battArrays:
        left_index = 0
        bat = []
        for current_battery in range(1, num_batteries+1):
            current_max = 0
            for i in range(left_index, len(array)-(num_batteries - current_battery)):
                if (atoi(array[i]) > current_max):
                    current_max = atoi(array[i])
                    left_index = i
            bat.append(array[left_index])
            left_index += 1
        batteries.append(atoi("".join(bat)))

    print(f"Part 2: {sum(batteries)}")

if __name__ == "__main__":
    part1()
    part2()