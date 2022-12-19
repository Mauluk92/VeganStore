import json

from command.handler.context_manager.check_context_manager import CheckContextManager
from command.handler.file.file_handler import FileHandler


class CheckFileHandler(FileHandler):
    """
    This file-handler checks wheter the product exist, it is used by the AddHandler
    """
    END_LABEL = "AGGIUNTO: X{} {}"

    def __init__(self):
        super().__init__(CheckContextManager("products.json"))

    def handle_file(self, file_obj, data):
        """
        Perform writing on file, given the already existing product.
        Returns False otherwise
        """
        register = json.load(file_obj)
        data["quantity"] = int(data["quantity"])
        for product in register["products"]:
            if product["name"] == data["name"]:
                product["quantity"] += data["quantity"]
                print(self.END_LABEL.format(data["quantity"], product["name"]))
                file_obj.seek(0)
                file_obj.truncate(0)
                json.dump(register, file_obj)
                return True
        return False
