import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Kidney Killer", 3.5, 8)

    def test_drink_exists(self):
        self.assertEqual("Kidney Killer", self.drink.name, self.drink.alcohol_level)

    def test_drink_has_price(self):
        self.assertEqual(3.5, self.drink.price)