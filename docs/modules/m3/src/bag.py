from abc import ABC, abstractmethod
from collections.abc import Iterator

class Bag(ABC):
   @abstractmethod
   def add(self, element) -> bool:
      ...
   @abstractmethod
   def remove(self, element) -> bool:
      ...
   @abstractmethod
   def __contains__(self, element) -> bool:
      ...
   @abstractmethod
   def __len__(self) -> int:
      ...
   @abstractmethod
   def __iter__(self) -> Iterator:
      ...
