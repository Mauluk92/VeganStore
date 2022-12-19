import json
from typing import Union

from command.user_command import UserCommand
from command.enums.command_enum import CommandEnum
from command.handler.command_handler import CommandHandler
from command.handler.file.add_file_handler import AddFileHandler
from command.handler.file.check_file_handler import CheckFileHandler
from exception.input_exception import InputException
from input.input_handler import InputHandler
from input.user_input import UserInput
from model.product_properties import ProductPropertiesEnum
from validator.input.user_input import UserInputValidator
from validator.money.money_format import MoneyFormatValidator
from validator.name.name_format import NameFormatValidator
from validator.quantity.quantity_format import QuantityFormatValidator


class AddHandler(CommandHandler):

    """
    Handler for inserting new products (or already existing ones). Has a two file-handler:
    file_handler_check encapsulates the logic to add already existing products.
    file_handler_add encapsulates the logic to add a new product
    """
    ADD_LABEL = "Aggiungi: "

    LABELS = {
        "name": "Nome del prodotto: ",
        "quantity": "Quantità: ",
        "sale_price": "Prezzo di vendita: ",
        "purchase_price": "Prezzo di acquisto: "
    }

    INPUT_ADD_AGAIN_FORMAT = "sì"

    INPUT_ADD_AGAIN_ERROR_MESSAGE = "La risposta deve essere sì oppure no"

    INPUT_VALIDATOR_MAPPING = {ProductPropertiesEnum.NAME: CommandEnum.NAME,
                               ProductPropertiesEnum.QUANTITY: CommandEnum.QUANTITY,
                               ProductPropertiesEnum.SALE_PRICE: CommandEnum.SALE_PRICE,
                               ProductPropertiesEnum.PURCHASE_PRICE: CommandEnum.PURCHASE_PRICE}

    def __init__(self):
        super().__init__(self.LABELS, InputHandler({
            CommandEnum.NAME: NameFormatValidator(),
            CommandEnum.QUANTITY: QuantityFormatValidator(),
            CommandEnum.PURCHASE_PRICE: MoneyFormatValidator(),
            CommandEnum.SALE_PRICE: MoneyFormatValidator(),
            CommandEnum.ADD: UserInputValidator(
                self.INPUT_ADD_AGAIN_FORMAT,
                self.INPUT_ADD_AGAIN_ERROR_MESSAGE),
            CommandEnum.INVALID_INPUT: UserInputValidator(
                self.INPUT_ADD_AGAIN_FORMAT,
                self.INPUT_ADD_AGAIN_ERROR_MESSAGE)}))
        self.file_handler_check = CheckFileHandler()
        self.file_handler_add = AddFileHandler()

    def handle_command(self, command: UserCommand):
        """
        Handles the adding of a product. For each property, user input is required.
        If the product already exists, the function terminates and invokes sell_again() skipping
        the other passages
        :param command: the command given by the input handler
        :return: True if the operation is performed
        """
        print(self.ADD_LABEL)
        while True:
            try:
                for product_property in [(prop, prop.value) for prop in ProductPropertiesEnum]:
                    command.data[product_property[1]] = input(self.labels[product_property[1]])
                    self.input_handler.check_input(UserInput(command.data[product_property[1]],
                                                             self.INPUT_VALIDATOR_MAPPING[product_property[0]]))
                    if (product_property[0] == ProductPropertiesEnum.QUANTITY and
                            self.file_handler_check.handle_command(command)):
                        self.add_again()
                        return True
                self.file_handler_add.handle_command(command)
                self.add_again()
                break
            except InputException as ex:
                print(ex)

    def add_again(self):
        """
        Handles the secondary loop for adding other products, by issuing an ADD command,
        and checking the inputs
        """
        while True:
            try:
                user_input = input("Vuoi aggiungere un altro prodotto?\n")
                if user_input == "no":
                    break
                self.input_handler.check_input(UserInput(user_input, CommandEnum.ADD))
                command = self.input_handler.issue_command(UserInput(user_input, CommandEnum.ADD), {})
                self.handle_command(command)
            except InputException as ex:
                print(ex)
