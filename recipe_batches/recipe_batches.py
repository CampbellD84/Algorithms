#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # create empty list
    possible_amt = []
    # list comp to check dicts for amts of ingredients for recipes
    check_if_enough = [ing for ing in recipe if
                       recipe.keys() == ingredients.keys() and
                       recipe[ing] > ingredients[ing]
                       or not ing in ingredients]

    if len(check_if_enough) > 0:
        return 0

    possible_amt = [(ingredients[ing] // recipe[ing])
                    for ing in ingredients if ingredients[ing] >= recipe[ing]]

    return min(possible_amt)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
