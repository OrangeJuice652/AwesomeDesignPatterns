import socket
import selectors
import os
from undo_redo.invoker import Invoker
from undo_redo.history import History
from undo_redo.commands import (
    Up,
    Down,
    Undo,
    Redo,
)


class Client:
    def __init__(self):
        self.socket_listen()
        self.selector_start()
        self.history: History = History()
        self.invoker = Invoker()

    def command_listen(self):
        while True:
            events = self.selector.select()
            for key, event_mask in events:
                key.data(key.fileobj)

    def socket_listen(self):
        if 'ACCEPT_TASK_SOCKET_IP' in os.environ and \
           'ACCEPT_TASK_SOCKET_PORT' in os.environ:
            self.socket = socket.socket()
            self.socket.bind(
                (os.environ['ACCEPT_TASK_SOCKET_IP'],
                int(os.environ['ACCEPT_TASK_SOCKET_PORT']))
            )
            self.socket.listen()
            self.socket.setblocking(False)
        else:
            raise Exception(
                'ACCEPT_TASK_SOCKET_IP or ACCEPT_TASK_SOCKET_PORT is not set'
            )

    def selector_start(self):
        self.selector = selectors.DefaultSelector()
        self.selector.register(
            self.socket,
            selectors.EVENT_READ,
            self.task_accept,
        )

    def task_accept(self, socket):
        connect, _ = socket.accept()
        data = connect.recv(2048)
        self.invoke_command(data.decode('utf-8'))
        connect.close()

    def invoke_command(self, command_code: str):
        print(f'invoke_command: {command_code}')
        print(f'before history: {self.history.current}')
        if command_code == 'up':
            print('up command is invoked')
            self.invoker.set_command(
                Up()
            )
            self.history = self.invoker.execute(self.history)
        elif command_code == 'down':
            print('down command is invoked')
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
        print(f'after history: {self.history.current}')

