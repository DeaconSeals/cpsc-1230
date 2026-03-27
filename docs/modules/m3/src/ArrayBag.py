from bag import Bag
from collections.abc import Iterator


class ArrayBag(Bag):
   def __init__(self, capacity=1):
      self.elements = [None for _ in range(capacity)]
      self.size = 0

   def _resize(self, capacity):
      temp = [None for _ in range(capacity)]
      for i in range(self.size):
         temp[i] = self.elements[i]
      self.elements = temp

   def is_full(self):
      return self.size == len(self.elements)

   def add(self, element):
      if self.is_full():
         self._resize(self.size * 2)
      self.elements[self.size] = element
      self.size += 1

   def remove(self, element):
      i = self.locate(target)
      if i is None: return False
      self.size -= 1
      self.elements[i] = self.elements[self.size]
      self.elements[size] = None

      if self.is_sparse():
         self._resize(len(self.elements)//2)

      return True

   def __contains__(self, element):
      return self.locate(element) is not None

   def is_empty(self):
      return self.size == 0

   def __len__(self):
      return self.size

   def is_sparse(self):
      return (self.size > 0) and (self.size < len(self.elements) // 4)

   def locate(self, element):
      for i in range(self.size):
         if self.elements[i] == element:
            return i
         return None

   def __iter__(self):

class ArrayIterator(Iterator):
   def __init__(self, elements, size=None):
      # the array of elements to be iterated over
      self._elements = elements
      
      # the number of elements in the array
      if size is not None:
         self._size = size
      else:
         self._size = len(elements)
         
      # the current position of the iterator
      self._current = 0

   def __next__(self):
      if self._current < self._size:
         item = self._elements[self._current]
         self._current += 1
         return item
      else:
         raise StopIteration

if __name__ == '__main__':
   bag = ArrayBag()