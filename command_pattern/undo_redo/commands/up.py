from undo_redo.history import History
from undo_redo.commands import (
    ICommand,
)


class Up(ICommand):

    def __init__(self, undo=False):
        self._undo = undo

    def undo_command(self):
        # circle import対策
        from undo_redo.commands import Down
        return Down(undo=True)

    def execute(self, history: History):
        history.current += 1
        if not self._undo:
            history.append_history(self)
        return history

