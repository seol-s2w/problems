from ..small import Small


def test_Small_str():
    assert str(Small([0])) == "0.0"
    assert str(Small([0, 0, 0])) == "0.000"
    assert str(Small([0, 0, 0, 1])) == "0.0001"
    assert str(Small([1, 0, 0, 0])) == "0.1000"
    assert str(Small([1, 2, 3, 4])) == "0.1234"
    assert str(Small([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == "0.000000000000000000001"


def test_Small_repr():
    assert repr(Small([0])) == "Small([0])"
    assert repr(Small([0, 0, 0])) == "Small([0, 0, 0])"
    assert repr(Small([1, 2, 3, 4])) == "Small([1, 2, 3, 4])"


def test_Small_abs():
    assert abs(Small([0, 0, 0])) == 0.0
    assert abs(Small([1, 2, 3, 4])) == 0.1234
    assert abs(Small([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])) == 0.1234123412341234


def test_Small_len():
    assert len(Small([0])) == 1
    assert len(Small([0, 0, 0])) == 3
    assert len(Small([1, 2, 3, 4])) == 4
    assert len(Small([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == 30


def test_Small_getitem():
    zero = Small([0])
    assert zero[0] == 0
    assert zero[:] == "0.0"

    s = Small([0, 1, 2, 3, 4, 5, 6])
    assert s[1] == 1
    assert s[-1] == 6
    assert s[2:5] == "0.0023400"
    assert s[3:] == "0.0003456"
    assert s[:-2] == "0.0123400"
