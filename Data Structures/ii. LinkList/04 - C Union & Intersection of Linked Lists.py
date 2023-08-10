# 04 - C Union & Intersection of Linked Lists.py

from _LinkedList import LinkedList
from _Node import Node


def union(list1, list2):
    # Return other List if one of them is empty
    if (list1.is_empty()):
        return list2
    elif (list2.is_empty()):
        return list1

    start = list1.get_head()

    # Traverse the first list till the tail
    while start.next_element:
        start = start.next_element

    # Link last element of first list to the first element of second list
    start.next_element = list2.get_head()
    list1.remove_duplicates()
    return list1
    
    # time complexity to O(l^2) where l = m + n. Here, m is the size of the first list, and n is the size of the second list.

def intersection(list1, list2):

    result = LinkedList()
    current_node = list1.get_head()

    # Traversing list1 and searching in list2
    # insert in result if the value exists
    while current_node is not None:
        value = current_node.data
        if list2.search(value):
            result.insert_at_head(value)
        current_node = current_node.next_element

    # Remove duplicates if any
    result.remove_duplicates()
    return result

    # The time complexity will be max(O(mn),O(min(m,n)^2 )) where m is the size of the first list and n is the size of the second list.


ulist1 = LinkedList()
ulist2 = LinkedList()
ulist1.insert_at_head(8)
ulist1.insert_at_head(22)
ulist1.insert_at_head(15)
ulist2.insert_at_head(21)
ulist2.insert_at_head(14)
ulist2.insert_at_head(7)

print("-------- Union --------")
print("List 1")
ulist1.print_list()

print("\nList 2")
ulist2.print_list()

new_list = union(ulist1,ulist2)
print("\nUnion of list 1 and 2")
new_list.print_list()


# Intersection
ilist1 = LinkedList()
ilist2 = LinkedList()
ilist1.insert_at_head(14)
ilist1.insert_at_head(22)
ilist1.insert_at_head(15)
ilist2.insert_at_head(21)
ilist2.insert_at_head(14)
ilist2.insert_at_head(15)


print("\n-------- Intersection --------")
print("List 1")
ilist1.print_list()

print("\nList 2")
ilist2.print_list()

lst = intersection(ilist1, ilist2)

print("\nIntersection of list 1 and 2")
lst.print_list()