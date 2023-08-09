# 06 - C List of Products of all Elements.py

# Given a list, modify it so that each index stores the product of all elements in the list except the element at the index itself.


def find_product(lst):
    
    # new_lst = []
    # for i in range(len(lst)):
    #     prod = 1
    #     for j in range(len(lst)):
    #         if i != j:
    #             prod *= lst[j]
    #     new_lst.append(prod)
        
    # # time complexity: O(n^2)
    # # space complexity: O(n)
    
    # return new_lst

    
    prod = 1
    zero = False
    for e in lst:
        if e != 0:
            prod *= e
        else:
            zero = True
    # time complexity: O(n)
    
    for i, e in enumerate(lst):
        if zero:
            if e == 0:
                lst[i] = prod
            else:
                lst[i] = 0
        else:
            lst[i] = prod/e
    # time complexity: O(n)
    
    # space complexity: O(1)
    # total time complexity: O(n)

    return lst
    

arr = [0,1,2,3]
print(find_product(arr))