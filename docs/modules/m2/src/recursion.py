def length(person) {
   if person.in_front_of is None:
      return 1;
   else:
      return 1 + length(person.in_front_of)

def factorial(n):
   fact = n
   for i in range(n-1, 0, -1):
      fact = fact*i
   return fact

def factorial(n):
   if n == 1:
      return 1
   return n * factorial(n-1)

def hanoi(n, start_peg, end_peg, temp_peg):
   '''Recursive solution to Tower of Hanoi. Prints Optimal sequence of moves'''
   if n == 1:
      print(f'Move one disk from {start_peg} to {end_peg}.')
   else:
      hanoi(n - 1, start_peg, temp_peg, end_peg)
      print(f'Move one disk from {start_peg} to {end_peg}.')
      hanoi(n - 1, temp_peg, end_peg, start_peg)

def linear_search(a, target, left, right):
   if left > right:
      return None

   if a[left] == target:
      return left
   
   return linear_search(a, target, left + 1, right)

def binary_search(a, target):
   if left > right:
      return None

   middle = left + ((right - left) // 2)
   if a[middle] == target:
      return middle
   
   if a[middle] > target:
      return binary_search(a, target, left, middle - 1)
   
   return binary_search(a, target, middle + 1, right)

if __name__ == '__main__':
   f = factorial(5)