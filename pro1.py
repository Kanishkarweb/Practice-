def filter_numbers(numbers, condition):
    # Define a lambda function inside the outer function for filtering
    filtered_list = list(filter(lambda x: condition(x), numbers))
    
    return filtered_list

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers using the lambda function
filtered_even = filter_numbers(numbers, lambda x: x % 2 == 0)
print("Even numbers:", filtered_even)

# Filter numbers greater than 5 using the lambda function
filtered_greater_than_5 = filter_numbers(numbers, lambda x: x > 5)
print("Numbers greater than 5:", filtered_greater_than_5)
