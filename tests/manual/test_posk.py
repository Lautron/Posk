# To run add -s flag to pytest

import tests.mocks as mocks
import pytest


def assert_input():
    it_worked = bool(input("\nWrite anything to pass test:\n"))
    assert it_worked


@pytest.mark.editor
def test_opening_with_editor():
    posk = mocks.get_mock_posk()
    posk._open_tasks_input_with_editor()
    assert_input()


@pytest.mark.timer
def test_termdown():
    posk = mocks.get_mock_posk()
    entries = mocks.get_mock_timer_entries()
    posk.run_timer(entries)
    assert_input()


@pytest.mark.integration
def test_integration():
    mock_file = mocks.get_mock_csv_file()
    posk = mocks.get_mock_posk()
    tasks = posk._parse_tasks(mock_file)
    entries = posk.get_timer_entries(tasks)
    posk.run_timer(entries)
