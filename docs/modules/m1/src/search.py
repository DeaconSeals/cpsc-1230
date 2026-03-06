def search(a, target):
   """
   This function uses the linear search algorithm to return
   the index of the first occurrence of target in a or None
   if a does not contain target.
   """
   pass

def search(a, target):
   i = 0
   while i < len(a) and a[i] != target:
      i += 1
   if i < len(a):
      return i
   else:
      return None

def search(a, target):
   for i in range(len(a)):
      if a[i] == target:
         return i
   return None