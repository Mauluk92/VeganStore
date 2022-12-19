import json
from decimal import Decimal

from command.user_command import UserCommand
from command.handler.command_handler import CommandHandler


class CashHandler(CommandHandler):
    """
    Handler for displaying the profits
    """

    DISPLAY_HEADER = "PROFITTI"
    DISPLAY_INCOME = "Lordi: {}€\nNetti: {}€"

    def handle_command(self, command: UserCommand):
        """
        Handles the display of gross and net profits, formatting the output
        with Decimal class
        :param command: the command given the input handler
        """
        with open("products.json", "r") as file:
            print(self.DISPLAY_HEADER)
            register = json.load(file)
            gross_income = Decimal(0.00)
            net_income = Decimal(0.00)
            for product in register["sold"]:
                gross_income += Decimal(product["sale_price"])
                net_income += Decimal(product["sale_price"]) - Decimal(product["purchase_price"])
            print(self.DISPLAY_INCOME.format(gross_income, net_income, ".2f"))
