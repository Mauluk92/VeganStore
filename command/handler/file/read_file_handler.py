import json

from command.handler.context_manager.read_context_manager import ReadContextManager
from command.handler.file.file_handler import FileHandler


class ReadFileHandler(FileHandler):
    def __init__(self):
        super().__init__(ReadContextManager("products.json"))

    def handle_file(self, file_obj, data):
        register = json.load(file_obj)
        if not register["products"]:
            print("Non c'è alcun prodotto!")
        else:
            for product in register["products"]:
                print(product["name"], str(product["quantity"]), str(product["sale_price"]))
