# 12 - C Rearrange Sorted List in Max-Min Form.py
# Arrange elements in such a way that the maximum element appears at first position, then minimum at second, then second maximum at third and second minimum at fourth and so on.

def max_min(lst):
    
    '''Solution #1: Creating a new list'''
    # result = []
    # for i, x in enumerate(lst[:len(lst)//2]):
    #     result.append(lst[-(i+1)])
    #     result.append(x)
        
    # if len(lst) % 2 == 1:
    #     result.append(lst[len(lst)//2])
        
    # return result
    # # time complexity: O(n)
    # # space complexity: O(n)
    
    '''Solution #2: Using space complaxity O(1) Extra Space'''
    for i in range(len(lst)//2):
        lst.insert(2*i+1, lst.pop()) # time complexity: O(n)
    return lst
    # time complexity: O(n^2)
    
    

lst = [1,2,3,4,5]
print(max_min(lst)) # [5,1,4,2,3]