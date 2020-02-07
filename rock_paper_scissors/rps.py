#!/usr/bin/python

import sys

# create a helper function


def helper_funct(old_res, games_amt, total_res):
    # Base Case
    if games_amt == 0:
        # append old result to total result of permutations
        total_res.append(old_res)
        return old_res
    # recursive calls for rock, paper and scissors
    helper_funct(old_res + ['rock'], games_amt-1, total_res)
    helper_funct(old_res + ['paper'], games_amt-1, total_res)
    helper_funct(old_res + ['scissors'], games_amt-1, total_res)


def rock_paper_scissors(n):
    # create empty list
    result = []
    helper_funct([], n, result)
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
