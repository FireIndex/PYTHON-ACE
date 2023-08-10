# 04 - C Implement a Queue Using Stacks.py

from _Stack import MyStack

class NewQueue:  

  # Can use size from argument to create stack   
  def __init__(self):
    self.main_stack = MyStack()
    
	# Inserts Element in the Queue
  def enqueue(self,value):
    # Push the value into main_stack in O(1)
    self.main_stack.push(value)
    print (str(value) + " enqueued")
  # time complexity: O(1)
  
	# Removes Element From Queue  
  def dequeue(self):
    self.new_stack = MyStack()
    
    while not self.main_stack.is_empty():
        self.new_stack.push(self.main_stack.pop())
    
    pop = self.new_stack.pop() # store in reverse order
    print(str(pop) + " dequeued")

    while not self.new_stack.is_empty():
        self.main_stack.push(self.new_stack.pop())

    return pop
  
  # time complexity: O(n)

if __name__ == "__main__" :
  queue = NewQueue()
  for i in range(5):
    queue.enqueue(i+1)
  print("----------")
  for i in range(5):
    queue.dequeue()
    