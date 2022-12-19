from enum import Enum


class CommandEnum(Enum):
    """
    Encapsulates all the available commands the user or a handler can issue
    """
    INVALID_INPUT = 0
    ADD = 1
    DISPLAY = 2
    SELL = 3
    REGISTER_SALE = 4
    VIEW_INCOME = 5
    NAME = 6
    QUANTITY = 7
    SALE_PRICE = 8
    PURCHASE_PRICE = 9
    HELP = 10
    CHECK_PRODUCTS = 11


