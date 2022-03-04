#!/usr/bin/env python3

# Our price table and offers:
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+
# Notes:
#  - For any illegal input return -1
#
# In order to complete the round you need to implement the following method:
#      checkout(String) -> Integer
# Where:
#  - param[0] = a String containing the SKUs of all the products in the basket
#  - @return = an Integer representing the total checkout value of the items


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # convert string input to list
    skus_list = list(skus)
    return skus_list
    # check items and amount for special offer for each elem
    # add total of SKUs
    # return SKUs total cost


print(checkout("AABCA"))

