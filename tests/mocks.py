from inputs import CSVInputFormat
from helpers import Task
import io

task_info = [
    ("Work on Posk", "code", "4", "2"),
    ("Plan project on Jira", "planning", "2", "1"),
]


def get_mock_csv_file():
    parser = CSVInputFormat()
    tasks_string = "\n".join([", ".join(task) for task in task_info])
    mock_contents = f"{parser.get_input_template()}\n{tasks_string}"
    mock_file = io.StringIO(mock_contents)
    return mock_file


def get_mock_tasks():
    return [Task(*task) for task in task_info]
