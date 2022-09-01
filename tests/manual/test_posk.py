# To run add -s flag to pytest

import tests.mocks as mocks
import pytest


def assert_input():
    it_worked = bool(input("\nWrite anything to pass test:\n"))
    assert it_worked


def test_opening_with_editor():
    posk = mocks.get_mock_posk()
    posk._open_tasks_input_with_editor()
    assert_input()


@pytest.mark.skip(reason="Takes too long")
def test_termdown():
    posk = mocks.get_mock_posk()
    entries = mocks.get_mock_timer_entries()
    posk.run_timer(entries)
    assert_input()
