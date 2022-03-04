#!/usr/bin/env python3
#from solutions.SUM import sum_solution

def compute(x, y):
    if 0 <= x <= 100 and 0 <= y <= 100:
        result = x + y
        return result
    else:
        pass


class TestSum():
    def test_sum(self):
        # assert sum_solution.compute(1, 2) == 3
        assert compute(1, 2) == 3
