from _Node import Node

class LinkedList:
    def __init__(self):
        self.head_node = None # Pointer to first node
       
    def get_head(self):
        return self.head_node
    # Time complexity: O(1)
    
    def is_empty(self):
        if self.head_node == None:
            return True
        else:
            return False
    # Time complexity: O(1)
    
    def length(self):
        if self.is_empty():
            print("List is Empty")
            return 0
        
        count = 0
        cur_node = self.head_node
        while cur_node:
            count+=1
            cur_node = cur_node.next_element
        
        return count
    # Time complexity: O(1)
    
    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True


    '''Insertion'''
    #  insert at the head
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next_element = self.head_node # Link new node to head's next node
        self.head_node = new_node # Make new node as head
        return self.head_node
    # Time complexity: O(1)
    
    # Insertion at the k Position
    def insert_at_position(self, k, data):
        new_node = Node(data)
        
        if self.head_node is None: # If list is empty then make the new node as head
            self.head_node = new_node
            return
        
        temp = self.head_node
        while temp.next_element and k > 1: # Traverse to the (k-1)th node
            temp = temp.next_element
            k -= 1
            
        new_node.next_element = temp.next_element # Link the new node to the (k+1)th node
        temp.next_element = new_node # Link the (k-1)th node to the new node
        return
    
    #  insert at the tail
    def insert_at_tail(self, data):
        new_node = Node(data)
        
        if self.head_node is None: # If list is empty then make the new node as head
            self.head_node = new_node
            return

        temp = self.head_node
        while temp.next_element: # Traverse to the last node
            temp = temp.next_element
        
        temp.next_element = new_node # Link the new node after the last node
        return
    # Time complexity: O(n)
        

    '''Deletion'''
    #  Deletion at the head
    def delete_at_head(self):
        if self.is_empty():
            print("List is Empty")
            return False
        
        first = self.head_node
        self.head_node = first.next_element
        del first
        return True
    # Time complexity: O(1)
    
    # Deletion by value
    def delete(self, data):
        if self.is_empty():
            print("List is Empty")
            return False
        
        cur_node = self.head_node
        
        # if head
        if cur_node.data == data:
            self.head_node = cur_node.next_element # (None)
            del cur_node
            return True
        
        prv_node = None
        while cur_node:
            if cur_node.data == data:
                prv_node.next_element = cur_node.next_element
                del cur_node
                return True
            
            prv_node = cur_node
            cur_node = cur_node.next_element
        
        return False
    # Time complexity: O(n)

    #  Deletion at the tail
    def delete_at_tail(self):
        if self.is_empty():
            print("List is Empty")
            return False
        
        if not self.head_node.next_element:
            del self.head_node.next_element
            self.head_node = None
            return True
        
        current = self.head_node
        prev = None
        while current.next_element:
            prev = current
            current = current.next_element
        prev.next_element = None
        del current  # Remove the deleted node from memory
 
        return True
    # Time complexity: O(1)


    '''Checking'''
    def search(self, data):
        if self.is_empty():
            print("List is Empty")
            return False
        
        cur_node = self.head_node
        while cur_node:
            if cur_node.data == data:
                return True
            cur_node = cur_node.next_element

        return False
    # Time complexity: O(n) & Space complexity: O(1)

    def recursive_search(self, node, value):
        # Base case
        if not node:
            return False
        if node.data is value:
            return True
        
        return self.search(node.next_element, value)
    # Time complexity: O(n) & Space complexity: O(n) 
        
    def remove_duplicates(self):
        if self.is_empty():
            return

        # If list only has one node, leave it unchanged
        if self.get_head().next_element is None:
            return

        outer_node = self.get_head()
        while outer_node:
            inner_node = outer_node  # Iterator for the inner loop
            
            while inner_node:
                if inner_node.next_element:
                    if outer_node.data == inner_node.next_element.data:
                        # Duplicate found, so now removing it
                        new_next = inner_node.next_element.next_element
                        inner_node.next_element = new_next
                    else:
                        # Otherwise simply iterate ahead
                        inner_node = inner_node.next_element
                else:
                    # Otherwise simply iterate ahead
                    inner_node = inner_node.next_element
            outer_node = outer_node.next_element
        return
    # Time complexity: O(n^2) & Space complexity: O(1) 

    

if __name__ == '__main__':
    list = LinkedList() # Initialize a linked list

    print(list.get_head()) # Returns None
    print(list.is_empty()) # Returns True
    list.print_list()

    print("Inserting values in list")
    
    # for i in range(1, 10):
    #     list.insert_at_head(i) # Insert values at head
    
    # for i in range(1, 10):
    #     list.insert_at_tail(i) # Insert values at tail
    list.insert_at_tail(6) # Insert values at tail
        
    # list.insert_at_position(5, 110) # Insert value at position 5
    list.print_list()
    
    # print(list.delete_at_head())
    # print(list.delete(2))
    print(list.delete_at_tail())
    list.print_list()
    
    print(list.search(6))
    print(list.search(60))
    print(list.length())
