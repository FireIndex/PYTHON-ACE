# 10 - C min() Function Using a Stack.py

# Create Stack => stack = myStack(5); where 5 is size of stack
# Create Queue => queue = myQueue(5); where 5 is size of queue
# Stack Functions => isEmpty(), isFull(), top()
# Queue Functions => enqueue(int),dequeue(),isEmpty(),getSize()
from _Stack import MyStack

class MinStack:
    # Constructor
    def __init__(self):
        self.main_stack = MyStack()
        self.min_stack = MyStack()
        
    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()
    
    # Pushes value into new stack
    def push(self, value):
        self.main_stack.push(value)
        if self.min_stack.is_empty() or self.min_stack.peek() > value:
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.peek())
            
    # Returns minimum value from new stack in constant time
    def min(self):
        if self.min_stack.is_empty():
            return None
        return self.min_stack.peek()
    
    # Time Complaxity: O(1)
    
if __name__ == "__main__":
    stack = MinStack()
    stack.push(5)
    stack.push(0)
    stack.push(2)
    stack.push(4)
    stack.push(1)
    stack.push(3)
    stack.push(0)
    print("Main stack:", stack.main_stack.stack_list)
    print("Min stack:", stack.min_stack.stack_list)
    print("Minimum value: " + str(stack.min()))
    stack.pop()
    stack.push(-2)
    print("Main stack:", stack.main_stack.stack_list)
    print("Min stack:", stack.min_stack.stack_list)
    print("Minimum value: " + str(stack.min()))
    stack.pop()
    print("Main stack:", stack.main_stack.stack_list)
    print("Min stack:", stack.min_stack.stack_list)
    print("Minimum value: " + str(stack.min()))
