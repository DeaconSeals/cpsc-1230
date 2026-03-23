Which big-O expression best characterizes the time complexity of the following code?

def foo(N: int):
    count = 0
    i = 100
    while i > 1:
        i = i-2
        for j in range(100):
            for k in range(100):
                count += 1
    return count

def foo(N: int):
    count = 0
    i = N
    while i > 1:
        count += 1
        i = i / 2
    i = N
    while i > 1:
        count += 1
        i = i - 2
    return count

def foo(N: int):
    count = 0
    i = N
    for i in range(1, 10):
        count += 1
    while i > 1:
        count += 1
        i = i / 2
    return count

def foo(N: int):
    count = 0
    i = 1
    while i < N:
        j = 1
        while j < N:
            count += 1
            j = j * 2
        i = i + 2
    return count

def foo(N: int):
    count = 0
    j = 0
    while j < N:
        for i in range(1, N):
            count += 1
        j = j + 2
    return count

def kmin(a, k):
   '''returns the kth smallest element in a sequence of unique values'''
   seq = sorted(a)
   return seq[k-1]

def foo(k: int):
   if k == 1:
      return 1
   return foo(k - 1) + 2

def max1(a):
   maximum = -1
   for value in a:
      if value > maximum:
         maximum = value
   return maximum

def foo(N: int):
   count = 0
   for i in range(1, 10, 2):
      for j in range(i, 20):
         k = 1
         while k < 30:
            count += 1
            k += 1
   return count

def foo(N: int):
   count = 0
   for i in range(0, N, 2):
      for j in range(i, N):
         k = 1
         while k < N/2:
            count += 1
            k += 1
   return count

def foo(N: int):
   count = 0
   i = N
   while i > 1:
      count += 1
      i = i / 2
   for j in range(1, N):
      count += 1
   return count

def foo(N: int):
   count = 0
   i = 1
   while i < N:
      for j in range(1, N, 2):
         count += 1
      i = i * 2
   return count

def foo(a: list, k: int):
   for i in range(k):
      location = i
      for j in range(i+1, len(a)):
         if a[j] < a[location]:
            location = j
      swap(a, i, location)
   return a[k-1]

def sum1(n: int):
   '''computes the sum from 1..n'''
   if n == 1:
      return 1
   return n + ________