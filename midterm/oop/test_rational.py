from rational import Rational

def test_add():
    rational = Rational(2,3)
    other_rational = Rational(3,4)
    rational.add(other_rational)

    expected = "17/12"
    actual = str(rational)

    assert actual == expected

def test_mulitplication():
    rational = Rational(2,3)
    other_rational = Rational(3,4)
    rational.multiply(other_rational)

    expected = "6/12"
    actual = str(rational)

    assert actual == expected


if __name__ == "__main__":
    import pytest
    pytest.main()
    