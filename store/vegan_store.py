from console.user_console import UserConsole
from command.enums.command_enum import CommandEnum
from command.handler.add_handler import AddHandler
from command.handler.cash_handler import CashHandler
from command.handler.display_handler import DisplayHandler
from command.handler.sell_handler import SellHandler
from input.input_handler import InputHandler
from validator.input.user_input import UserInputValidator


class VeganStore:
    """
    The store of vegan products: requires an :class:`InputHandler` to handle the validation of inputs,
    with an :class:`UserConsole` instance which is responsible for the user-interaction.
    """


    MAIN_MENU = """
                1 - Aggiungi un prodotto
                2 - Elenca i prodotti
                3 - Registra vendita
                4 - Visualizza profitti
                5 - Aiuto
                6 - Esci dal programma
                """

    def __init__(self):
        self.input_handler = InputHandler({CommandEnum.INVALID_INPUT: UserInputValidator(),
                                           CommandEnum.DISPLAY: UserInputValidator(),
                                           CommandEnum.ADD: UserInputValidator(),
                                           CommandEnum.REGISTER_SALE: UserInputValidator(),
                                           CommandEnum.VIEW_INCOME: UserInputValidator(),
                                           CommandEnum.HELP: UserInputValidator()})
        self.console = UserConsole("6", {
            CommandEnum.ADD: AddHandler(),
            CommandEnum.DISPLAY: DisplayHandler(),
            CommandEnum.REGISTER_SALE: SellHandler(),
            CommandEnum.VIEW_INCOME: CashHandler()
        },
                                   self.MAIN_MENU, self.input_handler,
                                   {"1": CommandEnum.ADD,
                                    "2": CommandEnum.DISPLAY,
                                    "3": CommandEnum.REGISTER_SALE,
                                    "4": CommandEnum.VIEW_INCOME,
                                    "5": CommandEnum.HELP})

    def start(self):
        self.console.main_loop()
