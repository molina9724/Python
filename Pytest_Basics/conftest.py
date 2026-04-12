import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        choices=("dev", "staging", "prod"),
        help="my option: dev/staging/prod",
    )
    parser.addoption(
        "--slow",
        action="store_true",
    )
    parser.addoption(
        "--mybrowser",
        action="append",
        help="Specify browsers to test (can be used multiple times)",
    )


@pytest.fixture
def env(request):
    return request.config.getoption("--env")


@pytest.fixture
def slow(request):
    return request.config.getoption("--slow")


@pytest.fixture
def browser(request):
    return request.config.getoption("--mybrowser")
