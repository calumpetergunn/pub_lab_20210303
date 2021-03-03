import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Kidney Killer", 3.5)