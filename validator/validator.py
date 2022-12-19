from abc import abstractmethod


class Validator:
    """
    Each validator is used by an input handler to validate its inputs :class:`InputHandler`
    """
    def __init__(self, error_message: str):
        self.error_message = error_message

    @abstractmethod
    def is_valid(self, data: any):
        pass
