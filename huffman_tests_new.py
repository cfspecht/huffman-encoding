import unittest
import filecmp
from huffman import *

class TestList(unittest.TestCase):
   def test_cnt_freq(self):
      freqlist	= cnt_freq("test1.txt")
      anslist = [0]*256
      anslist[97:104] = [2, 4, 8, 16, 0, 2, 0] 
      self.assertListEqual(freqlist[97:104], anslist[97:104])

   def test_create_huff_tree(self):
      freqlist = cnt_freq("test1.txt")
      hufftree = create_huff_tree(freqlist)
      numdatas = 32
      dataforroot = "a"
      self.assertEqual(hufftree.freq, 32)
      self.assertEqual(hufftree.data, 'a')
      left = hufftree.left
      self.assertEqual(left.freq, 16)
      self.assertEqual(left.data, 'a')
      right = hufftree.right
      self.assertEqual(right.freq, 16)
      self.assertEqual(right.data, 'd')

   def test_create_code(self):
      freqlist = cnt_freq("test1.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('d')], '1')
      self.assertEqual(codes[ord('a')], '0000')
      self.assertEqual(codes[ord('f')], '0001')

   def test_01_encodefile(self):
      huffman_encode("test1.txt", "encodetest1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("encodetest1.txt", "test1.out"))

   def test_02_encodefile(self):
      huffman_encode("test2.txt", "encodetest2.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("encodetest2.txt", "test2.out"))

   def test_03_encodefile(self):
      huffman_encode("test3.txt", "encodetest3.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("encodetest3.txt", "test3.out"))

   def test_04_encodefile(self):
      huffman_encode("test5.txt", "encodetest5.txt")
      self.assertTrue(filecmp.cmp("encodetest5.txt", "test5.out"))

   def test_05_encodefile(self):
      huffman_encode("test6.txt", "encodetest6.txt")
      self.assertTrue(filecmp.cmp("encodetest6.txt", "test6.out"))

   def test_01_decodefile(self):
      freqlist = cnt_freq("test1.txt")
      huffman_decode(freqlist,"test1.out", "decodetest1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodetest1.txt", "test1.txt"))

   def test_02_decodefile(self):
      freqlist = cnt_freq("test2.txt")
      huffman_decode(freqlist,"test2.out", "decodetest2.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodetest2.txt", "test2.txt"))

   def test_03_decodefile(self):
      freqlist = cnt_freq("test3.txt")
      huffman_decode(freqlist, "test3.out", "decodetest3.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodetest3.txt", "test3.txt"))

   def test_tree_preord(self):
      freqlist = cnt_freq("test4.txt")
      test_tree = create_huff_tree(freqlist)
      self.assertEqual(tree_preord(test_tree), "00001-97-1-102-1-98-1-99-1-100-")


   # ADDED EDGE CASES ==============================================================================



if __name__ == '__main__': 
   unittest.main()
