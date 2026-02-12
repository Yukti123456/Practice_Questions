#Q1-Create a lambda to square a number and apply it to a list [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5]

# Lambda function to square a number
square = lambda x: x * x

# Apply lambda to list
squared_numbers = list(map(square, numbers))

print(squared_numbers)
