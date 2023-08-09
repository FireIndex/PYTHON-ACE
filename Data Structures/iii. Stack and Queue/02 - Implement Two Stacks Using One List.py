# 02 - Implement Two Stacks Using One List.py

class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.size = size
        self.stack = [None]*self.size
        self.first_empty_indx = 0
        self.last_empty_indx = size - 1
        
    def is_empty_space(self):
        return (self.first_empty_indx + (self.size - self.last_empty_indx)) <= self.size

    # Insert Value in First Stack
    def push1(self, value):
        if not self.is_empty_space():
            raise Exception("Stack is full")
        
        self.stack[self.first_empty_indx] = value
        self.first_empty_indx += 1

    # Insert Value in Second Stack
    def push2(self, value):
        if not self.is_empty_space():
            raise Exception("Stack is full")
        
        self.stack[self.last_empty_indx] = value
        self.last_empty_indx -= 1

    # Return and remove top Value from First Stack
    def pop1(self):
        pop = self.stack[self.first_empty_indx - 1]
        self.stack[self.first_empty_indx - 1] = None
        self.first_empty_indx -= 1
        return pop

    # Return and remove top Value from Second Stack
    def pop2(self):
        pop = self.stack[self.last_empty_indx + 1]
        self.stack[self.last_empty_indx + 1] = None
        self.last_empty_indx += 1
        return pop
    
    def p(self):
        print(self.first_empty_indx, self.last_empty_indx, "\n", self.stack, "\n")
    

if __name__ == "__main__" :
    st = TwoStacks(6)
    st.push1(1)
    st.push1(2)
    st.push1(3)

    st.push1(4)
    st.push1(5)
    st.push1(6)
    # st.push1(7)

    st.p()

    print(st.pop1())
    print(st.pop1())
    print(st.pop1())

    print(st.pop2())
    print(st.pop2())
    print(st.pop2())