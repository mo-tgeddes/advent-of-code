def calculate_gamma_epsilon(report):
    gamma = []
    epsilon = []
    for index in range(len(report[0])):
        counter = []
        for binary in report:
            counter.append(binary[index])
        most_common_gamma_epsilon(counter, gamma, epsilon)

    return (int(''.join(gamma), 2)), (int(''.join(epsilon), 2))


def calculate_oxygen(report):
    oxygenlist = report.copy()
    for index in range(len(report[0])):
        counter = []
        for binary in oxygenlist:
            counter.append(binary[index])
        if most_common_number(counter) == 0:
            oxygenlist = [binary for binary in oxygenlist if binary[index] != '1']
        else:
            oxygenlist = [binary for binary in oxygenlist if binary[index] != '0']
        if len(oxygenlist) == 1:
            return int(''.join(oxygenlist[0]), 2)


def calculate_co2(report):
    co2list = report.copy()
    for index in range(len(report[0])):
        counter = []
        for binary in co2list:
            counter.append(binary[index])
        if least_common_number(counter) == 0:
            co2list = [binary for binary in co2list if binary[index] != '1']
        else:
            co2list = [binary for binary in co2list if binary[index] != '0']
        if len(co2list) == 1:
            return int(''.join(co2list[0]), 2)


def most_common_number(binarylist):
    least = 0
    if binarylist.count('1') >= binarylist.count('0'):
        least = 1
    return least


def least_common_number(binarylist):
    least = 1
    if binarylist.count('0') <= binarylist.count('1'):
        least = 0
    return least


def most_common_gamma_epsilon(binarylist, gamma, epsilon):
    if binarylist.count("0") > len(binarylist) / 2:
        # get updated automatically without having to return anything
        gamma.append("0")
        epsilon.append("1")
    else:
        gamma.append("1")
        epsilon.append("0")


def read_file(filepath):
    with open(filepath) as file_handle:
        contents = file_handle.readlines()
        # list comprehension - reads everything in square brackets before
        # complaining
    return [(line.strip()) for line in contents]


if __name__ == "__main__":
    course1 = read_file("input.txt")
    # gamma, epsilon = calculate_gamma_epsilon(course1)
    # print(gamma * epsilon)
    print(calculate_co2(course1) * calculate_oxygen(course1))
