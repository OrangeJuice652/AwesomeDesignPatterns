from typing import Optional
from undo_redo.history import History
from .i_command import ICommand


class Redo(ICommand):
    def execute(self, history: History):
        try:
            command: Optional[ICommand] = history.last_command()
        except IndexError:
            print('the command history is empty')
            return history
        else:
            return command.execute(history)

