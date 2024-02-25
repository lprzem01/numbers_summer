from main_Code import numbers_sum
import pytest

def test_numbers_sum(monkeypatch):
    """test to check if defoult data returns correct number"""
    # Monkeypatch the "input" function to return "no".
    monkeypatch.setattr('builtins.input', lambda _: "no")

    # Call the function and assert the output.
    assert numbers_sum() == "781.0"

def test_data(monkeypatch):
    """test to check if test data returns correct output"""
    # Monkeypatch the "input" function to return "no".
    monkeypatch.setattr('builtins.input', lambda _: "yes")
    monkeypatch.setattr('builtins.input', lambda _: "data/test_data")

    # Call the function and assert the output.
    assert numbers_sum() == "2"

# Run the test
if __name__ == "__main__":
    pytest.main()

