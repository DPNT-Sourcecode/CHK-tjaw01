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


def calculate_item_price(item, amount):
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
    item_price_json = json.loads(json.dumps(item_price))
    price = item_price_json[item]["price"]
    offer_amount = item_price_json[item]["offer_amount"]
    offer_price = item_price_json[item]["offer_price"]
    if offer_amount is not None:
        number_of_offers = int(amount) // int(offer_amount)
        remained_items = int(amount) % int(offer_amount)
        total_item_price = ((number_of_offers * offer_price) +
                            (remained_items * price))
    else:
        total_item_price = price * amount
    return total_item_price


# print(checkout("AABCA"))
print(calculate_item_price("A", "4"))

