# 05 - C Find Two Numbers that Add up to k.py

# Given a list and a number "k", find two numbers from the list that sum to "k".


def binary_search(a, item):
    first = 0
    last = len(a) - 1
    found = False
    index = -1
    
    while first <= last and not found:
        mid = (first + last) // 2
        
        if a[mid] == item:
            index = mid
            found = True
        else:
            if a[mid] < item:
                first = mid + 1
            else:
                last = mid - 1
                
    return index

def find_sum(lst, k):
    '''
    for i, x in enumerate(lst):
        for j, y in enumerate(lst):
            if x + y == k and i != j:
                return [x, y]
    # time complexity: O(n^2)
    '''
      
         
    '''
    lst.sort()
    for j in range(len(lst)): # O(n)
        # find the difference in list through binary search
        # return the only if we find an index
        index = binary_search(lst, k -lst[j]) # time complexity: O(logn)
        if index is not -1 and index is not j:
            return [lst[j], k -lst[j]]
    # Time complexity: O(nlogn)
    '''

    
    # '''
    # sort the list
    lst.sort()
    index1 = 0
    index2 = len(lst) - 1
    result = []
    sum = 0
    # iterate from front and back
    # move accordingly to reach the sum to be equal to k
    # returns false when the two indices meet
    while (index1 != index2):
        sum = lst[index1] + lst[index2]
        if sum < k:
            index1 += 1
        elif sum > k:
            index2 -= 1
        else:
            result.append(lst[index1])
            result.append(lst[index2])
            return result
    return False
    # Time complexity: O(n)
    # '''


lst = [1,21,3,14,5,60,7,6]
k = 81
print(find_sum(lst, k))