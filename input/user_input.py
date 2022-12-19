from command.enums.command_enum import CommandEnum


class UserInput:
    """
    Encapsulates input from user with a :class:`CommandEnum`, responsible for
    determining the type of operation to perform or handle (ADD, DISPLAY, SELL...)
    """
    def __init__(self, input_from_user: any, category: CommandEnum):
        self.input_from_user = input_from_user
        self.category = category
