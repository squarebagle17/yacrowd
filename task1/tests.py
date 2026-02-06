import pytest
import calculations


@pytest.mark.parametrize(
    "test_input,expected", [("4\n1 3\n3 1\n4 4\n7 1", "3"),
                            ("3\n1 8\n10 11\n21 5", "5"),
                            ("10\n2 1\n22 10\n26 17\n29 2\n45 20\n47 32\n72 12\n75 1\n81 31\n97 7", "57")]
)
def test_humidifier(test_input, expected):
    assert calculations.humidifier_calc(test_input) == expected
