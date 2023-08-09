# 04 - C Merge Two Sorted Lists.py

# Given two sorted lists, merge them into one list which should also be sorted.

def merge_lists(lst1, lst2):
    return sorted([*lst1, *lst2])
    # Time complexity: O(nlogn)
        
    # with creating new list
    '''
    lst = [*lst1, *lst2] # O(n)
    res = [] # O(1)
    for i in range(len(lst)): # O(n)
        _min = min(lst) # O(n)
        res.append(_min) # O(1)
        lst.remove(_min) # O(n)
        # O(1) + 2*O(n) = O(n)
        
    # O(n)*O(n) = O(n^2)
    del lst
    return res
    # Time complexity: O(n^2)
    '''

    '''
    merged = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1

    # Append remaining elements from both lists (if any)
    merged.extend(lst1[i:])
    merged.extend(lst2[j:])

    return merged
    # Time complexity: O(n + m) = O(n)
    '''
    
    '''
    # Without creating new list
    ind1 = 0
    ind2 = 0
    
    while ind1 < len(lst1) and ind2 < len(lst2):
        # Remember both list are sorted
        if (lst1[ind1] > lst2[ind2]):
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1
            ind2 += 1
        else:
            ind1 += 1
    
    if ind2 < len(lst2): # Append whatever is left of list2 to list1
        lst1.extend(lst2[ind2:])
        
    return lst1
    # time complexity: O(n)
    '''
    
print(merge_lists([1,3,4,5], [2,6,7,8]))