# 13 - C  Maximum Sum Sublist.py

# Given an array, find the contiguous sublist with the largest sum.


def find_max_sum_sublist(lst):
    if len(lst) < 1:
        return 0
    
    curMax = lst[0]
    globalMax = lst[0]
    
    for i in lst:
        if curMax < 0:
            curMax = i
        else:
            curMax += i
        if globalMax < curMax:
            globalMax = curMax
    
    return globalMax


print(find_max_sum_sublist([-4,2,-5,1,2,3,6,-5,1]))
