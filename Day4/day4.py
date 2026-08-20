
def open_file():
    with open("Day4\\input\\input.txt") as f:
        lines = f.readlines()

    factory_map = []
    for each in lines:
        factory_map.append(list(each.strip()))

    return factory_map

def check_surroundings(factory_map, source_y, source_x):
    x_list = [source_x]
    y_list = [source_y]
    result = 0
    if source_x - 1 >= 0:
        x_list.append(source_x-1)
    if source_x + 1 < len(factory_map[source_y]):
        x_list.append(source_x+1)
    if source_y - 1 >= 0:
        y_list.append(source_y-1)
    if source_y + 1 < len(factory_map):
        y_list.append(source_y+1)


    for x in x_list:
        for y in y_list:
            if (y == source_y and x == source_x):
                continue
            if factory_map[y][x] == "@":

                result += 1

    return result


def part1(factory_map):
    total = 0
    for y in range(len(factory_map)):
        for x in range(len(factory_map[y])):
            if(factory_map[y][x] == "@"):
                if (check_surroundings(factory_map,y,x) < 4):
                    print(f"Eligible Box Found at: ({y},{x})")
                    total +=1
    print(total)


def part2(factory_map):
    total = 0
    old_total = -1
    remove = []
    while(True):
        for y in range(len(factory_map)):
            for x in range(len(factory_map[y])):
                if(factory_map[y][x] == "@"):
                    if (check_surroundings(factory_map,y,x) < 4):
                        remove.append([y,x])
                        total +=1
        for each in remove:
            factory_map[each[0]][each[1]] = "."
        remove.clear()
        if (old_total != total):
            old_total = total
        else:
            break
    print(total)

if __name__ == "__main__":
    factory_map = open_file();
    part1(factory_map)
    part2(factory_map)