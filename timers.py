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
        return f"--title '{entry.description}' {entry.duration}"

    def run(self, entry: TimerEntry) -> None:
        args = self._get_args_from_entry(entry)
        command = f"termdown {args}"
        subprocess.run(command, shell=True)
