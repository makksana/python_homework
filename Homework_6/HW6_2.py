print('Task 2', end='\n\n')

# Input data:

# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# Create a function which takes as input 
# two dicts with structure mentioned above, 
# then computes and returns the total price of stock.

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def total_price_of_stock(stock, prices):
    total_price = 0
    for key, value in stock.items():
        price = prices[key]
        if value != 0 and price != 0:
            total_price += value * price
            # print(f'Product {key}, stock {value}, price {price}')
    return total_price

print(total_price_of_stock(stock, prices))