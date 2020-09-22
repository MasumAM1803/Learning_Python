A = [5, 1, 4, 2, 8]
A1 = A.copy()

for i in range(len(A)):
    for j in range(0, len(A)-i-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]

for i in range(len(A)):
    print(A[i])

# RECURSIVE BUBBLE SORT
def recru_bubble_sort(A1):
    for i, num in enumerate(A1):
        try:
            if A1[i+1] < num:
                A1[i] = A1[i+1]
                A1[i+1] = num
                recru_bubble_sort(A1)
        except IndexError:
            pass
    return A1


recru_bubble_sort(A1)
print("\n Recursive")
for i in range(len(A1)):
    print(A1[i])