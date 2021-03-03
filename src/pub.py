class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drink_stock = []

    # Needs extra logic to protect against multiple instances
    def add_to_stock(self, drink_name):
            self.drink_stock.append(drink_name)

    # returns either true or false (for testing)
    def check_if_drink_in_stock(self, drink_name):
        return drink_name in self.drink_stock

    # remove drink from stock
    def remove_from_stock(self, drink):
        self.drink_stock.remove(drink)

    # total beer sales in units (potential future function)
    # def increase_beers_sold()

    # increase till total
    def increase_till_total(self, drink_price):
        self.till += drink_price
    
    # take drink from stock, take customer money and add to till
    def sell_drink_to_customer(self, customer, drink):
        if self.check_if_drink_in_stock(drink) == True:
            customer.take_customers_money(drink.price)
            self.increase_till_total(drink.price)
            self.remove_from_stock(drink)
   