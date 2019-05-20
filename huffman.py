""" Project 3: Huffman Coding
CPE202-09
Author:
    Chris Specht
"""


class Node:
    """Write docstring for this class
    """
    def __init__(self, frequency, letter=None, left=None, right=None):
        self.freq = frequency
        self.data = letter
        self.left = left
        self.right = right

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass


def cnt_freq(filename):
    """ Opens a text file and counts frequency of occurrences of all characters
    Index of a list is the ord() of a character
    Args:
        filename (str): file to be opened
    Returns:
        list: list of frequencies of characters
    """
    # initialize empty list of size 256
    freqlist = [0] * 256

    # read target file
    fp = open(filename, "r")
    lines = fp.readlines()
    fp.close()
