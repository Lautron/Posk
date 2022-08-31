import subprocess
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

    def _open_tasks_input_with_editor(self):
        folder_path = Config.tmp_files_folder
        tmp_filename = "tmp_tasks"
        command = f"$EDITOR {folder_path}{tmp_filename}"
        self.input_format_strategy.create_file(folder_path, tmp_filename)
        subprocess.Popen(command, shell=True)

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
