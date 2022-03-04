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
    # Dont forget to check for invalid input: return -1
    skus_list = list(skus)
    skus_elem_count = {}
    for elem in skus_list:
        skus_elem_count[elem] = skus_list.count(elem)
    # check items and amount for special offer for each elem
#    for item, amount in skus_elem_count.items():

    # add total of SKUs
    # return SKUs total cost
    return(skus_elem_count)


def calculate_price(item, amount):
    item_price = {
        "A": {
            "price": 50,
            "offer_amount": 3,
            "offer_price": 130
        },
        "B": {
            "price": 30,
            "offer_amount": 2,
            "offer_price": 45
        },
        "C": {
            "price": 20,
            "offer_amount": None,
            "offer_price": None
        },
        "D": {
            "price": 15,
            "offer_amount": None,
            "offer_price": None
        },
    }
    item_price_json = json.dumps(item_price)
    return item_price_json[item]


# print(checkout("AABCA"))
print(calculate_price("A", "4"))



