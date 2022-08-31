from abc import ABC, abstractmethod
from typing import Optional
from helpers import Task
from trackers import AbstractTrackerStrategy
from inputs import AbstractInputFormatStrategy


class PoskContext:
    def __init__(self, config: Config):
        self.config = config
        self.input_format_strategy: Optional[AbstractInputFormatStrategy] = None
        self.tracker_strategy: Optional[AbstractTrackerStrategy] = None

    def set_tracker_strategy(self, strategy: AbstractTrackerStrategy):
        self.tracker_strategy = strategy

    def set_input_format_strategy(self, strategy: AbstractInputFormatStrategy):
        self.input_format_strategy = strategy

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
