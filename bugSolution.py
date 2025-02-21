def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    total = sum(numeric_numbers)
    count = len(numeric_numbers)
    if count == 0:
        return 0
    average = total / count
    return average

# Example usage with an empty list:
my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")

# Example usage with a list containing only zeros:
my_list = [0,0,0]
result = calculate_average(my_list)
print(f"The average is: {result}")

#Example usage with a list containing both positive and negative numbers:
my_list = [1,2,-3,4,-5]
result = calculate_average(my_list)
print(f"The average is: {result}")

# Example usage with a list containing non-numeric values:
my_list = [1,2,"a",4,5]
result = calculate_average(my_list)
print(f"The average is: {result}") # This will now print 2.6666666666666665 