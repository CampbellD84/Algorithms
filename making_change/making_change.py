#!/usr/bin/python

import sys

# denominations = [1, 5, 10, 25, 50]


def making_change(amount, denominations):
    # Base Case 1
    if amount == 0:
        return 1
    # Base Case 2
    elif amount < 0 or not denominations:
        return 0
    else:
        coin = denominations[-1]
        return sum(making_change(amt, denominations[:-1]) for amt in range(amount, -1, -coin))


if __name__ == "__main__":
        # Test our your implementation from the command line
        # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
