# 07 - C Find Minimum Value in List

# Given a list of size ‘n,’ can you find the minimum value in the list? Implement your solution in Python and see if your output matches the expected output


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge_two_sorted_lists(left, right)

def merge_two_sorted_lists(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    
    while j < len_b:
        sorted_list.append(b[j])
        j += 1
    
    return sorted_list

def find_minimum(arr):
    if len(arr) == 0:
        return None
    
    pp = merge_sort(arr)
    return pp[0]
    
    arr.sort()
    return arr[0]
    # time complexity: O(nlogn)
    
    minimum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
    # time complexity: O(n)
    
    return minimum

print(find_minimum([9,2,3,6,1]))
