from abc import abstractmethod


class Observer:

    """
    Each observer has a change state function which defines the behavior on notify by an :class:`Observable`
    """

    @abstractmethod
    def change_state(self, state: any):
        pass
