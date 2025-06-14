from undo_redo.client import Client

if __name__ == '__main__':
    client = Client()
    client.command_listen()
