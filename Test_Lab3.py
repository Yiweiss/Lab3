import Lab3

print("Test_Lab3")


def test_bubble_sort_eq_10():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 62, 12,68]
    descending_arr = [90, 68, 64, 62, 34, 25, 22, 12, 12, 11]
    ascending_arr = [11, 12, 12, 22, 25, 34, 62, 64, 68, 90]

    ascending_result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    descending_result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (ascending_result == ascending_arr and descending_arr == descending_result)


def test_bubble_sort_descending_mt_10():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 12, 34, 23, 76]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 1)


def test_bubble_sort_ascending_lt_10():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 2)


def test_bubble_sort_no_numbers():
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 0)


def test_bubble_sort_not_all_int():
    result = []
    input_arr = [64, 34, 25, "asdf", 22, 11, 90, 'a', "gjslkdfj", 5.5]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 3)



