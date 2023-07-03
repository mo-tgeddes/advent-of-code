def product_depth_position(course):
    depth = 0
    position = 0
    # enumerate = index is the number in the list and item is the actual value
    for index, item in enumerate(course):
        if item[0] == "forward":
            position = position + item[1]
        elif item[0] == "down":
            depth += item[1]
        elif item[0] == "up":
            depth -= item[1]
    return depth * position


def product_aim(course):
    depth = 0
    position = 0
    aim = 0
    # enumerate = index is the number in the list and item is the actual value
    for index, item in enumerate(course):
        if item[0] == "forward":
            position = position + item[1]
            depth += aim * item[1]
        elif item[0] == "down":
            aim += item[1]
        elif item[0] == "up":
            aim -= item[1]
    return depth * position


def read_file(filepath):
    with open(filepath) as file_handle:
        contents = file_handle.readlines()
    commands = []
    for line in contents:
        instruction, value = line.split()
        commands.append([instruction, int(value)])
    return commands


if __name__ == "__main__":
    course1 = read_file("input.txt")
    print(product_aim(course1))
