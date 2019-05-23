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
        # return "HuffmanNode {data: %s, letter: %s, left: %s, right: %s}" % (self.freq, self.data, \
        #                                                                     self.left, self.right)
        return "HuffmanNode {data: %s, letter: %s}" % (self.freq, self.data)                                                                    

    def __eq__(self, other):
        return isinstance(other, type(self)) and \
               self.freq == other.freq and \
               self.data == other.data and \
               self.left == other.left and \
               self.right == other.right


def comes_before(a, b):
    """ Returns True if tree "a" comes before tree "b"
    In other words, if frequency of "a" < frequency of "b"
    Args:
        a (Node/NoneType): tree "a"
        b (Node/NoneType): tree "b"
    Returns:
        bool: True if tree "a" comes before tree "b", else False
    """
    # if tree a comes before tree b, a occurence < b occurence
    if a.freq < b.freq:
        return True
    # if tree a comes after tree b, a occurence > b occurence
    if a.freq > b.freq:
        return False
    # if a occurence equals b occurence
    if ord(a.data) < ord(b.data): # if a comes before b
        return True
    # if a comes after b
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
    # create list of Huffman nodes
    node_heap = [Node(freqlist[i], chr(i)) for i in range(256) if freqlist[i] != 0]

    # min heapify the list
    min_heapify(node_heap)

    # while minheap has more than one item
    while len(node_heap) > 1:

        # pop two items from minheap
        node1 = pop(node_heap)
        node2 = pop(node_heap)

        # create a new internal node by attaching node1 and node2
        new_node = Node(node1.freq + node2.freq)
        new_node.data = min(node1.data, node2.data)
        new_node.left = node1
        new_node.right = node2

        # re-insert newly created node into minheap
        insert(node_heap, new_node)

    # return huffman tree, which is last item in node_heap
    return node_heap.pop()


def min_heapify(alist):
    """ Min heapifies an unsorted list of Node objects
    Args:
        alist (list): list to be heapified
    """
    # parents of leaf nodes start here
    last_parent = len(alist) // 2 # is actually the index plus 1 since range stop is exclusive
    size = len(alist)
    # call shift_down() on parents of leaf nodes, decrement i
    for i in reversed(range(last_parent)): # iterates from "last_parent - 1" to 0
        shift_down(alist, i, size)


def insert(heap, node):
    """ Inserts a HuffmanNode into a minheap
    Args:
        heap (list): minimum heap
        node (Node): node to be inserted
    """
    # append the new node
    heap.append(node)
    # shift up, starting at index -1
    shift_up(heap, -1)


def pop(heap):
    """ Removes and returns minimum node from min heap
    Args:
        heap (list): min heap
    Returns:
        Node: HuffmanNode with minimum frequency
    """
    # empty heap
    if not heap:
        raise KeyError("Heap is empty")
    # only one item in heap
    if len(heap) == 1:
        return heap.pop()
    # swap first and last node object
    heap[0], heap[-1] = heap[-1], heap[0]
    # remove last node object from list
    target = heap.pop()
    # shift down first element, which is out of place
    shift_down(heap, 0, len(heap))
    return target


def shift_up(heap, index):
    """ Shifts Node object at bottom of current heap to its proper place
    Args:
        heap (list): min heap
        index (int): root index of current call of function
    """
    # initialize parent node
    parent = (index - 1) // 2

    # if callee index has no parent
    if parent < 0:
        return

    # get the minimum index between callee index and parent index
    if comes_before(heap[index], heap[parent]): # if child < parent
        min_index = index
    else:
        min_index = parent

    # base case
    # if parent is smaller, AKA callee node is in correct position, end function
    if min_index != index:
        return

    # swap nodes and recursively call on parent node
    heap[index], heap[parent] = heap[parent], heap[index]
    shift_up(heap, parent)
    

def shift_down(heap, i, size):
    """ Shifts Node object at top of current heap to its proper place
    Args:
        heap (list): heap to be modified
        i (int): root index of current call of function
        size (int): size of the heap (actual size, not index)
    Returns:
        int: number of comparisons
    """
    # calculate indices of root, left, and right children of current root
    root_index = i
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    # get index of smaller child
    # checking if index < size ensures a value is actually there
    # re-assigning root_index shifts pointer down
    if left_index < size and comes_before(heap[left_index], heap[root_index]):
        root_index = left_index

    if right_index < size and comes_before(heap[right_index], heap[root_index]): # checks if right value is less than root value or left value
        root_index = right_index

    # if root index has changed, swap values
    if root_index != i:
        heap[root_index], heap[i] = heap[i], heap[root_index]
        # recursive call on subheap
        shift_down(heap, root_index, size) 

    # base case is if current node has no children or node is in correct place
    return
