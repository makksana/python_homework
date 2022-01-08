print('Task 3', end='\n\n')
# Product Store

# Write a class Product that has three attributes:

# type
# name
# price
# Then create a class ProductStore,
# which will have some Products and
# will operate with all products in the store.
# All methods, in case they can’t perform its action,
# should raise ValueError with appropriate error information.

# Tips: Use aggregation/composition concepts
# while implementing the ProductStore class.
# You can also implement additional classes
# to operate on a certain type of product, etc.

# Also, the ProductStore class must have the following methods:

# add(product, amount) - adds a specified quantity
# of a single product with a predefined price premium
# for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds
# a discount for all products specified by input identifiers
# (type or name). The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount
# of products from the store if available,
# in other case raises an error.
# It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about
# all available products in the store.
# get_product_info(product_name) - returns a tuple
# with product name and amount of items in the store.


class Product:

    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.type}, {self.name}, ${self.price}'


class ProductInShop:

    def __init__(self, prod: Product, amount, extr_charge=0):
        self.prod = prod
        self.amount = amount
        self.price = prod.price + (prod.price * extr_charge/100)


class ProductStore:
    Extra_Charge = 30

    def __init__(self, extra_charge=30):
        self.Extra_Charge = extra_charge
        self.products: list[ProductInShop] = []
        self.income = 0

    def get_all_products(self):
        products = []
        for product_in_shop in self.products:
            products.append(
                {
                    'type': product_in_shop.prod.type,
                    'name': product_in_shop.prod.name,
                    'price': product_in_shop.price,
                    'amount': product_in_shop.amount,
                }
            )
        return products

    def get_product_info(self, product_name):
        for product_in_shop in self.products:
            if product_in_shop.prod.name == product_name:
                return product_in_shop.prod.name, product_in_shop.amount

    def add(self, product, amount):
        if amount < 0:
            raise ValueError('Amount cannot be negative')
        for product_in_shop in self.products:
            if product_in_shop.prod == product:
                product_in_shop.amount += amount
                break
        else:
            product_in_shop = ProductInShop(product, amount, self.Extra_Charge)
            self.products.append(product_in_shop)

    def get_income(self):
        return round(self.income, 2)

    def set_discount(self, identifier, percent):
        for product_in_shop in self.products:
            if product_in_shop.prod.name == identifier or product_in_shop.prod.type == identifier:
                discount = product_in_shop.price - product_in_shop.price*percent/100
                if discount >= product_in_shop.prod.price:
                    product_in_shop.price = discount
                else:
                    raise ValueError('Discount is too big')

    def sell_product(self, product_name, amount):
        for product_in_shop in self.products:
            if product_in_shop.prod.name == product_name:
                if product_in_shop.amount >= amount:
                    product_in_shop.amount -= amount
                    self.income += (product_in_shop.price -
                                    product_in_shop.prod.price)*amount
                else:
                    raise ValueError(
                        f'Not enough {product_in_shop.prod.name} in shop')


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
