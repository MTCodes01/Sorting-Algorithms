def Bubble(lst):
    print(lst)
    for i in range(len(lst)):
        for j in range(0,len(lst)-i-1):
            print(i,j)
            if lst[j] > lst[j+1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
        

def Selection(lst):
    for i in range(len(lst)-1):
        temp = i
        for j in range(i+1, len(lst)):
            if lst[temp] > lst[j]:
                temp = j
        if i != temp:
            lst[i], lst[temp] = lst[temp], lst[i]
    return lst

def Insertion(lst):
    print(lst)
    for i in range(1, len(lst)):
        last = lst[i-1]
        for j in range(i, len(lst)):
            print(i,j)
            continue
    print(lst)
    return lst

def Merge(lst):
    print(lst)
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(i,j)
            continue
    print(lst)
    return lst

def Quick(lst):
    print(lst)
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(i,j)
            continue
    print(lst)
    return lst

def Heap(lst):
    print(lst)
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(i,j)
            continue
    print(lst)
    return lst

def Counting(lst):
    print(lst)
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(i,j)
            continue
    print(lst)
    return lst

def Radix(lst):
    print(lst)
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(i,j)
            continue
    print(lst)
    return lst

def Bucket(lst):
    print(lst)
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(i,j)
            continue
    print(lst)
    return lst

def Shell(lst):
    print(lst)
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(i,j)
            continue
    print(lst)
    return lst

def Tim(lst):
    print(lst)
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(i,j)
            continue
    print(lst)
    return lst

def Comb(lst):
    print(lst)
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(i,j)
            continue
    print(lst)
    return lst

def Pigeonhole(lst):
    print(lst)
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(i,j)
            continue
    print(lst)
    return lst

def Cycle(lst):
    print(lst)
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(i,j)
            continue
    print(lst)
    return lst

def Bitonic(lst):
    print(lst)
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(i,j)
            continue
    print(lst)
    return lst