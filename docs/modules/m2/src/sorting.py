import random

def less(x, y):
   return x < y

def swap(a, i, j):
   a[i], a[j] = a[j], a[i]

def selection_sort(a):
   for i in range(len(a)):
      min_idx = i
      for j in range(i+1, len(a)):
         if a[j] < a[min_idx]:
            min_idx = j
      swap(a, i, min_idx)

def insertion_sort(a):
   for i in range(len(a)):
      for j in range(i, 0, -1):
         if a[j] < a[j-1]:
            swap(a, j, j-1)
         else:
            break

def max(a):
   m = a[0]
   for value in a:
      if value > m:
         m = i
   return m

def max(a, l, r):
   if l == r:
      return a[l]

   mid = (l + r) // 2
   lm = max(a, l, mid)
   rm = max(a, mid+1, r)

   if lm > rm:
      return lm
   else:
      return rm

def merge_sort(a, left = 0, right = None, aux = None):
   if left == right: return

   if aux is None:   aux = a.copy()
   if right is None: right = len(a)-1

   mid = left + ((right - left) // 2)
   merge_sort(a, left, mid, aux)
   merge_sort(a, mid+1, right, aux)

   merge(a, left, mid, right, aux)

def merge(a, left, mid, right, aux):
   for k in range(left, right + 1):
      aux[k] = a[k]

   i = left
   j = mid + 1
   for k in range(left, right + 1):
      if i > mid:
         a[k] = aux[j]
         j += 1
      elif j > right:
         a[k] = aux[i]
         i += 1
      elif aux[j] < aux[i]:
         a[k] = aux[j]
         j += 1
      else:
         a[k] = aux[i]
         i += 1

def merge(a, left, mid, right, aux):
   for k in range(left, right + 1): aux[k] = a[k]
   
   i, j = left, mid+1
   for k in range(left, right + 1):
      if i > mid:             a[k], j = aux[j], j+1
      elif j > right:         a[k], i = aux[i], i+1
      elif aux[j] < aux[i]:   a[k], j = aux[j], j+1
      else:                   a[k], i = aux[i], i+1

def qsort(a, left, right):
   if right <= left:
      return

   j = partition(a, left, right)
   qsort(a, left, j-1)
   qsort(a, j+1, right)

def partition(a, left, right, pivot_idx):
   pivot = a[pivot_idx]
   swap(a, pivot_idx, right) # move pivot to the end
   p = left # p will become the final index of pivot
   for i in range(left, right):
      if a[i] < pivot:
         swap(a, i, p)
         p += 1
   swap(a, p, right) # move pivot to its correct location
   return p

def shuffle(a):
   for i in range(len(a)-1, 0, -1):
      j = random.randrange(i+1)
      swap(a, i, j)

def quicksort(a):
   shuffle(a)
   qsort(a, 0, len(a)-1)

# thing = [i for i in range(10)]
# thing.reverse()
# print(thing)
# merge_sort(thing)
# print(thing)

class Data():
   def __init__(self, v1, v2):
      self.value1 = v1
      self.value2 = v2

   def __lt__(self, other: Data):
      return self.value1 < other.value1

class Student():
   def __init__(self, fname, lname, section):
      self.fname = fname
      self.lname = lname
      self.section = section
   
   def to_string(self)
      print(f'{self.lname}, {self.fname}, {self.section}')

def quicksort(a, key = None):
   ...

def mergesort(a, key = None):
   ...