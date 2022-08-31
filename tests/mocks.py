from inputs import CSVInputFormat
from config import Config
from helpers import Task, TimerEntry
import io


class MockConfig(Config):
    tmp_files_folder = "./tmp/"
    work_set_duration = "25m"
    break_duration = "5m"


task_info = [
    ("Work on Posk", "code", "4", "2"),
    ("Plan project on Jira", "planning", "2", "1"),
]

timer_entries = [
    TimerEntry("work", "Work on Posk", "25m"),
    TimerEntry("work", "Work on Posk", "25m"),
    TimerEntry("break", "Break", "5m"),
    TimerEntry("work", "Work on Posk", "25m"),
    TimerEntry("work", "Work on Posk", "25m"),
    TimerEntry("break", "Break", "5m"),
    TimerEntry("work", "Plan project on Jira", "25m"),
    TimerEntry("break", "Break", "5m"),
    TimerEntry("work", "Plan project on Jira", "25m"),
    TimerEntry("break", "Break", "5m"),
]


def get_mock_csv_file():
    parser = CSVInputFormat()
    tasks_string = "\n".join([", ".join(task) for task in task_info])
    mock_contents = f"{parser.template}\n{tasks_string}"
    mock_file = io.StringIO(mock_contents)
    return mock_file


def get_mock_tasks():
    return [Task(*task) for task in task_info]


def get_mock_timer_entries():
    return timer_entries
