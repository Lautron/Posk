from abc import ABC, abstractmethod
from helpers import TimerEntry
import subprocess


class AbstractTrackerStrategy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def start_time_entry(self, entry: TimerEntry):
        """Add time entry on time tracking service

        :task: TODO
        :returns: TODO

        """
        pass

    @abstractmethod
    def stop_time_entry(self):
        """Stop time entry on time tracking service

        :task: TODO
        :returns: TODO

        """
        pass


class TogglTrackerStrategy(AbstractTrackerStrategy):
    def __init__(self):
        pass

    def start_time_entry(self, entry: TimerEntry):
        """Add time entry on time tracking service

        :task: TODO
        :returns: TODO

        """
        if entry.project == "break":
            return
        command = f"toggl start -o '{entry.project}' '{entry.description}'"
        subprocess.run(command, shell=True)

    def stop_time_entry(self):
        """Stop time entry on time tracking service

        :task: TODO
        :returns: TODO

        """
        subprocess.run("toggl stop", shell=True)
