import random, time
from random import randint
def Merges(alist):
    if len(alist)>1:
        size = len(alist)
        half = size // 2
        left = alist[ :half]
        rigth = alist[half: ]
        Merges(left)
        Merges(rigth)

        i = 0
        j = 0
        k = 0
        while i<len(left) and j<len(rigth):
            if left[i] < rigth[j]:
                alist[k]= left[i]
                i = i+1
            else:
                alist[k] = rigth[j]
                j = j+1
            k = k+1
        while i < len(left):
            alist[k] = left[i]
            i= i+1
            k= k+1

        while j<len(rigth):
            alist[k]= rigth[j]
            j= j+1
            k= k+1
    return alist


A = []
for x in range(2000000):
    A.append(random.randint(1,100))
print (A)
print ("/////*/*//****//////")
t0 = time.clock()
print (Merges(A))
print ("%.2f sec"%(time.clock()-t0))
