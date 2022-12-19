from abc import abstractmethod

from command.user_command import UserCommand
from command.enums.command_enum import CommandEnum
from input.user_input import UserInput


class CommandHandler:
    """
    Super class of all handlers, used to define common logic between them
    """
    def __init__(self, labels=None, input_handler=None):
        self.labels = labels
        self.input_handler = input_handler

    @abstractmethod
    def handle_command(self, command: UserCommand):
        """
        Every handler as an handle_command method to handle a command given by an input handler
        """
        pass

    def record_input(self, label: str, category: CommandEnum):
        input_from_user = input(self.labels[label])
        self.input_handler.check_input(UserInput(input_from_user, category))
        return input_from_user
