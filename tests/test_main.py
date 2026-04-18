import pytest
from your_module import classify_name

@pytest.mark.parametrize("name, expected", [
    ("Ali", "Oddiy"),
    ("John", "O‘rtacha"),
    ("Alexander", "Murakkab"),
    ("Bob", "Oddiy"),
    ("Christopher", "Murakkab"),
])
def test_classify_name(name, expected):
    assert classify_name(name) == expected

def test_classify_name_empty():
    with pytest.raises(ValueError):
        classify_name("")

def test_classify_name_none():
    with pytest.raises(ValueError):
        classify_name(None)
