from enum import Enum


class ProductPropertiesEnum(Enum):
    """
    Those are the properties of a product sold
    """
    NAME = "name"
    QUANTITY = "quantity"
    SALE_PRICE = "sale_price"
    PURCHASE_PRICE = "purchase_price"
