ORG = [1, 3, 5, 'seven']
print(f"Orignal List:\n {ORG}\n")

temp = [*ORG]
temp.append(9) # It works in O(1) time. It will always append at the end.
print(f"Append 9:\n {ORG} -> {temp}\n")

temp = [*ORG]
temp.insert(0, 0) # It works in O(n) time. If the index does not exist it will insert at the end.
print(f"Insert 0 at 0 index:\n {ORG} -> {temp}\n")

temp = [*ORG]
temp.remove("seven")
print(f"Remove 'seven':\n {ORG} -> {temp}\n")

# temp = [*ORG]
# temp.remove("0") # It works in O(n) time. If the element does not exist it will throw an error.
# prinft("Remove '0':\n {ORG} -> {temp}\n")

temp = [*ORG]
temp.pop(2) # It works in O(1) time. If the index does not exist it will throw an error.
print(f"Pop 2 index:\n {ORG} -> {temp}\n")

temp = [*ORG]
temp.reverse() # It works in O(n) time. It will reverse the list.
print(f"Reverse:\n {ORG} -> {temp}\n")


temp = list(range(10)) # It works in O(n) time. It will create a list of range.
print(f"slice range [0:4]:\n {temp} -> {temp[0:4]}\n")

temp = list(range(10))
temp[1:4] = [45, 21, 83]
print(f"initalise range [1:4]:\n {list(range(10))} -> {temp}\n")

temp = list(range(10))
del temp[::2]
print(f"del range [::2]:\n {list(range(10))} -> {temp[0:4]}\n")