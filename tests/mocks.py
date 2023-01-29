from inputs import CSVInputFormat
from timers import TermdownStrategy
from posk import PoskContext
from trackers import TogglTrackerStrategy

from config import Config
from helpers import Task, TimerEntry
import io


class MockConfig(Config):
    tmp_files_folder = "./tests/"
    work_set_duration = 25
    break_duration = 5
    notify_command = "dunstify '$1' '$2'"
    take_longer_break_after_how_many_work_sets = 4
    long_break_multiplier = 2
    enable_tracker = False
    notify_sound_filename = "~/.config/alarm/alarm.mp3"


def get_mock_posk():
    return PoskContext(
        MockConfig(), CSVInputFormat(), TogglTrackerStrategy(), TermdownStrategy()
    )


task_info = [
    ("Work on Posk", "code", "4", "2"),
    ("Plan project on Jira", "planning", "2", "1"),
]

timer_entries = [
    TimerEntry("code", "Work on Posk #1", 25),
    TimerEntry("code", "Work on Posk #2", 25),
    TimerEntry("break", "Break", 10),
    TimerEntry("code", "Work on Posk #3", 25),
    TimerEntry("code", "Work on Posk #4", 25),
    TimerEntry("break", "Break", 20),
    TimerEntry("planning", "Plan project on Jira #1", 25),
    TimerEntry("break", "Break", 5),
    TimerEntry("planning", "Plan project on Jira #2", 25),
    TimerEntry("break", "Break", 5),
]


def get_mock_csv_file():
    parser = CSVInputFormat()
    tasks_string = "\n".join([", ".join(task) for task in task_info])
    mock_contents = f"{parser.template}\n{tasks_string}"
    path = f"{MockConfig.tmp_files_folder}test"
    with open(path, "w") as fileobj:
        fileobj.write(mock_contents)

    return path


def get_mock_tasks():
    return [Task(*task) for task in task_info]


def get_mock_timer_entries():
    return timer_entries
