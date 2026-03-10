def sumA(N):
   sum_value = N*(N+1)/2
   return sum_value

def sumB(N):
   sum_value = 0
   for i in range(1, N+1):
      sum_value += i
   return sum_value

def sumC(N):
   sum_value = 0
   for i in range(1, N+1):
      for j in range(1, i+1):
         sum_value += 1
   return sum_value