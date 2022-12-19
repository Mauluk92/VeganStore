class InputException(Exception):
    """
    Any input error raises an input exception
    """
    def __init__(self, message):
        super().__init__(message)
