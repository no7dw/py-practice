import pytest
'''
"test_input,expected", [
    ("3+5", 8), --- input '3+5' expected 8
    ("2+4", 6), --- input '2+4' expected 6
    ("6*9", 54),--- input '6*9' expected 54
]
'''
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54),
])
def test_eval(test_input, expected):
    assert expected == eval(test_input)