""" Project 3: Huffman Coding
CPE202-09
Author:
    Chris Specht
"""


class Node:
    """ Huffman Node, can be either None or Node
    Attributes:
        freq (int): frequency of the character
        data (str): the character
        left (Node/NoneType): left child
        right (Node/NoneType): right child
    """
    def __init__(self, frequency, letter=None, left=None, right=None):
        self.freq = frequency
        self.data = letter
        self.left = left
        self.right = right

    def __repr__(self):
        return "HuffmanNode {data: %s, letter: %s, left: %s, right: %s}" % (self.freq, self.data, \
                                                                            self.left, self.right)

    def __eq__(self, other):
        return isinstance(other, Node) and \
               self.freq == other.freq and \
               self.data == other.data and \
               self.left == other.left and \
               self.right == other.right


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
    lines = fp.readlines() # list of lines separated by \n
    fp.close()             # looks like ["onelinehere"]

    # iterate through each character in each line
    for line in lines:
        for char in line:
            # add 1 to index of current character
            freqlist[ord(char)] += 1

    return freqlist