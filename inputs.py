import csv
from abc import ABC, abstractmethod
from helpers import Task


class AbstractInputFormatStrategy(ABC):
    template = ""

    def __init__(self):
        pass

    @abstractmethod
    def set_input_template(self, template):
        """Set default input config template

        :returns: TODO

        """
        pass

    @abstractmethod
    def get_input_template(self):
        """Get default input config template

        :returns: TODO

        """
        pass

    @abstractmethod
    def parse_tasks(self, file) -> list[Task]:
        """Stop time entry on time tracking service

        :task: TODO
        :returns: TODO

        """
        pass


class CSVInputFormat(AbstractInputFormatStrategy):
    template = (
        "description, project, work_sets, take_break_after_how_many_work_sets"
    ) + "\n"

    def __init__(self):
        pass

    def set_input_template(self, template):
        self.template = template

    def get_input_template(self):
        """Get default input config template

        :returns: TODO
        """

        return self.template

    def parse_tasks(self, file) -> list[Task]:
        """Stop time entry on time tracking service

        :task: TODO
        :returns: TODO
        """
        reader = csv.reader(file, skipinitialspace=True)
        reader = iter(reader)  # Skip header row
        next(reader)
        tasks = [Task(*row) for row in reader if row]
        return tasks
