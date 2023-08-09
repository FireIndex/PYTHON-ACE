# 08 - C First Non-Repeating Integer in a List.py

def find_first_unique(lst):
    for i, x in enumerate(lst):
        flag = False
        for j, y in enumerate(lst):
            if i != j:
                if x == y:
                    flag = True
                    break
        if not flag:
            return x

print(find_first_unique([9,2,2,6,9,1,6]))