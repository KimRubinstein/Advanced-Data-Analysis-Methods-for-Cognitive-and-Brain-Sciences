
# A function is a block of code that can be executed multiple times with different inputs. 
# By using functions, you can break down a complex problem into smaller, more manageable parts.

# We will use self-made functions in cases when we will want to use the same calculation multiple times,
# when only the arguments will change. We will only need to write the function once, and then we will be 
# able to use the functions many times as we wish.

# Few rules to follow when writing a function:
# (1) Every function will be responsible for one (and only) calculation,
#     if there is more than one calculation needed to be done - seperate the calculations into
#     few functions and add an top-level function that will call them.
# (2) The shorther the better! ~10 lines should be enough to keep the first rule
# (3) Try to have no more than 4 arguments
# (4) Avoid code duplication
# (5) Use descriptive names 
# (6) Include a docstring (a short description of the function)


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
x = greet("John") # what will x contain?

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

# In this example, we define a function find_minimum that takes a list of numbers as an argument and returns the minimum value in the list. 
# The function uses a loop to iterate through the list of numbers and updates the variable min_value if a smaller number is found. 
# The final value of min_value is returned from the function.

# %%
nums = [5, 10, 3, 8, 15]
print(find_minimum(nums)) 


# %%
def min_max(numbers):
    return (min(numbers), max(numbers))

# In this example, we define a function min_max that takes a list of numbers as an argument and returns the minimum and the maximum value in the list. 
# The final value of min_max is returned from the function.

# %%
nums = [5, 10, 3, 8, 15]
print(min_max(nums)) 

# %%
# what will happen if we'll insert the function into object?
min_max_object = (min_max(nums))
# we will get a tuple of the two returned objects

# %%
def sum_of_squares(numbers):
    """Return the sum of the squares of the numbers in a list.
    """
    total = 0
    for number in numbers:
        total += number * number
    return total



# %%
numbers = [1, 2, 3, 4, 5]
result = sum_of_squares(numbers)
print(result)

# In this example, the sum_of_squares function takes a list of numbers as an argument and calculates the sum of their squares. 
# The result is returned from the function and stored in the variable result.


# --------------------------------------------------------------------------------------------------
# EXTRA: Python Global Keyword
# https://www.programiz.com/python-programming/global-keyword

