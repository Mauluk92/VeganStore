import re

from validator.validator import Validator


class UserInputValidator(Validator):

    """
    Validates an user input against a regexp
    """

    def __init__(self, valid_inputs="[0-6]", error_message="L'input deve essere compreso tra 1 e 6"):
        super().__init__(error_message)
        self.valid_inputs = valid_inputs

    def is_valid(self, data: str) -> bool:
        return True if re.search(self.valid_inputs, data) else False
