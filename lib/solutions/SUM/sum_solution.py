#!/usr/bin/env python3
# noinspection PyShadowingBuiltins,PyUnusedLocal

def compute(x, y):
    if 0 <= x <= 100 and 0 <= y <= 100:
        result = x + y
        return result
    else:
        pass


print(compute(1, 10))

