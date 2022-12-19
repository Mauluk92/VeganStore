from abc import abstractmethod


class ProductContextManager:
    """
    Super class of all context managers in this package
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
