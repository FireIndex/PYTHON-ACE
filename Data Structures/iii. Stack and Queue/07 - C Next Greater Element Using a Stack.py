# 07 - C Next Greater Element Using a Stack.py

from Stack import MyStack

def next_greater_element(lst):
    res = []
    # Iterate list
    for i in range(0, len(lst)):
        # initialise nextGreatest to -1
        next_greatest = -1
        for j in range(i+1, len(lst)):
            # Update nextGreatest when greater value found
            if lst[i] < lst[j]:
                next_greatest = lst[j]
                break
        # append next greatest
        res.append(next_greatest)
        print(str(lst[i]) + " -- " + str(next_greatest))
    return res

    # time complexity: O(n^2)

if __name__ == "__main__" :
    a = next_greater_element([4, 6, 3, 2, 8, 1, 9, 9, 9])
    print(a)
