import json

from command.handler.context_manager.write_context_manager import WriteContextManager
from command.handler.file.file_handler import FileHandler


class AddFileHandler(FileHandler):
    """
    Handles the insertion of a new product on file
    """
    END_LABEL = "AGGIUNTO: X{} {}"

    def __init__(self):
        super().__init__(WriteContextManager("products.json"))

    def handle_file(self, file_obj, data):
        """
        Performs the insertion of a new product on file-level
        """
        data["quantity"] = int(data["quantity"])
        register = json.load(file_obj)
        products = list(register["products"])
        products.append(data)
        file_obj.seek(0)
        file_obj.truncate(0)
        json.dump({'products': products, 'sold': register["sold"]}, file_obj)
        print(self.END_LABEL.format(data["quantity"], data["name"]))
        return True
