from .i_command import ICommand


class CreateTask(ICommand):
    logger: Logger

    def __init__(self, logger):
        self.logger = logger

    def executet(task):
        self._commit_a_task(task)
        self.logger.set_saved_task(task)
        return self.logger

    def _save_a_task(task):
        # save a task to storage
        pass

