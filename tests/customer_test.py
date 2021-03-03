import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Malcolm", 10.45)
    
    def test_customer_exists(self):
        self.assertEqual("Malcolm", self.customer.name)

    def test_customer_wallet(self):
        self.assertEqual(10.45, self.customer.wallet)

    def test_can_afford_drink(self):
        drink = Drink("Tequilla Sunrise", 4)
        drink_price = drink.price
        self.assertEqual(True, self.customer.can_afford_drink(drink_price))