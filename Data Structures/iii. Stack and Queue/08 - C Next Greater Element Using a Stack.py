# 08 - C Next Greater Element Using a Stack.py

def next_greater_elements(arr):
    result = [-1] * len(arr)
    stack = []

    for i, num in enumerate(arr):
        while stack and num > arr[stack[-1]]:
            result[stack.pop()] = num
        stack.append(i)

    return result

if __name__ == '__main__':
    # Test the function
    input_array = [4, 5, 2, 10, 8]
    output = next_greater_elements(input_array)
    print("Input array:", input_array)
    print("Next Greater Elements:", output)
