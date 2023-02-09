
# A function is a block of code that can be executed multiple times with different inputs. 
# By using functions, you can break down a complex problem into smaller, more manageable parts.

# %%
def greet(name):
    print("Hello, " + name + "!")

# In this example, we define a function called greet that takes one argument, name, and uses it to generate a personalized greeting. 
# To call the function, simply write the name of the function followed by the arguments in parentheses.

# %%
greet("John")

# %%
def find_minimum(numbers):
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

# In this example, we define a function find_minimum that takes a list of numbers as an argument and returns the minimum value in the list. The function uses a loop to iterate through the list of numbers and updates the variable min_value if a smaller number is found. 
# The final value of min_value is returned from the function.

# %%
numbers = [5, 2, 1, 9, 8, 3]
result = find_minimum(numbers)
print(result)

# %%
def sum_of_squares(numbers):
    total = 0
    for number in numbers:
        total += number * number
    return total

# In this example, the sum_of_squares function takes a list of numbers as an argument and calculates the sum of their squares. 
# The result is returned from the function and stored in the variable result.

# %%
numbers = [1, 2, 3, 4, 5]
result = sum_of_squares(numbers)
print(result)


