import array

# type: 'u' (Py_UNICODE), initializer list: [1, 2, 3]

# type: 'h' (signed short), initializer list: [1, 2, 3]
# type: 'H' (unsigned short), initializer list: [1, 2, 3]

# type: 'l' (long), initializer list: [1, 2, 3]
# type: 'L' (unsigned long), initializer list: [1, 2, 3]
# type: 'q' (signed long long), initializer list: [1, 2, 3]
# type: 'Q' (unsigned long long), initializer list: [1, 2, 3]

# type: 'c' (char), initializer list: ['a', 'b', 'c']
# type: 'b' (signed char), initializer list: [1, 2, 3]
# type: 'B' (unsigned char), initializer list: [1, 2, 3]

# type: 'i' (int), initializer list: [1, 2, 3]
# type: 'I' (unsigned int), initializer list: [1, 2, 3]
# type: 'f' (float), initializer list: [1, 2, 3]
# type: 'd' (double), initializer list: [1.1, 2.2, 3.3]

new_array = array.array('f', [1, 2, 3])
print(f"first element of float array:\n {new_array} -> {new_array[0]}\n")


initializer_list = [2, 5, 43, 5, 10, 52, 29, 5]
number_array = array.array('i', initializer_list)
print(f"initializer list:\n {number_array}")
print(
    f" 2nd to 5th:\n\t {number_array[1:5]}\n",
    f"Beginning to 3rd:\n\t {number_array[:-5]}\n",
    f"6th to end:\n\t {number_array[5:]}\n",
    f"Beginning to end:\n\t {number_array[:]}\n",
)

# append, extend, insert, remove, pop, del are same as list