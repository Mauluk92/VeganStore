from command.enums.command_enum import CommandEnum
from input.input_handler import InputHandler
from input.user_input import UserInput


class UserConsole:

    """
    Handles the request from the user. It contains a dictionary of options, an :class:`InputHandler`
    and command handlers to handle the requests from user
    """

    def __init__(self, condition_on_exit,
                 command_handlers: dict,
                 message_display: str,
                 input_handler: InputHandler,
                 dictionary_options: dict):
        self.condition_on_exit = condition_on_exit
        self.input_handler = input_handler
        self.command_handlers = command_handlers
        self.message_display = message_display
        self.dictionary_options = dictionary_options

    def main_loop(self):
        """
        This is the main loop of the program. Here takes place the handling of requests from user
        """
        print(self.message_display)
        while True:
            user_input = input()
            option = self.dictionary_options.get(user_input, CommandEnum.INVALID_INPUT)
            if user_input == self.condition_on_exit:
                break
            elif option == CommandEnum.HELP:
                print(self.message_display)
            elif option == CommandEnum.INVALID_INPUT:
                print("L'input non è corretto! Premi 5 per aiuto")
            else:
                command = self.input_handler.issue_command(UserInput(str(user_input), option), {})
                self.command_handlers[option].handle_command(command)


