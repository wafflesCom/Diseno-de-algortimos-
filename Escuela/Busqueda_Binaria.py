import random
A = []
for x in range(500):
    A.append(random.randint(1,200))
first = A[0]
final = len(A)-1
find = False

number = input("give me the number: ")
number = int(number)
while not(find) and first <= final:
    half = int((first + final) / 2)
    if number == A[half]:
        find = True
    elif number < A[half]:
        first = half - 1
    else:
        first = half + 1

if find:
    print ("the given number was found in the pisition "+str(half+1))
else:
    print ("not found")
