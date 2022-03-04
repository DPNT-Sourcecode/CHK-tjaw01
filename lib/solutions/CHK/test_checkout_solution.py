import unittest
from checkout_solution import *


class TestCheckout(unittest.TestCase):
    def test_calculate_item_price(self):
        self.assertAlmostEqual(checkout_solution.calculate_item_price("A", 4), 180)

