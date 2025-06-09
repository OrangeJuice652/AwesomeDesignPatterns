class Commit(ICommand):
    logger: Logger

    def __init__(self, logger):
        self.logger = logger

    def execute(user_email, user_encrypted_password):
        self._commit_a_user(user_email, user_encrypted_password)
        self.logger.set_saved_user(user_email, user_encrypted_password)
        return self.logger

    def _commit_a_user():
        # save a user to storage
        pass
