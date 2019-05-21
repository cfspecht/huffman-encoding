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
        return isinstance(other, type(self)) and \
               self.freq == other.freq and \
               self.data == other.data and \
               self.left == other.left and \
               self.right == other.right


# If the tree is larger than one node, compare the frequencies of the
# root nodes and use the letter with the smallest ASCII value in the two nodes as a
# tiebreaker. 
# TODO Store the smallest letter in the new node???
def comes_before(a, b):
        """ Returns True if tree "a" comes before tree "b"
        In other words, if frequency of "a" < frequency of "b"
        Args:
            a (Node/NoneType): tree "a"
            b (Node/NoneType): tree "b"
        Returns:
            bool: True if tree "a" comes before tree "b", else False
        """
        # if one or both trees are larger than one node
            # TODO write code

        # if tree a comes before tree b, a occurence < b occurence
        if a.freq < b.freq:
            return True
        # if tree a comes after tree b, a occurence > b occurence
        elif a.freq > b.freq:
            return False

        
        # if a occurence equals b occurence
        elif ord(a.data) < ord(b.data): # if a comes before b
            return True
        elif ord(a.data) > ord(b.data): # if a comes after b
            return False


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


def create_huff_tree(freqlist):
    """ Builds and returns a Huffman tree from a given list of frequencies
    Args:
        freqlist (list): list of frequencies from cnt_freq()
    Returns:
        Node: root node of created Huffman tree
    """
    pass








# NOTE =============================================================================================

    # don't need HuffmanTree wrapper class
