from abc import abstractmethod
from collections.abc import Iterable

class Queue(Iterable):
   @abstractmethod
   def enqueue(self, element):
      '''Add one element to the rear of this queue'''
      ...

   @abstractmethod
   def dequeue(self, element):
      '''Remove and return the front element of this queue'''
      ...

   @abstractmethod
   def first(self):
      '''Return without removing the front element of this queue'''
      ...
      
   @abstractmethod
   def __len__(self) -> int:
      '''Return the number of elements in this queue'''
      ...