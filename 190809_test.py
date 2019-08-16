# 더블 함수 만들기

def double(n):  # n = parameter
    return n * 2


def test_double():
    assert double(2) ==4
    assert double(1234) ==2468
    assert double(1) ==2


def test_simpel():
    assert 1 + 1 == 2
