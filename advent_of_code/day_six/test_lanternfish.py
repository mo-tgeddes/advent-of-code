import pytest
from .lanternfish import simulate_lanternfish

fishes = [3,4,3,1,2]
#afterfish = [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]

@pytest.mark.parametrize("days, fishes, expected", [(80, fishes, 5934)])
def test_simulate_lanternfish(days, fishes, expected):
    output = simulate_lanternfish(days, fishes)
    assert output == expected
