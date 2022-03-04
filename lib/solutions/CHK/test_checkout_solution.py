import unittest
from checkout_solution import calculate_item_price


class TestCheckout(unittest.TestCase):
    def test_calculate_item_price(self):
        self.assertAlmostEqual(calculate_item_price("A", 4), 180)


