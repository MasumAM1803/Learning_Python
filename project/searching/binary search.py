def binarySearch(A, l, r, x):
    if r >= 1:
        mid = l + (r-l) // 2

        if A[mid] == x:
            return mid
        elif A[mid] > x:
            return binarySearch(A, l, mid-1, x)
        else:
            return binarySearch(A, mid+1, r, x)
    else:
        return -1


A = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
x = 23
l = 0
r = len(A)-1

result = binarySearch(A, l, r, x)
if result != -1:
    print("Element is present at index %d"%result)
else:
    print("Element is not present in array")