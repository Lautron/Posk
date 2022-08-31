from abc import ABC, abstractmethod
from helpers import Task
from trackers import AbstractTrackerStrategy
from inputs import AbstractInputFormatStrategy
from config import Config


class PoskContext:
    def __init__(
        self,
        config: Config,
        input_format_strategy: AbstractInputFormatStrategy,
        tracker_strategy: AbstractTrackerStrategy,
    ):
        self.config = config
        self.input_format_strategy = input_format_strategy
        self.tracker_strategy = tracker_strategy

    def _get_tasks_template(self):
        return self.input_format_strategy.get_input_template()

    def _open_tasks_input_with_editor(self):
        pass

    def _store_tasks(self):
        pass

    def _parse_tasks(self, file) -> list[Task]:
        return self.input_format_strategy.parse_tasks(file)

    def run_timer(self):
        pass

    def _notify_user(self):
        pass

    def _add_time_entry(self, task: Task):
        return self.tracker_strategy.add_time_entry(task)

    def _stop_time_entry(self):
        return self.tracker_strategy.stop_time_entry()
