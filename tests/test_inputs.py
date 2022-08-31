from inputs import CSVInputFormat
import io
import tests.mocks as mocks


def test_csv_parser():
    parser = CSVInputFormat()
    mock_file = mocks.get_mock_csv_file()
    tasks = parser.parse_tasks(mock_file)
    mock_tasks = mocks.get_mock_tasks()
    assert tasks == mock_tasks
