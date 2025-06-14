from undo_redo.history import History
from undo_redo.commands import (
    ICommand,
)


class Down(ICommand):
    def __init__(self, undo=False):
        self._undo = undo

    def undo_command(self):
        from undo_redo.commands import Up
        return Up(undo=True)
 
    def execute(self, history: History):
        history.current -= 1
        if not self._undo:
            history.append_history(self)
        print(f'history.current: {history.current}')
        return history

