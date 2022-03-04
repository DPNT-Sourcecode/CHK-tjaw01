#!/usr/bin/env python3
import json

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
    skus_list = list(skus)
    skus_elem_count = {}
    for elem in skus_list:
        skus_elem_count[elem] = skus_list.count(elem)
    # check items and amount for special offer for each elem
    for item, amount in skus_elem_count.items():

    # add total of SKUs
    # return SKUs total cost
    return(skus_elem_count)

# Our price table and offers:
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+
def calculate_price(item, amount):
    item_price = {
        "A" = ,
        "B" = 30,
        "C" = 20,
        "D" = 15,
    }

    if item == "A":
    # need to include a division of the amount to see how many items are offers or not.
    if item == "B":



print(checkout("AABCA"))

