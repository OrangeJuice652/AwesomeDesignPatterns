from undo_redo.command Import ICommand
from .history Import History


class Invoker:
    command: ICommand = None

    def set_command(self, command: ICommand):
        self.command = command

    def execute(self, history: History):
        return self.command.execute(history)

