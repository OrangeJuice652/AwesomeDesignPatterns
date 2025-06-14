from typing import List
from undo_redo.commands.i_command import ICommand


class History:
    def __init__(self):
        self.current = 0
        self._command_history: List[ICommand]

    def pop_last_command(self):
        return self._command_history.pop(-1)

    def last_command(self):
        return self._command_history[-1]

    def append_history(self, command: ICommand):
        self._command_history.append(command)

