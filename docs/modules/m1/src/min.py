# def min(a, b, c):
#    """Returns the minimum values of three real number parameters"""
#    pass

def min1(a, b, c):
   if a < b and a < c:
      return a
   if b < a and b < c:
      return b
   return c

def min2(a, b, c):
   if a < b:
      if a < c:
         return a
      elif c < a:
         return c
      else:
         return b
   else:
      if b < c:
         return b
      elif c < b:
         return c
      else:
         return b