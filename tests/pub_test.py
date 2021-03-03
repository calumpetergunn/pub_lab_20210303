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
        drink = Drink("Tequilla Sunrise", 4.00)
        self.pub.add_to_stock(drink)
        self.assertEqual(1, len(self.pub.drink_stock))

    def test_drink_in_drink_stock(self):
        drink = Drink("Tequilla Sunrise", 4.00)
        self.pub.add_to_stock(drink)
        self.assertEqual(True, self.pub.check_if_drink_in_stock(drink))

    def test_drink_not_in_drink_stock(self):
        drink = Drink("Tequilla Sunrise", 4.00)
        self.assertEqual(False, self.pub.check_if_drink_in_stock(drink))

    def test_take_customer_money(self):
        drink = Drink("Tequilla Sunrise", 4.00)
        customer = Customer("Bob", 25.55)
        customer.take_customers_money(drink.price)
        self.assertEqual(21.55, customer.wallet)

    def test_can_sell_drink_to_customer(self):
        drink = Drink("Tequilla Sunrise", 4.00)
        customer = Customer("Bob", 25.55)
        self.pub.add_to_stock(drink)
        self.pub.sell_drink_to_customer(customer, drink)
        self.assertEqual(21.55, customer.wallet)
        # self.assertEqual(104.5, self.pub.till)

    # def test_can_sell_pet_to_customer(self):
    #     customer = Customer("Jack Jarvis", 1000)
    #     self.pet_shop.sell_pet_to_customer("Sir Percy", customer)
    #     self.assertEqual(500, customer.cash)
    #     self.assertEqual(1500, self.pet_shop.total_cash)
    #     self.assertEqual(1, self.pet_shop.pets_sold)
    #     self.assertEqual(1, self.pet_shop.stock_count())
    #     self.assertEqual(1, customer.pet_count())