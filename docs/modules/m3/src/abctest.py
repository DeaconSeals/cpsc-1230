from abc import ABC, abstractmethod

class myABC(ABC):

   def test1(self):
      pass


   #@abstractmethod
   def test2(self):
      pass


class testcls(myABC):
   def some_func(self):
      print('potato')


if __name__ == '__main__':
   thing = testcls()
   thing.some_func()