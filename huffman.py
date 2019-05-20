"""Huffman Coding
CPE202

Author:
    Put your name here
"""
class Node:
    """Write docstring for this class
    """
    def __init__(self, frequency, letter=None, left=None, right=None):
        self.freq = frequency
        self.data = letter
        self.left = left
        self.right = right

    #to-do: write the repr and eq methods
