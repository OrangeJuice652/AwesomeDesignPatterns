from undo_redo.commands.i_command import ICommand
from .history import History


class Invoker:
    command: ICommand = None

    def set_command(self, command: ICommand):
        self.command = command

    def execute(self, history: History):
        print('invoker.execute')
        return self.command.execute(history)

