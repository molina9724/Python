import pytest
import json
from pathlib import Path
from _pytest.nodes import Item
from _pytest.main import Session
from _pytest.config import Config
import os
import time


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


# def pytest_collection_modifyitems(session: Session, config: Config, items: list[Item]):
#     smoke = list()
#     regression = list()
#     others = list()

#     for item in items:
#         if item.get_closest_marker("smoke"):
#             smoke.append(item)
#         elif item.get_closest_marker("regression"):
#             regression.append(item)
#         else:
#             others.append(item)

#     items[:] = others + regression + smoke


# def pytest_collection_modifyitems(session: Session, config: Config, items: list[Item]):
#     smoke = list()
#     regression = list()
#     others = list()

#     for item in items:
#         if item.get_closest_marker("smoke"):
#             smoke.append(item)
#         elif item.get_closest_marker("regression"):
#             regression.append(item)
#         else:
#             others.append(item)

#     if os.environ.get("LOGNAME") == "daniel_molina":
#         print(
#             f"Since 'LOGNAME' is not what I expected then we're removing all the test cases that don't have either the smoke or regression mark, which are the following: {others}"
#         )
#         items[:] = smoke + regression


# def pytest_sessionstart(session: Session):
#     session._start_time = time.time()  # type: ignore[attr-defined]


# def pytest_sessionfinish(session: Session, exitstatus):
#     start = getattr(session, "_start_time", None)
#     if start is not None:
#         duration = time.time() - start
#         print(f"Total duration: {duration:.2f} seconds")
#     else:
#         print("No start time found.")
#     finish = time.time()

#     reporter = session.config.pluginmanager.get_plugin("terminalreporter")

#     print("Test is finished, here are the results:")
#     print(f"Test cases collected: {session.testscollected}")

#     try:
#         passed_test_cases = len(reporter.stats["passed"])  # type: ignore
#         print(f"Test cases passed: {passed_test_cases}")
#     except KeyError:
#         print("No test cases passed")

#     print(f"Amount of test cases failed: {session.testsfailed}")
#     if hasattr(exitstatus, "name"):
#         print(f"The final status is: {exitstatus.name}")
#     else:
#         print("The final status is successful")
#     if (start is not None) and (finish is not None):  # usually only start can be None
#         duration = finish - start
#         print(duration)


# def pytest_runtest_setup(item: Item):
#     if item.get_closest_marker("smoke"):
#         pytest.skip("Just skipping if you have the smoke mark")


def pytest_configure(config: Config):
    config.addinivalue_line(
        "markers",
        "custom_marker: Marker created via pytest_configure",
    )
    print("This is the global config and I'm the boss here")
    config._boss = "CJ"  # type: ignore
    config._custom = True  # type: ignore


def pytest_collection_modifyitems(session: Session, config: Config, items: list[Item]):
    print(f"Verifying who's the boss after global changes: {config._boss}")  # type: ignore
    print(f"Running custom config: {config._custom}")  # type: ignore
