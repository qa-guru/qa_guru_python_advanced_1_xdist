import json

import pytest


@pytest.fixture
def get_test_user_id():
    with open("test_data.json", "r") as f:
        data = json.load(f)
    user_id, _ = next(filter(lambda item: item[1] is False, data.items()))

    data[user_id] = True
    with open("test_data.json", "w") as f:
        json.dump(data, f)

    yield user_id


def test_first(get_test_user_id):
    assert get_test_user_id == "1"

def test_second(get_test_user_id):
    assert get_test_user_id == "2"

def test_third(get_test_user_id):
    assert get_test_user_id == "3"

