def count_increase(report):
    """
    Return the number of times a depth measurement increases from the previous
    measurement from the report.

    Parameters
    ----------
    report : list
        List of depths.

    Return
    ------
    int
       The number of times a depth measurement increases from the previous
       measurement from the report.

    Example
    -------
    >>> report = [1, 2, 3, 2]
    >>> count_increase(report)
    2
    """

    count = 0
    prev = report[0]
    for depth in report[1:]:
        if depth > prev:
            count += 1
        prev = depth

    return count


def multi_increase(num, report):
    """
    Return the number of times an increment of depth measurements increases from the previous
    measurements from the report.
    
    Parameters
    ----------
    num : int
        Number that the depths are grouped together by.
    report : list
        List of depths.
    

    Return
    ------
    int
       The number of times an increment of depth measurements increases from the previous
       measurements from the report.

    Example
    -------
    >>> report = [1, 2, 3, 2]
    >>> num = 2
    >>> multi_increase(num,report)
    1
    """
    count = 0
    # prev = report[0]+report[1]+report[2]
    prev = sum(report[0:3])
    next = 0
    for index in range(1, (len(report))):
        next = sum(report[index:index + 3])
        if next > prev:
            count += 1
        prev = next

    return count


def read_file(filepath):
    with open(filepath) as file_handle:
        contents = file_handle.readlines()
        # list comprehension - reads everything in square brackets before
        # complaining
    return [int(line.strip()) for line in contents]


if __name__ == "__main__":
    report = read_file("input.txt")
    #print(count_increase(report))
    print(multi_increase(3, report))
