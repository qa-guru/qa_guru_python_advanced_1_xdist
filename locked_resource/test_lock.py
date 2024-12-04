import json
import random
import time
from filelock import FileLock

import pytest

# @pytest.fixture(scope="session")
# def session_fixture(tmp_path_factory, worker_id):
#     time.sleep(3)
#     n = random.randint(0, 100)
#     return n

@pytest.fixture(scope="session")
def session_fixture(tmp_path_factory, worker_id):
    def _produce_expensive_data():
        time.sleep(3)
        n = random.randint(0, 100)
        return n

    if worker_id == "master":
        return _produce_expensive_data()

    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "data.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = _produce_expensive_data()
            fn.write_text(json.dumps(data))
    return data

def test_example_1(session_fixture):
    assert session_fixture == -1, f"Random number is not -1 but {session_fixture}"

def test_example_2(session_fixture):
    assert session_fixture == -2, f"Random number is not -2 but {session_fixture}"
