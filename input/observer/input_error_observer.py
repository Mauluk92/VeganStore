from input.observer.observer import Observer
from exception.input_exception import InputException


class InputErrorObserver(Observer):
    """
    An observer which raises an :class:`InputException` error whenever the input is wrong
    """
    def __init__(self):
        self.state = []

    def change_state(self, error: str):
        raise InputException(error)

