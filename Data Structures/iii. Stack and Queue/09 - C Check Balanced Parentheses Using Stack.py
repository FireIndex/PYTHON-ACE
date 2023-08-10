
from _Stack import MyStack

def is_balanced(exp):
    stack = MyStack()
    
    open_bracket = "{[("
    close_bracket = "}])"
    
    for e in exp:
        if e in open_bracket:
            stack.push(e)
        else:
            if stack.is_empty(): # if stack is empty but there is close bracket "]"
                return False
            
            pop = stack.pop()
            if open_bracket.index(pop) != close_bracket.index(e):
                return False

    if stack.is_empty():
        return True
    else:
        return False
    
    # time complexity is O(n)

if __name__ == "__main__":
    # print(is_balanced("{[()]}"))
    
    _string = "{[()]}"
    print(f"{_string}: {is_balanced(_string)}")
    
    _string = "{[([({))]}}"
    print(f"{_string}: {is_balanced(_string)}")
    
    _string = "\"\""
    print(f"{_string}: {is_balanced(_string)}")