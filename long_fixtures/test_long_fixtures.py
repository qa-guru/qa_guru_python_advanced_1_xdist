import time

import pytest


@pytest.fixture(scope="module")
def fixture():
    time.sleep(1)


@pytest.mark.parametrize("i", range(10))
def test_something(i, fixture):
    pass
