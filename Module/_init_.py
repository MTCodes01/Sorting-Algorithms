algorithm_timing = {"Bubble" : 0, "Selection": 0, "Insertion": 0, "Merge" : 0,
                    "Quick" : 0, "Heap" : 0, "Counting" : 0, "Radix" : 0,
                    "Bucket" : 0, "Shell" : 0, "Tim" : 0, "Comb" : 0,
                    "Pigeonhole" : 0, "Cycle" : 0, "Bitonic" : 0
                    }

for i in algorithm_timing.keys():
    print(f"\ndef {i}(lst):\n    print(lst)\n    for i in range(len(lst)):\n\tfor j in range(len(lst)):\n\t    print(i,j)\n\t    continue\n    print(lst)\n    return lst")
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

print(list(range(len([1,2,5,4,5]),0,-1)))