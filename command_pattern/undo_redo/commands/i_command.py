from abc import ABC
from undo_redo.history import History


class ICommand(ABC):
    def execute(history: History):
        pass

