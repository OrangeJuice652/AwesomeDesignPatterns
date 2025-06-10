from .i_command import ICommand


class RemoveTask(ICommand):
    logger: Logger

    def __init__(self, logger):
        self.logger = logger

    def execute(task):
        self._remove_a_task(task_email, task_encrypted_password)
        self.logger.set_removed_task(task)
        return self.logger

    def _remove_a_task(task):
        # remove a task from storage
        pass
