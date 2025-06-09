class RemoveUser(ICommand):
    logger: Logger

    def __init__(self, logger):
        self.logger = logger

    def execute(user_email, user_encrypted_password):
        self._remove_a_user(user_email, user_encrypted_password)
        self.logger.set_removed_user(user_email, user_encrypted_password)
        return self.logger

    def _remove_a_user(user_email, user_encrypted_password):
        # remove a user from storage
        pass
