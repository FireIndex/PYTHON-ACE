# 09 - C Find Second Maximum Value in a List.py

# Given a list of size n, can you find the second maximum element in the list? Implement your solution in Python and see if your output matches the correct output.

class MergeSort:
    def __init__(self, arr):
        self.arr = arr
        
    # @staticmethod
    def sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            a = arr[:mid] # left half of the array (excluding mid)
            b = arr[mid:] # right half of the array (including mid)

            self.sort(a) # sub-divide left half of the array until it is sorted (base case)
            self.sort(b) # sub-divide right half of the array until it is sorted (base case)

            i = j = k = 0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    arr[k] = a[i]
                    i += 1
                else:
                    arr[k] = b[j]
                    j += 1
                k += 1

            while i < len(a):
                arr[k] = a[i]
                i += 1
                k += 1

            while j < len(b):
                arr[k] = b[j]
                j += 1
                k += 1
                

def find_second_maximum(lst): 
    '''Solution #1: Sort and index'''
    # merge_sorter = MergeSort(lst)
    # merge_sorter.sort(lst)
    # return merge_sorter.arr[-2]
    # # time complexity: O(nlogn)
    # # space complexity: O(n)
    
    '''Caveat: Note that above solution won’t work if duplicates of the first largest number exist. For instance, it would not work with a list like [1,2,4,4] since it would return 4 which is at the second last index of the sorted list. But, it is the largest element and not the correct answer'''
    
    '''Solution #2: Traversing the list twice'''
    # max_num = max(lst)
    # for i, j in enumerate(lst):
    #     if j == max_num:
    #         lst[i] = float('-inf')
    # return max(lst)
    # # time complexity: O(n)
    # # space complexity: O(1)
    
    '''Another way'''
    # first_max = second_max = float('-inf')
    # for i in lst:
    #     if i > first_max:
    #         first_max = i
    # for i in lst:
    #     if i > second_max and i < first_max:
    #         second_max = i
    # return second_max
    # # time complexity: O(n)
    # # space complexity: O(1)
    
    '''Solution #3: Traversing the list once'''
    if (len(lst) < 2):
        return None
    
    max_num = second_max = float('-inf')
    for i in lst:
        if i > max_num:
            second_max = max_num
            max_num = i
        elif i > second_max and i < max_num:
            second_max = i
    return second_max
    # time complexity: O(n)
    # space complexity: O(1) 
    

print(find_second_maximum([42, 17, 8, 56, 29, 91, 91, 3, 67, 12, 51]))