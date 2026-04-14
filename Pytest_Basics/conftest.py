import pytest
import json
from pathlib import Path
from _pytest.nodes import Item
from _pytest.main import Session
from _pytest.config import Config


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
    parser.addoption(
        "--api-key",
        action="store",
        choices=(
            "key1",
            "key2",
            "key3",
        ),
    )
    parser.addoption(
        "--test-data",
        action="append",
        choices=("0", "1", "2"),
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


@pytest.fixture
def api_key(request):
    value = request.config.getoption("--api-key")
    if value is None:
        raise KeyError("You must provide --api-key to run these tests.")
    return value


# def pytest_generate_tests(metafunc):
#     if "dynamic_input" in metafunc.fixturenames:
#         test_data = [1, 2, 3, 4]
#         metafunc.parametrize("dynamic_input", test_data)


@pytest.fixture
def test_data(request):
    return request.config.getoption("--test-data")


# def pytest_generate_tests(metafunc):
#     if "test_data" in metafunc.fixturenames:
#         data = metafunc.config.getoption("--test-data")
#         if not data:
#             data = []
#         metafunc.parametrize("test_data", data)


# def pytest_generate_tests(metafunc):
#     if "user_type" in metafunc.fixturenames:
#         test_data = ["admin", "user", "guest"]
#         metafunc.parametrize("user_type", test_data)
#     elif "permission" in metafunc.fixturenames:
#         test_data = ["read", "write", "read_and_write"]
#         metafunc.parametrize("permission", test_data)


json_test = Path(
    "/Users/daniel_molina/Downloads/Python/Python/Pytest_Basics/json_test.json"
)

data = {
    1: True,
    2: True,
    3: True,
    4: False,
    5: False,
}

with open(json_test, "w") as json_file:
    json.dump(data, json_file)


def pytest_generate_tests(metafunc):
    if "json_data" in metafunc.fixturenames:
        metafunc.parametrize("json_data", data.keys())


# def pytest_collection_finish(session: pytest.Session):
#     for item in session.items:
#         print(f"Test name: {item.name} - Test location: {item.location}")
#     print(f"Total amount of test cases: {len(session.items)}")


def pytest_collection_finish(session: pytest.Session):
    smoke_test_cases = []
    regression_test_cases = []
    for item in session.items:
        if item.get_closest_marker("smoke") is not None:
            smoke_test_cases.append(item.name)
        if item.get_closest_marker("regression") is not None:
            regression_test_cases.append(item.name)
    if smoke_test_cases:
        print(
            f"'smoke' marker was found {len(smoke_test_cases)} times. The following are the test cases marked with it: {smoke_test_cases}"
        )
    if regression_test_cases:
        print(
            f"'regression' marker was found {len(regression_test_cases)} times. The following are the test cases marked with it: {regression_test_cases}"
        )


def pytest_collection_modifyitems(session: Session, config: Config, items: list[Item]):
    smoke = list()
    regression = list()
    others = list()

    for item in items:
        if item.get_closest_marker("smoke"):
            smoke.append(item)
        elif item.get_closest_marker("regression"):
            regression.append(item)
        else:
            others.append(item)

    items[:] = others + regression + smoke
