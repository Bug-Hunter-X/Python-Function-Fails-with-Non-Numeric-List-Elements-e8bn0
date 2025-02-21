def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  # Handle empty list
    average = total / count
    return average

# Example usage with an empty list:
my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}") #This will print 0, as expected

# Example usage with a list containing only zeros:
my_list = [0,0,0]
result = calculate_average(my_list)
print(f"The average is: {result}") #This will print 0, as expected

#Example usage with a list containing both positive and negative numbers:
my_list = [1,2,-3,4,-5]
result = calculate_average(my_list)
print(f"The average is: {result}") #This will print -0.2, as expected

# Example usage with a list containing non-numeric values:
my_list = [1,2,"a",4,5]
result = calculate_average(my_list)
print(f"The average is: {result}") #This will raise a TypeError exception because of the string value "a"