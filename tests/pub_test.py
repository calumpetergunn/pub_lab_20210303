import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Dirty Dicks", 100.5)

    def test_pub_has_name(self):
        self.assertEqual("Dirty Dicks", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.5, self.pub.till)

    def test_drink_stock_starts_empty(self):
        self.assertEqual(0, len(self.pub.drink_stock))

    def test_can_add_drink_to_drink_stock(self):
        drink = Drink("Tequilla Sunrise", 4.00, 5)
        self.pub.add_to_stock(drink)
        self.assertEqual(1, len(self.pub.drink_stock))

    def test_drink_in_drink_stock(self):
        drink = Drink("Tequilla Sunrise", 4.00, 5)
        self.pub.add_to_stock(drink)
        self.assertEqual(True, self.pub.check_if_drink_in_stock(drink))

    def test_drink_not_in_drink_stock(self):
        drink = Drink("Tequilla Sunrise", 4.00, 5)
        self.assertEqual(False, self.pub.check_if_drink_in_stock(drink))

    def test_take_customer_money(self):
        drink = Drink("Tequilla Sunrise", 4.00, 5)
        customer = Customer("Bob", 25.55)
        customer.take_customers_money(drink.price)
        self.assertEqual(21.55, customer.wallet)

    def test_can_sell_drink_to_customer(self):
        drink = Drink("Tequilla Sunrise", 4.00, 5)
        customer = Customer("Bob", 25.55)
        customer.age = 22
        self.pub.add_to_stock(drink)
        self.pub.sell_drink_to_customer(customer, drink)
        self.assertEqual(21.55, customer.wallet)
        self.assertEqual(104.5, self.pub.till)

    def test_customer_age(self):
        customer = Customer("Bob", 25.55)
        customer.age = 19
        self.assertEqual(True, self.pub.age_check(customer))

    def test_drunkness_check(self):
        customer = Customer("Bob", 25.55)
        customer.customer_drunkness = 21
        self.assertEqual(True, self.pub.drunkeness_check(customer))
