# 05 - C Return the Nth Node from End.py

from _LinkedList import LinkedList
from _Node import Node


def find_nth(lst, n):
    if (lst.is_empty()):
        return -1
    
    _len = lst.length()
    if n < 0 or n > _len:
        return -1
    
    count = 0
    cur_node = lst.get_head()
    while count + n < _len:
        cur_node = cur_node.next_element
        count += 1
    
    return cur_node.data

    # Time complexity is O(n)


lst = LinkedList()
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.insert_at_head(8)
lst.insert_at_head(22)
lst.insert_at_head(15)


lst.print_list()
print(find_nth(lst, 5))
print(find_nth(lst, 1))
print(find_nth(lst, 10))

