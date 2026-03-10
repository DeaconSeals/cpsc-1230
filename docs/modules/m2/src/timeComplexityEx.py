for i in range(N):
   a = a + i
   b += 1
   print(a, b)

for i in range(N):
   for j in range(N):
      print(i*j)


count = 0
k = n

while k > 1:
   k = k / 2
   count += 1

for i in range(n):
   for j in range(n):
      print(i*j)

for i in range(n):
   count += 1


if a < b:
   while k > 1:
      k = k / 2
      count += 1
else:
   for i in range(n):
      count += 1

count = 0
for i in range(n):
   j = 1
   while j < n:
      for k in range(1, n, 2):
         count += 1
      j = j * 2

#1
count = 0
for i in range(1, n+1):
   for j in range(n, 1, -1):
      for k in range(1, n, 2):
         count += 1

#2
count = 0
for i in range(1, n+1):
   for j in range(n, 1, -1):
      for k in range(1, 1000, 2):
         count += 1

#3
count = 0
for i in range(1, 1000000):
   for j in range(i, 500, -1):
      for k in range(1, 10500, 2):
         count += 1

#4
count = 0
j = 1
for i in range(1, n):
   while j < n:
      j += 1
      count += 1
   j = 1

#5
count = 0
i = n
while i > 1:
   count += 1
   i = i / 2

#6
count = 0
i = 1
while i < n:
   count += 1
   i = i * 2

#7
count = 0
for i in range(1, n+1):
   j = n
   while j > 1:
      for k in range(1, n, 2):
         count += 1
      j = j / 2