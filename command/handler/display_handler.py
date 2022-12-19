import json
from json import JSONDecodeError

from command.user_command import UserCommand
from command.handler.command_handler import CommandHandler
from command.handler.file.read_file_handler import ReadFileHandler


class DisplayHandler(CommandHandler):
    """
    Handler for displaying products (if any). Has a file handler which encapsulates the database-logic
    """

    DISPLAY_HEADER = "PRODOTTO QUANTITA' PREZZO"

    def __init__(self):
        super().__init__()
        self.file_handler = ReadFileHandler()

    def handle_command(self, command: UserCommand):
        """
        Invokes the appropriate file-handler to perform the display of products
        """
        try:
            self.file_handler.handle_command(command)
        except JSONDecodeError:
            print("Sembra che il file sia vuoto o corrotto")

