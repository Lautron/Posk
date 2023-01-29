import subprocess, os, sys
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
        self.tmp_filepath = None
        self.folder_path = os.path.expanduser(self.config.tmp_files_folder)
        self.is_first_entry = True

    def _open_tasks_input_with_editor(self):
        tmp_filename = "tmp_tasks"
        self.tmp_filepath = f"{self.folder_path}{tmp_filename}"
        command = f"$EDITOR {self.tmp_filepath}"
        self.input_format_strategy.create_file(self.folder_path, tmp_filename)
        subprocess.call(command, shell=True)

    def _store_tasks(self):
        pass

    def _parse_tasks(self, filepath) -> list[Task]:
        return self.input_format_strategy.parse_tasks(filepath)

    def get_timer_entries(self, tasks: list[Task]) -> list[TimerEntry]:
        entries = []
        for task in tasks:
            for task_num in range(1, task.work_sets + 1):
                work_entry = TimerEntry(
                    task.project,
                    f"{task.description} #{task_num}",
                    self.config.work_set_duration,
                )
                entries.append(work_entry)

                should_take_break = (
                    task_num % task.take_break_after_how_many_work_sets == 0
                )
                if should_take_break:
                    should_be_longer = (
                        task_num
                        % self.config.take_longer_break_after_how_many_work_sets
                        == 0
                    )
                    break_duration = (
                        self.config.break_duration
                        * task.take_break_after_how_many_work_sets
                    )
                    if should_be_longer:
                        break_duration *= self.config.long_break_multiplier

                    break_entry = TimerEntry("break", "Break", break_duration)
                    entries.append(break_entry)

        return entries

    def run_timer(self, entries: list[TimerEntry]):
        for entry in entries:
            try:
                self._notify_user(entry)
                self._add_time_entry(entry)
                self.timer_strategy.run(entry)
            except KeyboardInterrupt:
                print("Skipping timer...")

            self._stop_time_entry()

    @staticmethod
    def format_notify_command(command, entry):
        return command.replace("$1", entry.description).replace(
            "$2", f"{entry.duration}m"
        )

    def _notify_user(self, entry):
        command = self.format_notify_command(self.config.notify_command, entry)
        subprocess.run(command, shell=True)

        if self.is_first_entry:
            return

        sound_path = os.path.expanduser(self.config.notify_sound_filename)
        sound_command = f"play -v 0.5 {sound_path} 2> /dev/null"
        print("Press ctrl+c to stop ringing")
        while True:
            try:
                subprocess.run(sound_command, shell=True)
            except KeyboardInterrupt:
                break

    def _add_time_entry(self, entry: TimerEntry):
        self.is_first_entry = False
        if not self.config.enable_tracker:
            return
        return self.tracker_strategy.start_time_entry(entry)

    def _stop_time_entry(self):
        if not self.config.enable_tracker:
            return
        return self.tracker_strategy.stop_time_entry()

    def run(self):
        self._open_tasks_input_with_editor()
        tasks = self._parse_tasks(self.tmp_filepath)
        entries = self.get_timer_entries(tasks)
        self.run_timer(entries)
