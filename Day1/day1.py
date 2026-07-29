import code
from locale import atoi


print("hello")

def open_file():
    with open("Day1\\input\\input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        instructions = []
        for line in lines:
            if line[0] == "R":
                instructions.append(atoi(line[1:]))
            elif line[0] == "L":
                instructions.append(-atoi(line[1:]))
        return instructions


def part1():
    instructions = open_file()
    pos = 50
    code = 0
    for instruction in instructions:
        instruction = instruction % 100
        pos += instruction
        if pos < 0:
            pos = 100 + pos
        elif pos > 99:
            pos = pos - 100


        if pos == 0:
            code += 1

    print(f"Part 1: {code}")

def part2():
    instructions = open_file()
    pos = 50
    code = 0

    # Loop must count both the number of times the instruction counter crosses zero and the number of times the instruction lands on zero.
    for instruction in instructions:

        # Account for the wrap arounds
        if abs(instruction) >= 100:
            hundreds = abs(instruction) // 100
            code += hundreds
            if instruction < 0:            
                instruction = instruction + (hundreds * 100)
            else:
                instruction = instruction - (hundreds * 100)

        # Check if we are at zero, if so, don't double count transitions
        if pos == 0:
            pos += instruction
            if pos < 0:
                pos = 100 + pos
            elif pos > 100:
                pos = pos - 100
            elif pos == 0 or pos == 100:
                code += 1
                pos = 0
        else:
            pos += instruction
            if pos < 0:
                code += 1
                pos = 100 + pos
            elif pos > 100:
                code += 1
                pos = pos - 100
            elif pos == 0 or pos == 100:
                code += 1
                pos = 0

    print(f"Part 2: {code}")

if __name__ == "__main__":
    part1()
    part2()