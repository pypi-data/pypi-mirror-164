from typing import Callable
from MarkLib.taskstage import TaskStage
from MarkLib.taskitem import TaskItem
from .models.condition import Condition


class Task:
    description: str = ""
    stages: list[TaskStage] = []
    solution_method: Callable = None
    item_answer_builder = None

    def __init__(self, condition: Condition):
        self.condition = condition
        raw_answers = self.__class__.solution_method(*self.unwrapped_condition)
        answers = self.item_answer_builder.build(raw_answers)
        self.stages = [
            stage_class(answers) 
            for stage_class
            in self.__class__.stages
        ]

    @property
    def items(self) -> list[TaskItem]:
        return [item for stage in self.stages for item in stage.items]

    @property
    def answers(self):
        return [item.answer for item in self.items]
