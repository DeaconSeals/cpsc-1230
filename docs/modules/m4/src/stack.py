from abc import abstractmethod
from collections.abc import Iterable

class Stack(Iterable):
   @abstractmethod
   def push(self, element):
      '''Add one element to the top of this stack'''
      ...

   @abstractmethod
   def pop(self, element):
      '''Remove and return the top element of this stack'''
      ...

   @abstractmethod
   def peek(self):
      '''Return without removing the top element of this stack'''
      ...
      
   @abstractmethod
   def __len__(self) -> int:
      '''Return the number of elements in this stack'''
      ...