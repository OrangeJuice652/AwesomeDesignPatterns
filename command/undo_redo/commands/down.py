from undo_redo.history import History
from .i_command import ICommand


class Down(ICommand):
    def __init__(self, undo=False):
        self._undo = undo

    def undo_command(self):
        return Down(undo=True)
 
    def execute(self, history: History):
        history.current -= 1
        if not self._undo:
            history.append_command(self)
        print(f'history.current: {history.current}')
        return self.history

