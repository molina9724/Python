import pytest


@pytest.fixture()
def override():
    return False


def test_override(override):
    assert override
