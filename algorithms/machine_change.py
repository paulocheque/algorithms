from collections import OrderedDict
import operator

def calculate_change(input_value_in_cents, total_price_in_cents):
    """
    Unit price <= $1
    Available coins: quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent).
    Return fewest number of coins of the change
    """
    available_coins = dict(quarters=25, dimes=10, nickels=5, pennies=1)
    rest = input_value_in_cents - total_price_in_cents
    change = {}
    for name, value in OrderedDict(sorted(available_coins.items(), key=lambda t: t[1], reverse=True)).items():
        change[name] = rest // value
        rest = rest % value
    return change

import unittest
class Tests(unittest.TestCase):
    def test(self):
        self.assertEquals(dict(quarters=0, dimes=0, nickels=0, pennies=0), calculate_change(100, 100))
        self.assertEquals(dict(quarters=0, dimes=0, nickels=0, pennies=1), calculate_change(100, 99))
        self.assertEquals(dict(quarters=0, dimes=0, nickels=1, pennies=0), calculate_change(100, 95))
        self.assertEquals(dict(quarters=0, dimes=0, nickels=1, pennies=1), calculate_change(100, 94))
        self.assertEquals(dict(quarters=0, dimes=0, nickels=1, pennies=4), calculate_change(100, 91))
        self.assertEquals(dict(quarters=0, dimes=1, nickels=0, pennies=0), calculate_change(100, 90))
        self.assertEquals(dict(quarters=0, dimes=1, nickels=0, pennies=1), calculate_change(100, 89))
        self.assertEquals(dict(quarters=0, dimes=2, nickels=0, pennies=4), calculate_change(100, 76))
        self.assertEquals(dict(quarters=1, dimes=0, nickels=0, pennies=0), calculate_change(100, 75))
        self.assertEquals(dict(quarters=1, dimes=0, nickels=0, pennies=1), calculate_change(100, 74))
        self.assertEquals(dict(quarters=3, dimes=1, nickels=0, pennies=4), calculate_change(100, 11))
        self.assertEquals(dict(quarters=3, dimes=1, nickels=1, pennies=1), calculate_change(100, 9))

if __name__ == '__main__':
    unittest.main()
