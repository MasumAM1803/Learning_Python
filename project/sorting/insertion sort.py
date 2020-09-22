A = [4, 3, 2, 10, 12, 1, 5, 6]
A1 = A.copy()

for i in range(1, len(A)):
   key = A[i]
   j = i-1
   while j>= 0 and key < A[j]:
       A[j+1] = A[j]
       j -= 1
   A[j+1] = key

for i in range(len(A)):
    print(A[i])


def recru_insertion_sort(A1, n):
    if n <= 1:
        return
    recru_insertion_sort(A1, n-1)
    last = A1[n-1]
    j = n-2

    while j>=0 and A1[j]>last:
        A1[j+1] = A1[j]
        j=j-1
    A1[j+1] = last

n = len(A)
recru_insertion_sort(A1, n)
print('\n')
for i in range(n):
    print(A1[i])