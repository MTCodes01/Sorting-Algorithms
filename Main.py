"""
This script is designed to test and measure the performance of various sorting algorithms.
It imports the necessary algorithms from a module and applies them to a given list.
The execution time for each algorithm is calculated and displayed.

How to Use:
1. Ensure you have a module named 'Algorithms' with the sorting functions implemented.
2. Replace the 'inp' variable with your own list of numbers to sort.
3. Run the script to see the sorted list and the time taken by each algorithm.

List of Algorithms:
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Counting Sort
- Radix Sort
- Bucket Sort
- Shell Sort
- Tim Sort
- Comb Sort
- Pigeonhole Sort
- Cycle Sort
- Bitonic Sort
"""

# Import section
import time
import Module.Algorithms as S

# a = input("Enter \"Y\" to start!:")
a = "y"

def sort_time(func, lst):
    start_time = time.perf_counter()
    sorted_list = func(lst)
    end_time = time.perf_counter()
    return sorted_list, f'{(end_time - start_time):.8f} s'

#__main__
def __main__():
    q, quit, Q = "q", "q", "q"
    while True:
        # inp = eval(input("\nEnter your list (q --> quit) : "))
        inp = [1,23,12,324,32,134,53,1245,12,53]
        if type(inp) == type("") and inp == "q":
            break
        elif type(inp) == type([]):
            algorithms = {"Bubble" : S.Bubble, "Selection" : S.Selection, "Insertion" : S.Insertion,\
                           "Merge" : S.Merge, "Quick" : S.Quick, "Heap" : S.Heap, "Counting" : S.Counting,\
                              "Radix" : S.Radix, "Bucket" : S.Bucket, "Shell" : S.Shell, "Tim" : S.Tim,\
                                  "Comb" : S.Comb, "Pigeonhole" : S.Pigeonhole, "Cycle" : S.Cycle, "Bitonic" : S.Bitonic
                                  }
            sorted_lists = {}
            algorithm_timing = {}
            for i, j in algorithms.items():
                sorted_lists[i], algorithm_timing[i] = sort_time(j, inp.copy())
            print(f"\nSorted List is: {sorted_lists["Bubble"]}\n")
            for i, j in algorithm_timing.items():
                print(f"{i:<10} : {j}")
        else:
            print("\nEnter a List!\n")
        break
        
if a.lower()=="y":
    # try:
        __main__()
    # except:
    #     print("\n-- ERROR --")
print("\nEXITED!\n")