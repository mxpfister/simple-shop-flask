class Product:
    ID = None
    category = None
    name = None
    description = None
    price_excl_tax = None
    price_incl_tax = None
    stock = None

    def __init__(self, ID, category, name, description, price_excl_tax, price_incl_tax, stock):
        """
        Constructor
        :param ID: Id of an product
        :param category: category of an product
        :param name: name of an product
        :param description: description of an product
        :param price_excl_tax: gross price of an product
        :param price_incl_tax: net price of an product
        :param stock: stock of an product
        """
        self.ID = ID
        self.category = category
        self.name = name
        self.description = description
        self.price_excl_tax = price_excl_tax
        self.price_incl_tax = price_incl_tax
        self.stock = stock
