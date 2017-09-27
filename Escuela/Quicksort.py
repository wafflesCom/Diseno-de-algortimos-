import random, time
def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more
t0 = time.clock()
a = []
for x in range(2000000):
    a.append(random.randint(0,9))
print (a)
print ("/*/*/*/*/*")
print (quickSort(a))
print ("%.2f sec"%(time.clock()-t0))
