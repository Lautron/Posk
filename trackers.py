from abc import ABC, abstractmethod
from helpers import Task


class AbstractTrackerStrategy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def add_time_entry(self, task: Task):
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

    def add_time_entry(self, task):
        """Add time entry on time tracking service

        :task: TODO
        :returns: TODO

        """
        pass

    def stop_time_entry(self):
        """Stop time entry on time tracking service

        :task: TODO
        :returns: TODO

        """
        pass
