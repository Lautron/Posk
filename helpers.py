from collections import namedtuple
from dataclasses import dataclass


@dataclass
class Task:
    def __init__(
        self, description, project, work_sets, take_break_after_how_many_work_sets
    ):
        self.description = description
        self.project = project
        self.work_sets = int(work_sets)
        self.take_break_after_how_many_work_sets = int(
            take_break_after_how_many_work_sets
        )


TimerEntry = namedtuple("TimerEntry", ["project", "description", "duration"])
