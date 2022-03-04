#!/usr/bin/env python3
import json

# We are going to sell a new item E.
# Normally E costs 40, but if you buy 2 of Es you will get B free. How cool is
# that ? Multi-priced items also seemed to work well so we should have more of
# these.

# Our price table and offers:
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+

# Notes:
#  - The policy of the supermarket is to always favor the customer when
#  applying special offers.
#  - All the offers are well balanced so that they can be safely combined.
#  - For any illegal input return -1

# In order to complete the round you need to implement the following method:
#      checkout(String) -> Integer

# Where:
#  - param[0] = a String containing the SKUs of all the products in the basket
#  - @return = an Integer representing the total checkout value of the items


# noinspection PyUnusedLocal
# skus = unicode string
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+
items = {
    "A": {
        "price": 50,
        "offers": [
            {
                "required_item": "A",
                "required_item_amount": 3,
                "offer_item": "A",
                "offer_price": 130
            },
            {
                "required_item": "A",
                "required_item_amount": 5,
                "offer_item": "A",
                "offer_price": 200
            }
        ]
    },
    "B": {
        "price": 30,
        "offers": [
            {
                "required_item": "B",
                "required_item_amount": 2,
                "offer_item": "B",
                "offer_price": 45
            }
        ]
    },
    "C": {
        "price": 20,
        "offers": None
    },
    "D": {
        "price": 15,
        "offers": None
    },
    "E": {
        "price": 40,
        "offers": [
            {
                "required_item": "E",
                "required_item_amount": 2,
                "offer_item": "B",
                "offer_price": 0
            }
        ]
    },
}


def checkout(skus):
    basket = list(skus)
#    basket_items = {}
    for item in basket:
        if item not in items[item]:
            return -1
#        skus_elem_count[elem] = skus_list.count(elem)
#    total_cost_list = []
#    for item, amount in skus_elem_count.items():
#        total_cost_list.append(calculate_item_price(item, amount))
#    return(int(sum(total_cost_list)))
    return 0


def calculate_item_price(item, amount):
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
        total_item_price = int(price) * int(amount)
    return int(total_item_price)


print(checkout("A"))
