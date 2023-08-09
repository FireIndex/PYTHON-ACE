# 10 - C Right Rotate List.py

# Given a list, can you rotate its elements by one index from right to left? Implement your solution in Python and see if your code runs successfully

def right_rotate(lst, k):
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
        k -= 1 # for indexing
        
    '''Solution #1: Manual Rotation'''
    # for i in range(k):
    #     lst.append(lst[i])
    # return lst[k:]
    
    '''Solution #2: Pythonic Rotation'''
    return lst[k:] + lst[:k]

    # List slicing is in O(k) where k represents the number of elements that are sliced, and since the entire list is sliced hence the total time complexity is in O(n)
    

lst = [10,20,30,40,50]
k = 3

print(right_rotate(lst, k))
