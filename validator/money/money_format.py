import re

from validator.validator import Validator


class MoneyFormatValidator(Validator):

    """
    Validates currency against regex
    """

    MONEY_FORMAT = "\\d+\\.\\d{2}"
    ERROR_MESSAGE = """
    Il formato della valuta non è corretto!
    Deve essere un numero seguito da due cifre dopo la virgola!
    """

    def __init__(self):
        super().__init__(self.ERROR_MESSAGE)

    def is_valid(self, data: any) -> bool:
        return True if re.search(self.MONEY_FORMAT, data) else False
