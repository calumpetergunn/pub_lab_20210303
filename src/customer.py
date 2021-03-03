class Customer:


    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.age = 0
        self.drunkenness = 0
        # self.alcohol_level_customer = alcohol_level_customer

    # check if customer can afford drink
    def can_afford_drink(self, drink_price):
        return self.wallet >= drink_price

    # take money from customer wallet
    def take_customers_money(self, drink_cost):
        self.wallet -= drink_cost

    def customer_drunkness(self, drink):
        current_drunkness = self.drunkenness + drink
        return current_drunkness
        
