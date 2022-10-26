"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    for item in items:
        item = str(item)
        if frequencies.get(item) == None:
            frequencies[item] = 1
        else:
            frequencies[item] += 1
    return frequencies
