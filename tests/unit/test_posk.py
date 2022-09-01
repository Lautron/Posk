from posk import PoskContext
import tests.mocks as mocks


def test_timer_entries():
    posk = PoskContext(mocks.MockConfig(), None, None, None)
    tasks = mocks.get_mock_tasks()
    assert posk.get_timer_entries(tasks) == mocks.get_mock_timer_entries()
