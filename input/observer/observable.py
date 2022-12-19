from abc import abstractmethod
from typing import Callable

from input.observer.observer import Observer


class Observable:

    """
    Observable class: each observable has a notify function responsible for handling the
    interaction with an :class:`Observer`.
    See :class:`InputErrorObserver`
    """

    def __init__(self, observer: Observer):
        self.observer = observer

    @abstractmethod
    def notify_function(self, message: any):
        pass


