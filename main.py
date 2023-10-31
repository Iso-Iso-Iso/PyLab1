from random import randint
# Random fill
def fill_array_by_random(size):
    return [randint(1, 9) for _ in range(size)]
# Sum up 2 arrays
def sum_up_arrays(first_array, second_array):
    max_length = max(len(first_array), len(second_array))
    res = []
    rest = 0

    for i in range(max_length):
        # Get digits from arrays
        first_digit = first_array[-i - 1] if i < len(first_array) else 0
        second_digit = second_array[-i - 1] if i < len(second_array) else 0
        # Get total sum of 2 numbers
        total = first_digit + second_digit + rest
        # Save rest if total > 10
        rest = total // 10
        # Save array value without rest
        res.insert(0, total % 10)

    while len(first_array) < len(second_array):
        first_array.insert(0, 0)
    
    while len(second_array) < len(first_array):
        second_array.insert(0, 0)

    if rest > 0:
        res.insert(0, rest)

    return res

# Get arrays length
first_arr_length = int(input("Enter length of first array: "))

second_arr_length = int(input("Enter length of second array: "))
# Fill array by random
first_array = fill_array_by_random(first_arr_length)

second_array = fill_array_by_random(second_arr_length)
# Sum up arrays
computed = sum_up_arrays(first_array, second_array)
# Print result
print(f"First array is: {first_array}")
print(f"Second array is: {second_array}")
print(f"Result: {computed}")