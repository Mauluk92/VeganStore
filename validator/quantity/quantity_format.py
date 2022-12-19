import re

from validator.validator import Validator


class QuantityFormatValidator(Validator):

    """
    Each quantity should be a positive number
    """
    QUANTITY_FORMAT = "\\d+"
    ERROR_MESSAGE = """
    Il formato della quantità del prodotto non è corretto!
    Deve essere un numero intero maggiore o uguale a zero!
    """

    def __init__(self):
        super().__init__(self.ERROR_MESSAGE)

    def is_valid(self, data) -> bool:
        return True if re.search(self.QUANTITY_FORMAT, data) else False
