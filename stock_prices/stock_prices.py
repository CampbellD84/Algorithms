#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # store result of differences between prices in list
    prob_profit = []
    # iterate through prices list
    for idx in range(0, len(prices)):
        # buy stock
        stock_bought = prices[idx]

        # iterate through list again
        for jdx in range(0, len(prices)):
            # compare prices
            if idx > jdx:
                # sell stock
                stock_sold = prices[jdx]
                # add difference result to list
                prob_profit.append(stock_bought - stock_sold)

    # find maximum profit in result list
    max_prof = max(prob_profit)
    return max_prof


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
