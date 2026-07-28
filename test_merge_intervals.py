from merge_intervals import merge


def test_empty():
    assert merge([]) == []


def test_single():
    assert merge([[1, 4]]) == [[1, 4]]


def test_overlap():
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_touching():
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]


def test_unsorted():
    assert merge([[8, 10], [1, 3], [2, 6], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_nested():
    assert merge([[1, 10], [2, 3], [4, 5]]) == [[1, 10]]


def test_no_mutation():
    src = [[3, 5], [1, 2]]
    merge(src)
    assert src == [[3, 5], [1, 2]]
