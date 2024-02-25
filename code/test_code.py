
import pytest

def func(x):
    return x + 1


def test_answer():
    assert numbers_sum("no") == 781.0
    

retcode = pytest.main()