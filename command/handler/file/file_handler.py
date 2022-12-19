from abc import abstractmethod

from command.user_command import UserCommand
from command.handler.command_handler import CommandHandler
from exception.input_exception import InputException


class FileHandler(CommandHandler):

    """
    This is a super class of all file-handlers, which encapsulates database-like logic.
    """
    def __init__(self, context_manager, input_handler=None):
        super().__init__(input_handler)
        self.context_manager = context_manager

    def handle_command(self, command: UserCommand):
        """
        Handles file the given initialized context-manager and then handles it
        """
        try:
            with self.context_manager as file:
                self.handle_file(file, command.data)
                return True
        except InputException as ex:
            print(ex)
            return False

    @abstractmethod
    def handle_file(self, file_obj, data):
        """
        Define the current operation on file
        :param file_obj: the file to operate on
        :param data: the data given by user input
        """
        pass
