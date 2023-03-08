
# A function is a block of code that can be executed multiple times with different inputs.
# By using functions, you can break down a complex problem into smaller, more manageable parts.

# We will use self-made functions in cases when we will want to use the same calculation multiple times,
# when only the arguments will change. We will only need to write the function once, and then we will be
# able to use the functions many times as we wish.

# Few rules to follow when writing a function:
# (1) Every function will be responsible for one (and only) calculation,
#     if there is more than one calculation needed to be done - seperate the calculations into
#     few functions and add an top-level function that will call them.
# (2) The shorther the better! ~10 lines should be enough to keep to the first rule
# (3) Avoid code duplication
# (4) Use descriptive names
# (5) Include a docstring (a short description of the function)


# %%
def greet(name):
    """Print a personalized greeting.
        args:
            name (str): The name of the person to greet.
    """
    print("Hello, " + name + "!")

# In this example, we define a function called greet that takes one argument, name, and uses it to generate a personalized greeting.
# To call the function, simply write the name of the function followed by the arguments in parentheses.

# %%
greet("John")

# %%
def find_minimum(numbers):
    """ Return the minimum value in a list of numbers.

    args:
        numbers (list): A list of numbers.
    """
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
    """Return the sum of the squares of the numbers in a list.
        
    """
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


