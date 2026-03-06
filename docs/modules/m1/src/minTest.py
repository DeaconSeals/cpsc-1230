import unittest
import sys
from min import min1

# print(sys.float_info)

class MinTest(unittest.TestCase):
   
   # 000
   def test_min1_0(self):
      expected = 2
      actual = min1(2, 2, 2)
      self.assertEqual(expected, actual)

   # 001
   def test_min1_1(self):
      expected = 2
      actual = min1(2, 2, 4)
      self.assertEqual(expected, actual)

   # 010
   def test_min1_2(self):
      expected = 2
      actual = min1(2, 4, 2)
      self.assertEqual(expected, actual)

   # 011
   def test_min1_3(self):
      expected = 2
      actual = min1(2, 4, 6)
      self.assertEqual(expected, actual)

   # 011
   def test_min1_4(self):
      expected = 2
      actual = min1(2, 6, 4)
      self.assertEqual(expected, actual)

   # additional tests go here...

if __name__ == '__main__':
   unittest.main()