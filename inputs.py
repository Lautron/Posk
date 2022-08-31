import csv
from abc import ABC, abstractmethod
from helpers import Task


class AbstractInputFormatStrategy(ABC):
    template = ""

    @abstractmethod
    def create_file(self, path, filename):
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

    def create_file(self, path, filename):
        with open(f"{path}{filename}", "w") as file_obj:
            file_obj.write(self.template)

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
