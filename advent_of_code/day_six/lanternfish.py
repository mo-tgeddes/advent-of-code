
def simulate_lanternfish(days, fishes):
    """

    Return the number of fish after a certain number of days.

    Parameters
    ----------
    days : integer.
    fishes : list of integers.

    Returns
    -------
    integer
        fishnumber

    """
    fishnumber = len(fishes)
    for day in range(days):
        newfish = 8
        for index in range(fishnumber):
            fishes[index] -= 1
            if fishes[index] < 0:
                fishes[index] = 6
                fishes.append(newfish)
                fishnumber +=1
    return fishnumber

def fish_states(days, fishlist):
    fishstates = [0,0,0,0,0,0,0,0,0]
    for fish in fishlist:
        fishstates[fish] = fishstates[fish] + 1
    for day in range(days):
        morefish = fishstates[0]
        fishstates.pop(0)
        fishstates.append(morefish)
        fishstates[6] = fishstates[6] + morefish
    return sum(fishstates)

def fast_fish(days, fishes):
    if days > 0:
        counter = fishes.count(0)
        newfish = [6 if x==0 else x-1 for x in fishes]
        for index in range(counter):
            newfish.append(8)
        fishes = fast_fish((days-1), newfish)
    return fishes

def read_file(filepath):
    with open(filepath) as file_handle:
        contents = file_handle.readlines()
        # list comprehension - reads everything in square brackets before
        # complaining
    values = [int(value) for value in contents[0].split(",")]
    return values


if __name__ == "__main__":
    #fishlist = [1,2,4,5,5,5,2,1,3,1,4,3,2,1,5,5,1,2,3,4,4,1,2,3,2,1,4,4,1,5,5,1,3,4,4,4,1,2,2,5,1,5,5,3,2,3,1,1,3,5,1,1,2,4,2,3,1,1,2,1,3,1,2,1,1,2,1,2,2,1,1,1,1,5,4,5,2,1,3,2,4,1,1,3,4,1,4,1,5,1,4,1,5,3,2,3,2,2,4,4,3,3,4,3,4,4,3,4,5,1,2,5,2,1,5,5,1,3,4,2,2,4,2,2,1,3,2,5,5,1,3,3,4,3,5,3,5,5,4,5,1,1,4,1,4,5,1,1,1,4,1,1,4,2,1,4,1,3,4,4,3,1,2,2,4,3,3,2,2,2,3,5,5,2,3,1,5,1,1,1,1,3,1,4,1,4,1,2,5,3,2,4,4,1,3,1,1,1,3,4,4,1,1,2,1,4,3,4,2,2,3,2,4,3,1,5,1,3,1,4,5,5,3,5,1,3,5,5,4,2,3,2,4,1,3,2,2,2,1,3,4,2,5,2,5,3,5,5,1,1,1,2,2,3,1,4,4,4,5,4,5,5,1,4,5,5,4,1,1,5,3,3,1,4,1,3,1,1,4,1,5,2,3,2,3,1,2,2,2,1,1,5,1,4,5,2,4,2,2,3]
    fishlist = read_file("input.txt")
    #fishlist = [3,4,3,1,2]
    print(len(fast_fish(80, fishlist)))