import pytest


@pytest.mark.skip(reason="Skipping this one")
def test_sample():
    assert True


@pytest.mark.skipif(3 > 2)
def test_sample_2():
    assert False


@pytest.mark.xfail
def test_sample_3():
    assert False


@pytest.mark.my_mark
def test_sample_value():
    assert True


@pytest.mark.parametrize(
    ("a", "b", "results"), [(1, 2, 3), (1, 1, 2), (0, 1, 1), (5, 5, 10), (1, -1, 0)]
)
def test_add_parametrize(a, b, results):
    assert a + b == results
