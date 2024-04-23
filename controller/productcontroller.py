from model.product import Product


class ProductController:
    all_products = []
    user_cart = []

    def create_product(self, ID, category, name, description, price_excl_tax, price_incl_tax, stock):
        """
        creates an object product from the input and appends it to all_products
        :param ID: Id of an product
        :param category: category of an product
        :param name: name of an product
        :param description: description of an product
        :param price_excl_tax: gross price of an product
        :param price_incl_tax: net price of an product
        :param stock: stock of an product
        """
        new_product = Product(ID=ID, category=category, name=name, description=description,
                              price_excl_tax=price_excl_tax, price_incl_tax=price_incl_tax, stock=stock)
        self.all_products.append(new_product)

    def initial_products(self):
        """
        creates the products when the view has been started
        """
        self.create_product(ID=len(self.all_products) + 1000, category="Trouser", name="Sellateen",
                            description="The newest, hottest style in trousers. Trendy, fashion-forward and perfect for your lifestyle. You`ll never want to wear anything else!",
                            price_excl_tax=50, price_incl_tax=59.5, stock=100)
        self.create_product(ID=len(self.all_products) + 1000, category="Trouser", name="Babo",
                            description="The Trouser is a suit that has been designed to fit any body type and still look good. Made with a high-quality stretch fabric, the Trouser can be tailored to your exact measurements and still look like a million bucks.",
                            price_excl_tax=500, price_incl_tax=595, stock=10)
        self.create_product(ID=len(self.all_products) + 1000, category="Pullover", name="Piffen",
                            description="This pullover is the perfect addition to your winter wardrobe. The knit fabric is soft and will keep you warm and cozy, while the design keep you stylish.",
                            price_excl_tax=40, price_incl_tax=47.60, stock=50)
        self.create_product(ID=len(self.all_products) + 1000, category="Pullover", name="Chique",
                            description="This sweater is perfect for the office or an evening out. The material is soft and stretchy.",
                            price_excl_tax=30, price_incl_tax=35.70, stock=50)
        self.create_product(ID=len(self.all_products) + 1000, category="T-Shirts", name="Snowman",
                            description="The perfect t-shirt for the holidays! A winter white t-shirt with a snowman wearing a Santa hat.",
                            price_excl_tax=25, price_incl_tax=29.75, stock=30)
        self.create_product(ID=len(self.all_products) + 1000, category="T-Shirts", name="Paramour",
                            description="This t-shirt is perfect for any fan of the brand. The soft, durable fabric is easy to wash and features the brand's logo on the front.",
                            price_excl_tax=60, price_incl_tax=71.40, stock=40)
        self.create_product(ID=len(self.all_products) + 1000, category="Shorts", name="Petal",
                            description="Whether you're going to the gym, going for a run, or going for a hike, these Shorts will keep you feeling cool and comfortable.",
                            price_excl_tax=50, price_incl_tax=59.5, stock=60)
        self.create_product(ID=len(self.all_products) + 1000, category="Hats", name="Suave",
                            description="This hat is perfect for keeping the sun out of your eyes. It's also a great hat for keeping your head cool and your hair off your face.",
                            price_excl_tax=20, price_incl_tax=23.80, stock=100)
        self.create_product(ID=len(self.all_products) + 1000, category="Jackets", name="Patron",
                            description="This denim jacket has a bold and edgy look. It has a cropped fit and can be worn with a simple tee and jeans for a casual daytime look or with a tank top and jeans for a night out.",
                            price_excl_tax=80, price_incl_tax=95.20, stock=100)
        self.create_product(ID=len(self.all_products) + 1000, category="Jackets", name="Palace",
                            description="This jacket is a versatile piece that can be worn with any outfit. It is made of a durable fabric that is perfect for all seasons. It is a classic, timeless piece that will never go out of style.",
                            price_excl_tax=300, price_incl_tax=357, stock=10)

    def find_product(self, product_id):
        """
        finds a product from all_product
        :param product_id: the possible product id
        :return: returns the found product if there is an product with this id
        """
        for product in self.all_products:
            if product.ID == int(product_id):
                return product

    def add_to_cart(self, product_id, quantity):
        """
        checks if a product exists to the given ID and the given stock
        :param product_id: id of the product to be added to the cart
        :param quantity: how often the product should be added to the cart
        :return If everything is correct the function returns True
        """
        product = self.find_product(int(product_id))
        if product is not None:
            if product.stock >= int(quantity):
                for x in range(0, int(quantity)):
                    self.user_cart.append(product)
                return True

    def cart_total(self):
        """
        sums up the gross price of all product objects in the user cart
        :return: the total of the cart
        """
        cart_total = 0
        for p in self.user_cart:
            cart_total += p.price_incl_tax
        return cart_total

    def adapt_stock(self):
        """
        adjusts the stock of products that were in the cart after checkout
        """
        for product in self.all_products:
            if product in self.user_cart:
                quantity = self.user_cart.count(product)
                product.stock -= quantity
