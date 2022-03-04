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
                "offer_id": 1,
                "required_item_amount": 3,
                "offer_item": "A",
                "offer_price": 130
            },
            {
                "offer_id": 2,
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
                "offer_id": 3,
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
                "offer_id": 4,
                "required_item_amount": 2,
                "offer_item": "B",
                "offer_price": 0
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
    print(calculate_items_price(basket_items_count))
    return 0


def calculate_items_price(basket_items_count):
    total_basket_cost = {}
    for item, amount in basket_items_count.items():
        price = items[item]["price"]
        total_basket_cost[item] = (int(price) *
                                   int(amount))
    return(total_basket_cost)


def apply_offers(basket_items_count, total_basket_costs):
    for item, amount in basket_items_count.items():
        offer_prices = {}
        offers = items[item]["offers"]
        if offers is not None:
            for offer in offers:
                price = items[item]["price"]
                offer_id = offer["offer_id"]
                required_item_amount = offer["required_item_amount"]
                offer_price = offer["offer_price"]
                number_of_offers = int(amount) // int(required_item_amount)
                remained_items = int(amount) % int(required_item_amount)
                total_item_price = ((number_of_offers * offer_price) +
                                    (remained_items * price))
                offer_prices[offer_id] = total_item_price
                print(offer_prices)
        # calcute the price of each key value
        # for free items compare to see if offer item = current item


    # price = item_price_json[item]["price"]
    # required_item = item_price_json[item]["offer_amount"]
    # required_item_amount = item_price_json[item]["offer_price"]
    # offer_item =
    # offer_price =
    #
    # if offer_amount is not None:
    #     number_of_offers = int(amount) // int(offer_amount)
    #     remained_items = int(amount) % int(offer_amount)
    #     total_item_price = ((number_of_offers * offer_price) +
    #                         (remained_items * price))
    # else:
    #     total_item_price = int(price) * int(amount)
    # return int(total_item_price)


print(checkout("CCDDDAABC"))


