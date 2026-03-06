from time import time
from statistics import mean

class Node:
    def __init__(self, element, next_node=None):
        self.element = element
        self.next = next_node

class LinkedList:
   def __init__(self):
      self.front = None
      self.rear = None
      self.size = 0

   def append(self, val):
      n = Node(val)
      if self.size == 0:
         self.front = n
         self.rear = n
      else:
         self.rear.next = n
         self.rear = n
      self.size += 1

   def __getitem__(self, i):
      if i < 0 or i >= self.size:
         raise ValueError('index out of range')

      n = self.front
      for _ in range(i):
         n = n.next

      return n.element

   def __iter__(self):
      n = self.front
      yield n.element
      for _ in range(self.size-1):
         n = n.next
         yield n.element
   
   def __len__(self):
      return self.size

def search(a, target, key=None):
   """
   This function uses the linear search algorithm to return
   the index of the first occurrence of target in a or None
   if a does not contain target.
   """
   # if not isinstance(a, Sequence):
   #    raise TypeError("Input must support indexing")

   if key is None:
      key = lambda x: x
   
   for i in range(len(a)):
      if key(a[i]) == target:
         return i
   return None

def search_iterator(a, target, key=None):
   """
   This function uses the linear search algorithm to return
   the index of the first occurrence of target in a or None
   if a does not contain target.
   """
   # if not isinstance(a, Sequence):
   #    raise TypeError("Input must support indexing")

   if key is None:
      key = lambda x: x
   
   for i, val in enumerate(a):
      if key(val) == target:
         return i
   return None

if __name__ == '__main__':
   data_size = 10000
   samples = 10

   linked = LinkedList()
   for i in range(data_size):
      linked.append(i)
   array = [i for i in range(data_size)]

   array_index = []
   array_itr = []
   for _ in range(samples):
      start = time()
      search(array, data_size+1)
      duration = time() - start
      array_index.append(duration)
      start = time()
      search_iterator(array, data_size+1)
      duration = time() - start
      array_itr.append(duration)

   print(f'array_index: {mean(array_index)*1000}')
   print(f'array_itr: {mean(array_itr)*1000}')

   linked_index = []
   linked_itr = []
   for _ in range(samples):
      start = time()
      search(linked, data_size+1)
      duration = time() - start
      linked_index.append(duration)
      start = time()
      search_iterator(linked, data_size+1)
      duration = time() - start
      linked_itr.append(duration)

   print(f'linked_index: {mean(linked_index)*1000}')
   print(f'linked_itr: {mean(linked_itr)*1000}')

   # array_index: 0.6769180297851562
   # array_itr: 0.6787776947021484
   # linked_index: 1413.1707668304443
   # linked_itr: 1.3650178909301758