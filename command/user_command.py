from command.enums.command_enum import CommandEnum


class UserCommand:
    """
    Used to define the operation to be performed by a handler
    """
    def __init__(self, user_command_category: CommandEnum, data: dict):
        self.user_command_category = user_command_category
        self.data = data
