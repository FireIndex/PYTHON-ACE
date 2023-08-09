from Node import DoubleNode as Node

class DoubleLinkList:
    def __init__(self):
        self.head_node = None
        
    def get_head(self):
        return self.head_node
    
    def is_empty(self):
        return self.get_head() is None
    
    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        
        cur_node = self.head_node
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next_element
            
        print('None')
        return True
    
    def length(self):
        if self.is_empty():
            print("List is Empty")
            return 0
        
        count = 0
        cur_node = self.head_node
        while cur_node:
            count += 1
            cur_node = cur_node.next_element
            
        return count
        
    '''Insertion'''
    def insert_at_head(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head_node = new_node
            return self.head_node

        new_node.next_element = self.head_node
        self.head_node.previous_element = new_node
        self.head_node = new_node
        return self.head_node
            
    '''Deletion'''
    def delete(self, data):
        if self.is_empty():
            print("List is Empty")
            return False
        
        cur_node = self.get_head()
        if cur_node.data is data:
            self.head_node = cur_node.next_element
            if cur_node.next_element != None and cur_node.next_element.previous_element != None:
                cur_node.next_element.previous_element = None # set prev of head_node = None
                print(str(cur_node.data) + " Deleted!")
            
            return True
        
        while cur_node:
            if data is cur_node.data:
                if cur_node.next_element:
                    prev_node = cur_node.previous_element
                    next_node = cur_node.next_element
                    
                    prev_node.next_element = next_node
                    next_node.previous_element = prev_node
            
                else:
                    cur_node.previous_element.next_element = None
                
                print(str(data) + " Deleted!")
                return True
            
            cur_node = cur_node.next_element
        
        print(str(data) + " is not in the List!")
        return False

if __name__ == '__main__':
    list = DoubleLinkList()
    
    list.print_list()
    print(list.get_head())
    
    list.insert_at_head(1)
    list.insert_at_head(2)
    list.insert_at_head(3)
    list.print_list()
    
    print("length:", list.length())
    list.delete(2)
    list.print_list()