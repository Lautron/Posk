import tests.mocks as mocks
import pytest

pytestmark = pytest.mark.skip(reason="These tests are executed manually")


def test_termdown():
    posk = mocks.get_mock_posk()
    entries = mocks.get_mock_timer_entries()
    posk.run_timer(entries)


if __name__ == "__main__":
    test_termdown()
