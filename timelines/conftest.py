import pytest
from xdist.scheduler import LoadScopeScheduling

class FifoBasedScheduler(LoadScopeScheduling):

    def _split_scope(self, nodeid):
        return nodeid

@pytest.hookimpl(tryfirst=True)
def pytest_xdist_make_scheduler(config, log):
    return FifoBasedScheduler(config, log)


@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(session, config, items):
    durations = config.cache.get("test_durations", [])
    duration_dict = {nodeid: duration for nodeid, duration in durations}

    items.sort(key=lambda item: duration_dict.get(item.nodeid, 0), reverse=True)


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    durations = []
    for test in terminalreporter.stats.get('passed', []):
        durations.append((test.nodeid, test.duration))
    for test in terminalreporter.stats.get('failed', []):
        durations.append((test.nodeid, test.duration))
    for test in terminalreporter.stats.get('skipped', []):
        durations.append((test.nodeid, test.duration))

    config.cache.set("test_durations", durations)
    print(config.cache._cachedir)
