from sonar_sweep import count_increase, multi_increase

REPORT = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_count_increase():
    output = count_increase(REPORT)
    expected = 7
    assert output == expected


def test_multi_increase():
    output = multi_increase(3, REPORT)
    expected = 5
    assert output == expected
