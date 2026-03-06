import unittest
from collections.abc import Sequence
from book import Book

def search(a, target, key=None):
   """
   This function uses the linear search algorithm to return
   the index of the first occurrence of target in a or None
   if a does not contain target.
   """
   if not isinstance(a, Sequence):
      raise TypeError("Input must be a Sequence")

   if key is None:
      key = lambda x: x
   
   for i, val in enumerate(a):
      if key(val) == target:
         return i
   return None

class SearchTest(unittest.TestCase):
   def test_search_a_non_index(self):
      with self.assertRaises(TypeError):
         search(None, 1)
      with self.assertRaises(TypeError):
         search(0, 1)
   
   def test_search_a_len_0(self):
      expected = None
      actual = search([], 1)
      self.assertEqual(expected, actual)

   # additional tests go here...
   def test_search_string(self):
      a = ['2', '4', '6', '8', '10']
      target = '8'
      expected = 3
      actual = search(a, target)
      self.assertEqual(expected, actual)

   def test_search_int(self):
      a = [2, 4, 6, 8, 10]
      target = 8
      expected = 3
      actual = search(a, target)
      self.assertEqual(expected, actual)

   def test_search_book(self):
      a = [
            Book("author1", "title1", 123),
            Book("author2", "title2", 456),
            Book("author3", "title3", 789),
            Book("author4", "title4", 123),
            Book("author5", "title5", 456)
          ]
      target = Book("author4", "title4", 999)
      expected = 3
      actual = search(a, target)
      self.assertEqual(expected, actual)

if __name__ == '__main__':
   a = [
         Book("author1", "title1", 123),
         Book("author2", "title2", 456),
         Book("author3", "title3", 789),
         Book("author4", "title4", 123),
         Book("author5", "title5", 456)
       ]
   print(min(a, key=lambda book: book.pages))
   
   def print_book_list(books):
      for book in books:
         print(f'{book.author} {book.title} {book.pages}')
      print()

   a = [
         Book("Author A", "Title Z", 456),
         Book("Author B", "Title Y", 123),
         Book("Author C", "Title X", 789)
       ]

   print_book_list(a)

   a.sort(key = lambda x: x.title)
   print_book_list(a)
   a.sort(key = lambda x: x.pages)
   print_book_list(a)
   a.sort(key = lambda x: x.author)
   print_book_list(a)

   unittest.main()

def contains(a, Target):
   for element in a:
      if element == target:
         return True

   return False