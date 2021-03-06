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
        return "HuffmanNode {freq: %s, data: %s, left: %s, right: %s}" % (self.freq, self.data, \
                                                                            self.left, self.right)

    def __eq__(self, other):
        return isinstance(other, type(self)) and \
               self.freq == other.freq and \
               self.data == other.data and \
               self.left == other.left and \
               self.right == other.right

    def get_freq(self):
        """ Returns frequency of current node
        Returns:
            int: frequency
        """
        return self.freq

    def get_letter(self):
        """ Returns character of current node
        Returns:
            str: character
        """
        return self.data


class TreeTraversal:
    """ Helper class to generate a pre-order representation of a Huffman tree
    Attributes:
        bit_stream (str): accumulator variable for pre-order traversal of the tree
    """
    def __init__(self):
        self.bit_stream = ""

    def __eq__(self, other):
        return isinstance(other, type(self)) and \
               self.bit_stream == other.bit_stream

    def __repr__(self):
        return str(self.bit_stream)

    def get_bitstream(self):
        """ Returns bitstream, for use in tree_preord()
        Returns:
            str: bit stream
        """
        return self.bit_stream

    def tree_preord_helper(self, hufftree):
        """ Helper function for tree_preord()
        Args:
            hufftree (Node/NoneType): huffman tree being traversed
        """
        # if hufftree is none
        if not hufftree:
            return
        # if self.hufftree has children
        if hufftree.left or hufftree.right:
            self.bit_stream += "0"
            self.tree_preord_helper(hufftree.left)
            self.tree_preord_helper(hufftree.right)
        # if self.hufftree is leaf node
        else:
            self.bit_stream += "1"
            self.bit_stream += "-" + str(ord(hufftree.data)) + "-"


def comes_before(tree_a, tree_b):
    """ Returns True if tree "a" comes before tree "b"
    In other words, if frequency of "a" < frequency of "b"
    Args:
        tree_a (Node/NoneType): tree "a"
        tree_b (Node/NoneType): tree "b"
    Returns:
        bool: True if tree "a" comes before tree "b", else False
    """
    # if tree a comes before tree b, a occurence < b occurence
    if tree_a.freq < tree_b.freq:
        return True
    # if tree a comes after tree b, a occurence > b occurence
    if tree_a.freq > tree_b.freq:
        return False
    # if a occurence equals b occurence
    if ord(tree_a.data) < ord(tree_b.data): # if a comes before b
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
    file_pointer = open(filename, "r")
    lines = file_pointer.readlines() # list of lines separated by \n
    file_pointer.close()             # looks like ["onelinehere"]
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


def create_code(root_node):
    """ Traverses Huffman tree recursively (preorder), creating a list of codes for each character
    Args:
        root_node (Node): Huffman tree
    Returns:
        list: list of huffman codes for each character, sorted by index
    """
    code_list = [""] * 256
    create_code_helper(root_node, code_list, "")
    return code_list


def create_code_helper(root_node, code_list, accumulator):
    """ Traverses Huffman tree recursively, adding individual codes to code_list
    Args:
        root_node (Node/NoneType): Huffman tree
        code_list (list): list of Huffman codes
        accumulator (str): accumulator variable for Huffman path
    """
    # if current node is none
    if not root_node:
        return

    # check if current node is a leaf node
    if not root_node.left and not root_node.right:
        # add accumulator to code_list
        code_list[ord(root_node.data)] = accumulator
        # end this call
        return

    # traverse to the left
    create_code_helper(root_node.left, code_list, accumulator + "0")
    # traverse to the right
    create_code_helper(root_node.right, code_list, accumulator + "1")


def huffman_encode(in_file, out_file):
    """ Takes input file, encodes it, and writes it to ouput file
    Args:
        in_file (str): path of input file to be encoded
        out_file (str): desired path of resulting encoded output file
    """
    # process input file
    file_pointer = open(in_file, "r")
    raw_lines = file_pointer.readlines() # list of lines (strings)
    file_pointer.close()
    freqlist = cnt_freq(in_file)

    # if input file is empty
    if not raw_lines:
        out_str = ""
        file_pointer = open(out_file, "w")
        file_pointer.write(out_str)
        file_pointer.close()
        return

    # if input file is just one character, eg. ["aaaaa"]
    temp_line = raw_lines[0]
    if temp_line == len(temp_line) * temp_line[0]:

        out_str = "'%s' %s" % (temp_line[0], len(temp_line))
        file_pointer = open(out_file, "w")
        file_pointer.write(out_str)
        file_pointer.close()
        return

    # create huffman coding tools
    huff_tree = create_huff_tree(freqlist)
    code_list = create_code(huff_tree)

    # translate in_file into string of code
    out_string = ""
    for line in raw_lines:
        for char in line:
            out_string += code_list[ord(char)]

    # write translation to the output file
    file_pointer = open(out_file, "w")
    file_pointer.write(out_string)
    file_pointer.close()


def tree_preord(hufftree):
    """ Traverses huffman tree (preorder) and produces an encoded tree description
    Args:
        hufftree (Node/NoneType): huffman tree node
    Returns:
        str: encoded tree description
    """
    tree_traversal = TreeTraversal()
    tree_traversal.tree_preord_helper(hufftree)
    return str(tree_traversal)


def huffman_decode(freqlist, encoded_file, decode_file):
    """ Decodes a given huffman encoded file
    Args:
        freqlist (list): list of character frequencies, indexed by ord(char)
        encoded_file (str): path of encoded file to be decoded
        decode_file (str): desired path of resulting decoded file
    """
    # open and read encoded file
    file_pointer = open(encoded_file, "r")
    encoded_lines = file_pointer.readlines()
    file_pointer.close()

    # create code list to be used for decoding
    huff_tree = create_huff_tree(freqlist)
    code_list = create_code(huff_tree)

    # read characters until any huffman code is found
    # add resulting character to output string
    accumulator = ""
    out_string = ""
    for num in encoded_lines[0]: # num is either "0" or "1"
        accumulator += num
        # if accumulator is a huffman code
        if accumulator in code_list:
            target_index = code_list.index(accumulator)
            out_string += chr(target_index)
            accumulator = ""

    # write output string to output file
    file_pointer = open(decode_file, "w")
    file_pointer.write(out_string)
    file_pointer.close()


# HELPER FUNCTIONS =================================================================================

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
    # shift up, starting at index of last element
    shift_up(heap, len(heap) - 1)


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

    if right_index < size and comes_before(heap[right_index], heap[root_index]):
        root_index = right_index

    # if root index has changed, swap values
    if root_index != i:
        heap[root_index], heap[i] = heap[i], heap[root_index]
        # recursive call on subheap
        shift_down(heap, root_index, size)

    # base case is if current node has no children or node is in correct place
    return


# def main(): # for testing purposes
#     pass

# if __name__ == "__main__":
#     main()
