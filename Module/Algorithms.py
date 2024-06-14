import math

def Bubble(lst):
    for i in range(len(lst)):
        for j in range(0,len(lst)-i-1):
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
    for i in range(1, len(lst)):
        index = i
        for j in range(i-1, -1, -1):
            if lst[index] < lst[j]:
                lst[index], lst[j] = lst[j], lst[index]
                index -= index-j
    return lst

def Combine(lst_1, lst_2):
    lst = []
    while len(lst_1) > 0 and len(lst_2) > 0:
        if lst_1[0] > lst_2[0]:
            lst.append(lst_2.pop(0))
        elif lst_1[0] < lst_2[0]:
            lst.append(lst_1.pop(0))
        else:
            lst.append(lst_1.pop(0))
            lst.append(lst_2.pop(0))
    lst.extend(lst_1)
    lst.extend(lst_2)
    return lst

def Merge(lst):
    l = 0
    h = len(lst)
    lst2 = []
    if h != 1:
        mid = math.ceil(h/2)
        lst2.append(Merge(lst[l:mid]))
        lst2.append(Merge(lst[mid:h]))
        return Combine(lst2[0], lst2[1])
    return lst

def Quick(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[len(lst) // 2]
        left = [x for x in lst if x < pivot]
        middle = [x for x in lst if x == pivot]
        right = [x for x in lst if x > pivot]
        return Quick(left) + middle + Quick(right)

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