from command.handler.context_manager.product_context_manager import ProductContextManager


class CheckContextManager(ProductContextManager):
    """
    Check context manager. Used for checking if products already exists.
    """
    def __init__(self, file_path: str):
        super().__init__(file_path)

    def __enter__(self):
        self.file_obj = open(self.file_path, mode="r+")
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
