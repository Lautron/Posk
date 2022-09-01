import subprocess
from abc import ABC, abstractmethod
from helpers import Task, TimerEntry
from trackers import AbstractTrackerStrategy
from inputs import AbstractInputFormatStrategy
from config import Config
from timers import AbstractTimerStrategy


class PoskContext:
    def __init__(
        self,
        config: Config,
        input_format_strategy: AbstractInputFormatStrategy,
        tracker_strategy: AbstractTrackerStrategy,
        timer_strategy: AbstractTimerStrategy,
    ):
        self.config = config
        self.input_format_strategy = input_format_strategy
        self.tracker_strategy = tracker_strategy
        self.timer_strategy = timer_strategy

    def _open_tasks_input_with_editor(self):
        folder_path = self.config.tmp_files_folder
        tmp_filename = "tmp_tasks"
        command = f"$EDITOR {folder_path}{tmp_filename}"
        self.input_format_strategy.create_file(folder_path, tmp_filename)
        subprocess.call(command, shell=True)

    def _store_tasks(self):
        pass

    def _parse_tasks(self, file) -> list[Task]:
        return self.input_format_strategy.parse_tasks(file)

    def get_timer_entries(self, tasks: list[Task]) -> list[TimerEntry]:
        entries = []
        for task in tasks:
            for task_num in range(1, task.work_sets + 1):
                work_entry = TimerEntry(
                    "work", task.description, self.config.work_set_duration
                )
                entries.append(work_entry)

                should_take_break = (
                    task_num % task.take_break_after_how_many_work_sets == 0
                )
                if should_take_break:
                    break_entry = TimerEntry(
                        "break", "Break", self.config.break_duration
                    )
                    entries.append(break_entry)

        return entries

    def run_timer(self, entries: list[TimerEntry]):
        for entry in entries:
            try:
                self.timer_strategy.run(entry)
            except KeyboardInterrupt:
                print("Skipping timer...")
                continue

    def _notify_user(self):
        pass

    def _add_time_entry(self, task: Task):
        return self.tracker_strategy.add_time_entry(task)

    def _stop_time_entry(self):
        return self.tracker_strategy.stop_time_entry()
