import socket
import selectors
import os
from undo_redo.invoker import Invoker
from undo_redo.history import History


class Client:
    def __init__(self):
        self.socket_set()
        self.selector_set()
        self.history: History = None
        self.invoker = Invoker()

    def socket_listen(self):
        if ACCEPT_TASK_SOCKET_IP in os.environ and \
           ACCEPT_TASK_SOCKET_PORT in os.environ:
            self.socket = socket.Socket()
            self.socket.bind(
                os.environ[ACCEPT_TASK_SOCKET_IP],
                os.environ[ACCEPT_TASK_SOCKET_PORT],
            )
            self.socket.listen()
            self.socket.set_blocking(False)
        else:
            raise Exception(
                'ACCEPT_TASK_SOCKET_IP or ACCEPT_TASK_SOCKET_PORT is not set'
            )

    def selector_start(self):
        self.selector = selector.DefaultSelector()
        self.selector.register(
            self.socket,
            selectors.EVENT_READ,
            self.task_accept,
        )

    def task_accept(self, socket):
        connect, _ = socket.accept()
        data = connect.recv(2048)
        self.invoke_command(data.decode('utf-8'))

    def invoke_command(command_code: str):
        if command_code == 'up':
            self.invoker.set_command(
                Up()
            )
            self.history = self.invoker.execute(self.history)
        elif command_code == 'down':
            self.invoker.set_command(
                Down()
            )
            self.history = self.invoker.execute(self.history)
        elif command_code == 'undo':
            self.invoker.set_command(
                Undo()
            )
            self.history = self.invoker.execute(self.history)
        elif command_code == 'redo':
            self.invoker.set_command(
                Redo()
            )
            self.history = self.invoker.execute(self.history)

