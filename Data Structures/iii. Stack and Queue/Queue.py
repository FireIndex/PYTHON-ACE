from DoublyLinkedList import DoublyLinkedList

# With typical arrays, however, the time complexity is O(n) when dequeuing an element from the beginning of the queue. This is because when an element is removed, the addresses of all the subsequent elements must be shifted by 1, which makes it less efficient. With linked lists and doubly linked lists, the operations become faster.


class MyQueue:
    def __init__(self):
        self.items = DoublyLinkedList()

    def is_empty(self):
        return self.items.length == 0

    def front(self):
        if self.is_empty():
            return None
        return self.items.get_head()

    def rear(self):
        if self.is_empty():
            return None
        return self.items.tail_node()

    def size(self):
        return self.items.length
    
    def enqueue(self, value):
        return self.items.insert_tail(value)

    def dequeue(self):
        return self.items.remove_head()

    def display(self):
        return self.items.__str__()

if __name__ == "__main__" :
    queue_obj = MyQueue()
    print("queue.enqueue(2);")
    queue_obj.enqueue(2)
    print("queue.enqueue(4);")
    queue_obj.enqueue(4)
    print("queue.enqueue(6);")
    queue_obj.enqueue(6)
    print("queue.enqueue(8);")
    queue_obj.enqueue(8)
    print("queue.enqueue(10);")
    queue_obj.enqueue(10)
    
    queue_obj.display()
    
    print("is_empty(): " + str(queue_obj.is_empty()))
    print("front(): " + str(queue_obj.front()))
    print("rear(): " + str(queue_obj.rear()))
    print("size(): " + str(queue_obj.size()))
    print("Dequeue(): " + str(queue_obj.dequeue()))
    print("Dequeue(): " + str(queue_obj.dequeue()))
    print("queue.enqueue(12);")
    queue_obj.enqueue(12)
    print("queue.enqueue(14);")
    queue_obj.enqueue(14)

    while queue_obj.is_empty() is False:
        print("Dequeue(): " + str(queue_obj.dequeue()))

    print("is_empty(): " + str(queue_obj.is_empty()))
