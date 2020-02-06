#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


# RUNTIME = O(3^n) -- BAD!
# def eating_cookies(n, cache=None):
#     # base case
#     # found path that works
#     if n == 0:
#         return 1
#     # did not find path that works
#     elif n < 0:
#         return 0
#     else:
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n - 3)


# With cache
def eating_cookies(n, cache=None):
    # base case
    # found path that works
    if n == 0:
        return 1
    # did not find path that works
    elif n < 0:
        return 0
    # look in cache
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            # create dict where n is # of ways to eat cookies
            cache = {i: 0 for i in range(n + 1)}

        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n - 3, cache)
        return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
