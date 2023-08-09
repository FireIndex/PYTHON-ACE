# 02 - C Find Middle Node of Linked List.py
# 

from LinkedList import LinkedList
from Node import Node
# Access HeadNode => list.getHead()
# Check length => list.length()
# Check if list is empty => list.isEmpty()
# Node class  { int data ; Node nextElement;}


def find_mid(lst):
    if lst.is_empty():
        return None

    mid = 0
    if lst.length() % 2 == 0:
        mid = lst.length()//2
    else:
        mid = lst.length()//2 + 1

    cur_node = lst.get_head()
    for i in range(mid - 1):
        cur_node = cur_node.next_element

    return cur_node.data

lst = LinkedList()
lst.insert_at_head(22)
lst.insert_at_head(21)
lst.insert_at_head(10)
lst.insert_at_head(14)
lst.insert_at_head(7)

lst.print_list()
print(find_mid(lst))
