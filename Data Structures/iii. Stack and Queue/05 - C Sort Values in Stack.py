# 05 - C Sort Values in Stack.py

# Using built in sort method for Python lists

from Stack import MyStack

def sort_stack(stack):
  stack.stack_list.sort(reverse=True)
  return stack
# time complexity: O(nlogn)

if __name__ == "__main__" :
    # Creating and populating the stack
    stack = MyStack()
    stack.push(2)
    stack.push(97)
    stack.push(4)
    stack.push(42)
    stack.push(12)
    stack.push(60)
    stack.push(23)
    # Sorting the stack
    stack = sort_stack(stack)
    # Printing the sorted stack
    print("Stack after sorting")
    print([stack.pop() for i in range(stack.size())])
