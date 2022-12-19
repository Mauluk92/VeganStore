import json

from command.user_command import UserCommand
from command.enums.command_enum import CommandEnum
from command.handler.command_handler import CommandHandler
from command.handler.context_manager.check_context_manager import CheckContextManager
from exception.input_exception import InputException
from input.input_handler import InputHandler
from input.user_input import UserInput
from validator.input.user_input import UserInputValidator
from validator.name.name_format import NameFormatValidator
from validator.quantity.quantity_format import QuantityFormatValidator
from validator.selling.selling_format import SellingValidator


class SellHandler(CommandHandler):

    """
    This class is used to perform a selling operation, if possible
    """
    END_LABEL = "VENDUTO: X{} {}"
    SELLING_LABEL = "Registra una vendita: "
    LABELS = {
        "name": "Nome del prodotto: ",
        "quantity": "Quantità: ",
    }

    INPUT_SELL_AGAIN_FORMAT = "^sì$"

    INPUT_SELL_AGAIN_ERROR_MESSAGE = "La risposta deve essere sì oppure no"

    def __init__(self):
        super().__init__(self.LABELS, InputHandler({
            CommandEnum.NAME: NameFormatValidator(),
            CommandEnum.QUANTITY: QuantityFormatValidator(),
            CommandEnum.SELL: SellingValidator(),
            CommandEnum.REGISTER_SALE: UserInputValidator(self.INPUT_SELL_AGAIN_FORMAT,
                                                          self.INPUT_SELL_AGAIN_ERROR_MESSAGE)}))

    def handle_command(self, command: UserCommand):
        """
        Handles the selling operation, by first checking if the inputs are correct.
        If correct, checks if the products exist in the given amount
        """
        print(self.SELLING_LABEL)
        command.data = dict()
        while True:
            try:
                command.data["name"] = self.record_input("name", CommandEnum.NAME)
                command.data["quantity"] = int(self.record_input("quantity", CommandEnum.QUANTITY))
                self.input_handler.check_input(UserInput(command.data, CommandEnum.SELL))
                self.check_product(command)
                break
            except InputException as ex:
                print(ex)
                break
        self.sell_again()
        return True

    def check_product(self, command: UserCommand):
        """
        This function encapsulates the validation logic on file-level. If the product does not exists
        or if the product does not exist with the given quantity, exits with False
        :return:
        """
        with CheckContextManager("products.json") as file:
            register = json.load(file)
            for product in register["products"]:
                if product["name"] == command.data["name"]:
                    product["quantity"] -= command.data["quantity"]
                    if product["quantity"] < 0:
                        return True
                    print(self.END_LABEL.format(command.data["quantity"], product["name"]))
                    file.seek(0)
                    file.truncate(0)
                    command.data["sale_price"] = product["sale_price"]
                    command.data["purchase_price"] = product["purchase_price"]
                    sold = list(register["sold"])
                    sold += [command.data]
                    register["sold"] = sold
                    json.dump(register, file)
                    return False
            return True

    def sell_again(self):
        """
        Handles the secondary loop for another sell, by checking inputs and issuing a REGISTER_SALE command.
        :return:
        """
        while True:
            user_input = input("Vuoi registrare un'altra vendita?\n")
            if user_input == "no":
                break
            try:
                command = self.input_handler.issue_command(UserInput(user_input, CommandEnum.REGISTER_SALE), {})
                self.input_handler.check_input(UserInput(user_input, CommandEnum.REGISTER_SALE))
                self.handle_command(command)
            except InputException:
                pass
