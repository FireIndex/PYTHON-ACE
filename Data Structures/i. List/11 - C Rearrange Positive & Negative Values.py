# 11 - C Rearrange Positive & Negative Values.py
# Given a list, can you rearrange its elements in such a way that the negative elements appear at one end and positive elements appear at the other? Solve this problem in Python and see if your code runs correctly.

def rearrange(lst):
    '''Using filter'''
    # return list(filter(lambda x: x < 0, a)) + list(filter(lambda x: x >= 0, a))
    # # time complexity: O(n) + O(n) = O(n)
        
    '''Solution #2: Rearranging in Place, single iteration'''
    i = 0
    p = 0 # first positive element index
    while i < len(lst):
        if lst[i] < 0:
            if i != p:
                lst[i], lst[p] = lst[p], lst[i]
            i+=1
            p+=1
        else:
            i+=1
    return lst
    # time complexity: O(n) 
    
    '''Solution #3: Pythonic Rearrangement'''
    # return [i for i in lst if i < 0] + [i for i in lst if i >= 0]
    # # time complexity: O(n) + O(n) = O(n)
    

print(rearrange([10,-1,20,-8,4,5,-9,-6]))