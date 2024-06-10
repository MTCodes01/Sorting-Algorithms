def Bubble(lst):
    print(lst)
    for i in range(len(lst)):
        for j in range(0,len(lst)-i-1):
            print(i,j)
            if lst[j] > lst[j+1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    print(lst)
    return lst
        

def Selection(lst):
    print(lst)
    for i in range(len(lst)-1):
        temp = i
        for j in range(i+1, len(lst)):
            print(i,j)
            if lst[temp] > lst[j]:
                temp = j
        if i != temp:
            lst[i], lst[temp] = lst[temp], lst[i]
    print(lst)

def Insertion(lst):
    for i in range(len(lst)):
        continue

def Merge(lst):
    for i in range(len(lst)):
        continue

def Quick(lst):
    for i in range(len(lst)):
        continue

def Heap(lst):
    for i in range(len(lst)):
        continue

def Counting(lst):
    for i in range(len(lst)):
        continue

def Radix(lst):
    for i in range(len(lst)):
        continue

def Bucket(lst):
    for i in range(len(lst)):
        continue

def Shell(lst):
    for i in range(len(lst)):
        continue

def Tim(lst):
    for i in range(len(lst)):
        continue

def Comb(lst):
    for i in range(len(lst)):
        continue

def Pigeonhole(lst):
    for i in range(len(lst)):
        continue

def Cycle(lst):
    for i in range(len(lst)):
        continue

def Bitonic(lst):
    for i in range(len(lst)):
        continue