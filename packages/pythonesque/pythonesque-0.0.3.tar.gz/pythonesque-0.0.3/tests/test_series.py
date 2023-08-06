from pythonesque.series import consecutive_numbers

# https://docs.python.org/3/library/stdtypes.html#ranges
# NOTE two range objects that compare equal might have different start, stop and step attributes
# for that reason, we are comparing lists for equality


def test_consecutive_numbers_count_up_1_param():
    assert consecutive_numbers(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_consecutive_numbers_count_up_2_params():
    assert consecutive_numbers(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_consecutive_numbers_count_down_2_params():
    assert consecutive_numbers(10, 1) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def test_empty():
    assert consecutive_numbers(0) == []
    assert consecutive_numbers(-1) == []
    assert consecutive_numbers(-5) == []


def test_only_1_element():
    assert consecutive_numbers(124, 124) == [124]
