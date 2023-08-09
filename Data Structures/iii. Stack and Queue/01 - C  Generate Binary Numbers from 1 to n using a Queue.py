# 01 - C  Generate Binary Numbers from 1 to n using a Queue.py

from Queue import MyQueue

def find_bin_queue(num):  
    queue = MyQueue()
    
    num += 1
    for i in range(1, num):
        binary = ""
        while i > 1:
            binary += str(i%2)
            i //= 2
        
        binary += "1"
        queue.enqueue(binary[::-1])
    
    return queue # return object
    # Time Complaxity: O(nlogn)
    
def find_bin_list(num):  
    list = []
    
    num += 1
    for i in range(1, num):
        binary = ""
        while i > 1:
            binary += str(i%2)
            i //= 2
        
        binary += "1"
        list.append(int(binary[::-1]))
    
    return list # return list
    # Time Complaxity: O(nlogn)
    
# print(find_bin_list(50))
# print(find_bin_queue(5).print_list())


def find_bin(number):
    result = []
    queue = MyQueue()
    queue.enqueue(1)
    for i in range(number):
        result.append(str(queue.dequeue()))
        s1 = result[i] + "0"
        s2 = result[i] + "1"
        queue.enqueue(s1)
        queue.enqueue(s2)
        
    return result # For number = 3 , result = {"1","10","11"}
    # Time Complaxity: O(n)
    
print(find_bin(50))


