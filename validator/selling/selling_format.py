import json

from command.handler.context_manager.check_context_manager import CheckContextManager
from validator.validator import Validator


class SellingValidator(Validator):

    """
    Check if product sold exists and if it has the required quantity
    """
    ERROR_MESSAGE = """
    Il prodotto non è disponibile in quella quantità!
    """

    def __init__(self):
        super().__init__(self.ERROR_MESSAGE)

    def is_valid(self, data) -> bool:
        with CheckContextManager("products.json") as file:
            register = json.load(file)
            for product in register["products"]:
                if product["name"] == data["name"] and product["quantity"] >= data["quantity"]:
                    return True
        return False
