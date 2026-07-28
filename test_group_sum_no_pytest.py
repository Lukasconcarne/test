from group_sum import group_sum


def test_empty():
    assert group_sum([], "k", "v") == []


def test_basic():
    rows = [{"k": "b", "v": 2}, {"k": "a", "v": 3}, {"k": "b", "v": 5}]
    assert group_sum(rows, "k", "v") == [("a", 3), ("b", 7)]


def test_single_group():
    rows = [{"k": "x", "v": 1}, {"k": "x", "v": 2}, {"k": "x", "v": 4}]
    assert group_sum(rows, "k", "v") == [("x", 7)]


def test_sorted_by_key():
    rows = [{"g": 3, "n": 1}, {"g": 1, "n": 1}, {"g": 2, "n": 1}]
    assert group_sum(rows, "g", "n") == [(1, 1), (2, 1), (3, 1)]


def test_missing_key_raises():
    try:
        group_sum([{"k": "a"}], "k", "v")
        assert False, "Should have raised KeyError"
    except KeyError:
        pass  # Expected


def test_floats():
    rows = [{"k": "a", "v": 0.5}, {"k": "a", "v": 0.25}]
    assert group_sum(rows, "k", "v") == [("a", 0.75)]


if __name__ == "__main__":
    test_empty()
    test_basic()
    test_single_group()
    test_sorted_by_key()
    test_missing_key_raises()
    test_floats()
    print("All tests passed!")
