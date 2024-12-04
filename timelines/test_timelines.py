import time

import pytest


@pytest.mark.parametrize("i", range(100))
def test_fast(i):
    time.sleep(i / 1000)


@pytest.mark.parametrize("i", range(10))
def test_slow(i):
    time.sleep(i / 10)
