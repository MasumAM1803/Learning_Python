A = [4, 3, 2, 10, 12, 1, 5, 6]

for i in range(1, len(A)):
   key = A[i]
   j = i-1
   while j>= 0 and key < A[j]:
       A[j+1] = A[j]
       j -= 1
   A[j+1] = key

for i in range(len(A)):
    print(A[i])