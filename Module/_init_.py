# algorithm_timing = {"Bubble" : 0, "Selection": 0, "Insertion": 0, "Merge" : 0,
#                     "Quick" : 0, "Heap" : 0, "Counting" : 0, "Radix" : 0,
#                     "Bucket" : 0, "Shell" : 0, "Tim" : 0, "Comb" : 0,
#                     "Pigeonhole" : 0, "Cycle" : 0, "Bitonic" : 0
#                     }

# for i in algorithm_timing.keys():
#     print(f"\ndef {i}(lst):\n    print(lst)\n    for i in range(len(lst)):\n\tfor j in range(len(lst)):\n\t    print(i,j)\n\t    continue\n    print(lst)\n    return lst")
    # print(f' "{i}" : S.{i}', end=",")
    # print(i,end=" ,")

# print(type([]))

# def Bubble(lst):
#     print(lst)
#     for i in range(len(lst)): #[1, 3, 7, 4, 5]
#         if type(lst[i]) == type([]):
#             lst[i] = Bubble(lst[i])
#         else:
#             for j in range(0,len(lst)-i-1):
#                 print(i,j)
#                 if (type(lst[j]) != type([])) and (type(lst[j+1]) != type([])):
#                     if lst[j] > lst[j+1]:
#                         lst[j+1], lst[j] = lst[j], lst[j+1]
#     print(lst)
#     return lst

# print(list(range(len([1,2,5,4,5]),0,-1)))

# def change(lst):
#     print(lst)
#     lst.append(5)
#     print(lst)
# lst = [1,2,3,4]
# change(lst)
# print(lst)

import math

def merge(lst_1, lst_2):
    lst = []
    while len(lst_1) > 0 and len(lst_2) > 0:
        print("test1:", lst_1, lst_2, lst)
        if lst_1[0] > lst_2[0]:
            lst.append(lst_2.pop(0))
        elif lst_1[0] < lst_2[0]:
            lst.append(lst_1.pop(0))
        else:
            lst.append(lst_1.pop(0))
            lst.append(lst_2.pop(0))
    print("test2:", lst_1, lst_2, lst)
    lst.extend(lst_1)
    lst.extend(lst_2)
    return lst

def merge_sort(lst):
    l = 0
    h = len(lst)
    lst2 = []
    print("lst1:",lst)
    if h != 1:
        mid = math.ceil(h/2)
        lst2.append(merge_sort(lst[l:mid]))
        print("lst2_1:",lst2)
        lst2.append(merge_sort(lst[mid:h]))
        print("lst2_2:",lst2)
        return merge(lst2[0], lst2[1])
    return lst

lst= [11,22,8,43,94,3,5,1,27,6,7,21,3]
print(merge_sort(lst.copy()))

# print(len(lst),int(math.ceil(len(lst)/2)))
# print(lst1 + lst2)
# lst1.append(lst2.pop(0))
# print(lst1,lst2)