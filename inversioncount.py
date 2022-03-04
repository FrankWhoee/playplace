import math
import random

def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    a = arr[:math.ceil(len(arr)/2)]
    b = arr[math.ceil(len(arr)/2):]
    a, ai = mergeSortInversions(a)
    b, bi = mergeSortInversions(b)
    c = []
    i = 0
    j = 0
    inversions = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:]
    c += b[j:]
    i = 0;
    j = 0;
    while i < len(a) and j < len(b):
        if a[i] > 2 * b[j]:
            j += 1
            inversions += (len(a)-i)
        else:
            i += 1
    
    return c, inversions


ipt = []
for i in range(10):
    ipt.append(random.randint(0,20))

print(ipt)
print(mergeSortInversions(ipt))
