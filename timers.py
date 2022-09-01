from abc import ABC, abstractmethod
from helpers import TimerEntry
import subprocess


class AbstractTimerStrategy(ABC):
    template = ""

    @abstractmethod
    def _get_args_from_entry(self, entry: TimerEntry):
        pass

    @abstractmethod
    def run(self, entry: TimerEntry) -> None:
        pass


class TermdownStrategy(AbstractTimerStrategy):
    def _get_args_from_entry(self, entry: TimerEntry):
        return ["--title", f"'{entry.description}'", f"{entry.duration}"]

    def run(self, entry: TimerEntry) -> None:
        args = self._get_args_from_entry(entry)
        command = ["termdown"] + args
        subprocess.run(command)
