from command.user_command import UserCommand
from exception.input_exception import InputException
from input.user_input import UserInput
from input.observer.input_error_observer import InputErrorObserver
from input.observer.observable import Observable


class InputHandler(Observable):

    """
    InputHandler handles the user input providing validation and sending the appropriate request from
    client to handlers.
    """

    def __init__(self, validators: dict):
        super().__init__(InputErrorObserver())
        self.validators = validators

    def notify_function(self, message: any):
        """
        Each time the handler reports an error, notify its observer
        """
        self.observer.change_state(message)

    def check_input(self, user_input: UserInput):
        """
        Validates input using the appropriate validator
        :param user_input: encapsulates user input from keyboard
        :return: boolean stating if analysis of input succeeded
        """
        validator = self.validators[user_input.category]
        if not validator.is_valid(user_input.input_from_user):
            self.observer.change_state(validator.error_message)
        return True

    def issue_command(self, user_input: UserInput, data):
        """
        Issue a command, which can be used to perform an operation via handlers
        :param user_input: encapsulates user input
        :param data: any data that is linked to the input
        :return: a UserCommand, used to handle the request from the client
        """
        try:
            self.check_input(user_input)
            return UserCommand(user_input.category, data)
        except InputException as ex:
            print(ex)
