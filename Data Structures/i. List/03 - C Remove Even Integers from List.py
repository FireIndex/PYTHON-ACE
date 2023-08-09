# 03 - C Remove Even Integers from List.py

# Write a function removeEven(list) that takes in a list of integers and returns a list with all even integers removed.

def remove_even(lst):
    # one way
    return list(filter(lambda x: x%2 == 0, lst))

    # another way
    # return [x for x in lst if x%2 != 0]
    
    # another way
    # for i in lst:
    #     if i%2 == 0:
    #         lst.remove(i)
    # return lst
    
# time complexity: O(n)
    
print(remove_even([1,2,4,5,10,6,3]))