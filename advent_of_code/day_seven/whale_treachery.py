import numpy as np
def calculate_cheapest_alignment_brute_force(positions):
    smallest = min(positions)
    largest = max(positions)
    positionvalue = None
    minsum = 9999
    for value in range(smallest, largest+1):
        diff=np.subtract(positions,value)
        print(diff)
        positionsum = np.sum(np.abs(diff))
        if positionsum < minsum:
            minsum = positionsum
            positionvalue = value
    return positionvalue


def calculate_fuel_cost(positions, day):
    alignments = [np.ceil(np.mean(positions)), np.floor(np.mean(positions))]
    costs = [int(np.sum(calculate_positions(np.subtract(positions, alignment)))) for alignment in alignments]
    return min(costs)

def calculate_feul_day1(positions):
    alignment = np.median(positions)
    costs = np.subtract(positions, alignment)
    return int(np.sum(np.abs(costs)))

def calculate_positions(costs):
    return (np.abs(costs)**2 + np.abs(costs))//2

def read_file(filepath):
    with open(filepath) as file_handle:
        contents = file_handle.readlines()
        # list comprehension - reads everything in square brackets before
        # complaining
    values = [int(value) for value in contents[0].split(",")]
    return values


if __name__ == "__main__":
    positions = read_file("input.txt")
    #print(calculate_cheapest_alignment(positions))
    print(calculate_fuel_cost(positions, 2))
