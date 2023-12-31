# 03 - C Remove Duplicates from Linked List.py
# Let's try to figure out the Pythonic solution for removing duplicates from a linked list.

from _LinkedList import LinkedList
from _Node import Node


def remove_duplicates(lst):
    if lst.is_empty():
        return None

    # If list only has one node, leave it unchanged
    if lst.get_head().next_element is None:
        return lst

    outer_node = lst.get_head()
    while outer_node:
        inner_node = outer_node  # Iterator for the inner loop
        while inner_node:
            if inner_node.next_element:
                if outer_node.data == inner_node.next_element.data:
                    # Duplicate found, so now removing it
                    new_next_element = inner_node.next_element.next_element
                    inner_node.next_element = new_next_element
                else:
                    # Otherwise simply iterate ahead
                    inner_node = inner_node.next_element
            else:
                # Otherwise simply iterate ahead
                inner_node = inner_node.next_element
        outer_node = outer_node.next_element

    return lst

# The nested while loops increase this program’s complexity to O(n2).

lst = LinkedList()
lst.insert_at_head(7)
lst.insert_at_head(7)
lst.insert_at_head(7)
lst.insert_at_head(22)
lst.insert_at_head(14)
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)


lst.print_list()
remove_duplicates(lst)
lst.print_list()