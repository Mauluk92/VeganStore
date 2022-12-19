from validator.validator import Validator


class NameFormatValidator(Validator):

    """
    Validates names of products: not implemented (not required)
    """

    ERROR_MESSAGE = "Il nome non è formattato correttamente!"

    def __init__(self):
        super().__init__(self.ERROR_MESSAGE)

    def is_valid(self, data: any) -> bool:
        return True
