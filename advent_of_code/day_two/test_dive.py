from dive import product_depth_position, product_aim

COURSE = [["forward", 5], ["down", 5], ["forward", 8], ["up", 3], ["down", 8], ["forward", 2]]

def test_product_aim():
    output = product_aim(COURSE)
    expected = 900
    assert output == expected
def test_product_depth_position():
    output = product_depth_position(COURSE)
    expected = 150
    assert output == expected
