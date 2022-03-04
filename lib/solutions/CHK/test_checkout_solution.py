import unittest
from checkout_solution import calculate_item_price


class TestCheckout(unittest.TestCase):
    def test_calculate_item_price(self):
        self.assertAlmostEqual(calculate_item_price("A", 4), 180)
        self.assertAlmostEqual(calculate_item_price("A", 6), 260)
        self.assertAlmostEqual(calculate_item_price("B", 2), 45)
        self.assertAlmostEqual(calculate_item_price("B", 3), 75)
        self.assertAlmostEqual(calculate_item_price("C", 2), 40)
        self.assertAlmostEqual(calculate_item_price("C", 3), 60)
        self.assertAlmostEqual(calculate_item_price("D", 1), 15)
        self.assertAlmostEqual(calculate_item_price("D", 4), 60)


if __name__ == '__main__':
    unittest.main(verbosity=2)





