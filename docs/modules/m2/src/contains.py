# worst case a: 110.28973817825317 ms
# worst case b: 110.98644018173218 ms
# worst case binary: 0.005161762237548828 ms
# avg case a: 118.20688247680664 ms
# avg case b: 59.14151906967163 ms
# avg case b (sorted): 5.230135917663574 ms
# avg case binary: 0.00797271728515625 ms

import random
from time import time
from statistics import mean

def binary_search(a, target):
   left = 0
   right = len(a) - 1
   while left <= right:
      middle = (left + right) // 2
      if target < a[middle]:   
         right = middle - 1
      elif target > a[middle]: 
         left = middle + 1
      else:                    
         return middle
   return None


def contains_a(a, target):
   found = False
   for value in a:
      if value == target:
         found = True
   return found

def contains_b(a, target):
   for value in a:
      if value == target:
         return True
   return False

# def contains_c(a, target):
#    for idx, value in enumerate(a):
#       if value == target:
#          a.pop(idx)
#          a.insert(0, target)
#          return True
#    return False

def benchmark(fun, data, target):
   start = time()
   fun(data, target)
   return time()-start

def weighted_sample(data_range):
   if random.random() < 0.9:
      return random.randrange(data_range//10)
   else:
      return random.randint(data_range//10, data_range)

if __name__ == '__main__':
   data_size = 10
   samples = 100
   warmup = 2000
   data = [i for i in range(data_size)]
   sorted_data = data[:]
   random.shuffle(data)

   # warm up
   [benchmark(contains_a, data, data_size+1) for _ in range(warmup)]
   
   # worst case
   worst_a_times = []
   for _ in range(samples):
      worst_a_times.append(benchmark(contains_a, data, data_size+1))
   print(f'worst case a: {mean(worst_a_times)*1000} ms')

   worst_b_times = []
   for _ in range(samples):
      worst_b_times.append(benchmark(contains_b, data, data_size+1))
   print(f'worst case b: {mean(worst_b_times)*1000} ms')

   worst_binary_times = []
   for _ in range(samples):
      worst_binary_times.append(benchmark(binary_search, data, data_size+1))
   print(f'worst case binary: {mean(worst_binary_times)*1000} ms')

   # worst_c_times = []
   # for _ in range(samples):
   #    worst_c_times.append(benchmark(contains_c, data, data_size+1))
   # print(f'worst case c: {mean(worst_c_times)*1000} ms')

   # average case
   avg_a_times = []
   for _ in range(samples):
      avg_a_times.append(benchmark(contains_a, data, random.randrange(data_size)))
   print(f'avg case a: {mean(avg_a_times)*1000} ms')

   avg_b_times = []
   for _ in range(samples):
      avg_b_times.append(benchmark(contains_b, data, random.randrange(data_size)))
   print(f'avg case b: {mean(avg_b_times)*1000} ms')

   data = sorted_data
   avg_b_sorted_times = []
   for _ in range(samples):
      avg_b_sorted_times.append(benchmark(contains_b, data, weighted_sample(data_size)))
   print(f'avg case b (sorted): {mean(avg_b_sorted_times)*1000} ms')

   avg_binary_times = []
   for _ in range(samples):
      avg_binary_times.append(benchmark(binary_search, data, random.randrange(data_size)))
   print(f'avg case binary: {mean(avg_binary_times)*1000} ms')