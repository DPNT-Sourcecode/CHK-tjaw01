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
        "value_offers": [
            {
                "required_item_amount": 3,
                "offer_item": "A",
                "offer_price": 130
            },
            {
                "required_item_amount": 5,
                "offer_item": "A",
                "offer_price": 200
            }
        ],
        "free_offers": None
    },
    "B": {
        "price": 30,
        "value_offers": [
            {
                "required_item_amount": 2,
                "offer_item": "B",
                "offer_price": 45
            }
        ],
        "free_offers": None
    },
    "C": {
        "price": 20,
        "value_offers": None,
        "free_offers": None
    },
    "D": {
        "price": 15,
        "value_offers": None,
        "free_offers": None
    },
    "E": {
        "price": 40,
        "value_offers": None,
        "free_offers": [
            {
                "required_item_amount": 2,
                "offer_item": "B",
                "offer_price": None
            }
        ]
    }
}


def checkout(skus):
    basket = list(skus)
    basket_items_count = {}
    for item in basket:
        if item not in items:
            return -1
        basket_items_count[item] = basket.count(item)
    print(basket_items_count)
    basket_items_count = handle_for_free_offers(basket_items_count)
    print(basket_items_count)
    total_basket_cost = calculate_items_price(basket_items_count)
    values = total_basket_cost.values()
    total = sum(values)
    return total


def calculate_items_price(basket_items_count):
    total_basket_cost = {}
    for item, amount in basket_items_count.items():
        total_basket_cost[item] = handle_for_value_offers(item, amount)
    return total_basket_cost


def handle_for_value_offers(item, amount):
    offers = items[item]["offers"]
    offer_prices = []
    total = 0
    if offers:
        for offer in offers:
            offer_item = offer["offer_item"]
            price = items[item]["price"]
            required_item_amount = offer["required_item_amount"]
            offer_price = offer["offer_price"]
            number_of_offers = int(amount) // int(required_item_amount)
            remained_items = int(amount) % int(required_item_amount)
            total_item_price = ((number_of_offers * offer_price) +
                                (remained_items * price))
            offer_prices.append(total_item_price)
            total = min(offer_prices)
    else:
        price = items[item]["price"]
        total = int(price) * int(amount)
    return total


def handle_for_free_offers(basket_items_count):
    for item, amount in basket_items_count.items():
        offers = items[item]["offers"]
        if offers:
            for offer in offers:
                offer_price = offer["offer_price"]
                offer_item = offer["offer_item"]
                required_item_amount = offer["required_item_amount"]
                if not offer_price and required_item_amount <= amount:
                    number_of_offers = int(amount) // int(required_item_amount)
                    basket_items_count[offer_item] = (basket_items_count[offer_item] -
                                                      number_of_offers)
    return basket_items_count


print(checkout("CCABE"))




