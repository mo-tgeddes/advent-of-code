from .binary_diagnostic import calculate_gamma_epsilon, calculate_oxygen, calculate_co2

REPORT = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

def test_calculate_oxygen():
    output = calculate_oxygen(REPORT)
    expected = 23
    assert output == expected


def test_calculate_co2():
    output = calculate_co2(REPORT)
    expected = 10
    assert output == expected


def test_calculate_gamma_epsilon():
    output = calculate_gamma_epsilon(REPORT)
    expected = 22, 9
    assert output == expected