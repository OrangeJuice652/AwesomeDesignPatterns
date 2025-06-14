from typing import Optional
from undo_redo.history import History
from .i_command import ICommand


class Undo(ICommand):
    def execute(self, history: History):
        try:
            command: Optional[ICommand] = history.pop_last_command()
        except IndexError:
            print('the command history is empty')
            return history
        else:
            return command.undo_command().execute(history)

