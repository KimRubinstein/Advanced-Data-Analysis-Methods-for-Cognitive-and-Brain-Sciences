# a Python library is a collection of related modules or codes.

# There are two type of libraries - built-in libraries and external libraries.
# The main difference between them is that built-in libraries are part of the Python standard library and are
# included in every Python installation. External libraries, on the other hand, need to be installed separately.

# For example, the math library is a built-in library in Python that provides mathematical functions such as trigonometry,
# logarithms, and square roots. You don't need to install anything to use the math library; it is already included with Python.
# To use the math library, you simply need to import it into your Python script

# %%
import math # import the whole library
b = 4
print(math.sqrt(b))

# %%
from math import sqrt, sin # importing only specific items

print(sqrt(b))
print(sin(b))

# %%
# NumPy

# The name “Numpy” stands for “Numerical Python”. It is the commonly used library. It is a popular machine
# learning library that supports large matrices and multi-dimensional data. It consists of built-in
# mathematical functions for easy computations. Array Interface is one of the key features of this library.
# (source: https://www.geeksforgeeks.org/libraries-in-python/)

# In contrast to "math" library, the NumPy library is an external library that needs to be installed before you can use it.
# NumPy provides advanced mathematical functionality and support for arrays, which are not part of the built-in Python libraries.
# To install NumPy, you can use the pip package manager "pip install numpy" in the Terminal

# NumPy examples presented below are based on w3schools NumPy Tutorial: https://www.w3schools.com/python/numpy/default.asp

# pip install numpy
import numpy as np

# %%
# check numpy version
# print(np.__version__)

# %%
# A vector is a single one-dimension array of lists and behaves same as a Python list.
# Numpy provides numpy.array() method which creates a one dimensional array (vector) which can be horizontal or vertical.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)


# %%
print(type(arr)) # what type is this object?

# ! Note it isn't a list!
# The array object in NumPy is called "ndarray"
# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray

# %%
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

arr = np.array(42)
print(arr)

# %%
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# These are the most common and basic arrays.

arr = np.array([1, 2, 3, 4, 5])
print(arr)

# %%
# An array that has 1-D arrays as its elements is called a 2-D array.
# These are often used to represent matrix or 2nd order tensors.

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# %%
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# %%
# Array indexing is the same as accessing an array element.
# You can access an array element by referring to its index number.
# The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

arr = np.array([1, 2, 3, 4])
print(arr[0])

# %%

arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3]) # what will be printed out here?

# %%
# To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
# Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])

# %%
# We can use slicing to take elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
    # If we don't pass start its considered 0
    # If we don't pass end its considered length of array in that dimension
    # If we don't pass step its considered 1

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])     # slice elements from index 1 to index 5
print(arr[4:])      # slice elements from index 4 to the end of the array
print(arr[-3:-1])   # slice from the index 3 from the end to index 1 from the end

# %%
# You can search an array for a certain value, and return the indexes that get a match. To search an array, use the where() method.

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

# %%

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0) # what will this do?
print(x)

# %%
# (Pseudo) random numbers in NumPy can be performed using "random" module

x = np.random.randint(100) # generate a random integer from 0 to 100
y = np.random.randint(100, size=(5)) # generate a 1-D array containing 5 random integers from 0 to 100
z = np.random.randint(100, size=(3, 5)) # generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100

print(x)
print(y)
print(z)

# %%
# The choice() method allows you to generate a random value based on an array of values, it takes an array as a parameter
# and randomly returns one of the values.

x = np.random.choice([3, 5, 7, 9]) # return one of the values in an array
y = np.random.choice([3, 5, 7, 9], size=(3, 5)) # generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9)
print(x)
print(y)


# %%
# Using the choice() method we can also generate random numbers based on defined probabilities.

x = np.random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
# The probability for the value to be 3 is set to be 0.1
# The probability for the value to be 5 is set to be 0.3
# The probability for the value to be 7 is set to be 0.6
# The probability for the value to be 9 is set to be 0

print(x)

# Consider adding operations that change the dimensions of the array (e.g. reshape, transpose, etc.)

# %%
# Pandas

# Pandas are an important library for data scientists. It is an open-source machine learning library that
# provides flexible high-level data structures and a variety of analysis tools. It eases data analysis,
# data manipulation, and cleaning of data. Pandas support operations like Sorting, Re-indexing, Iteration,
# Concatenation, Conversion of data, Visualizations, Aggregations, etc.

# (source: https://www.geeksforgeeks.org/libraries-in-python/)

# Pandas examples presented below are based on w3schools Pandas Tutorial: https://www.w3schools.com/python/pandas/default.asp

# pip install pandas
import pandas as pd

# %%
# A Pandas DataFrame is a 2 dimensional data structure, like a table with rows and columns

data = {
    "Name": ["John", "Jane", "Jim", "Joan"],
    "Age": [32, 28, 41, 35],
    "Country": ["USA", "UK", "Canada", "Australia"]
}

df = pd.DataFrame(data)
print(df)

# %%
# refer to the row index:
print(df.loc[0])

# %%
# use a list of indexes:
print(df.loc[[0, 1]])

# %%
import pandas as pd

data = {
    "Name": ["John", "Jane", "Jim", "Joan"],
    "Age": [32, 28, 41, 35],
    "Country": ["USA", "UK", "Canada", "Australia"]
}


df = pd.DataFrame(data, index = ["sub1", "sub2", "sub3", "sub4"])
print(df)

# %%
# refer to the named index:
print(df.loc["sub2"])

# %%
import pandas as pd

df = pd.read_csv('spotify_dataset.csv')

# you can also write the whole path to a certain csv file as below (notice to add an "r" before!)
# df = pd.read_csv(r"C:\data_folder\data.csv")

print(df)

# %%
print(df.head(10)) # print only the first 10 rows (default of .head() is 5)
print(df.tail(7))  # print only the last 7 rows (default of .tail() is 5)

# %%
print(df.info())

# we can see that there are 41,111 rows and 16 columns
# the "info" method show us the name of each column, with the data type
# the method also tells us how many Non-Null values are present in each column

# %%
new_df = df.dropna() # creating new df with no empty cells (remove all rows that contain empty cells)
                     # note that by default, the dropna() method returns a new DataFrame, and will not change the original
                     # if you do want to change the original DataFrame, use the inplace = True argument


# %%
# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value
import pandas as pd

df = pd.read_csv('spotify_dataset.csv')
df.fillna(130, inplace = True) # replace NULL values with the number 130

# In general, it is not a good idea to replace empty cells with a fixed value. We should either
# remove the entire row, or find mark the missing values as NaN and make sure the operations we perform on the data treat NaN values correctly.

# %%
df.loudness.head()      # selecting an individual column
# df['loudness'].head()

# %%
df[['loudness']].head() # will return a dataframe containing only this column
# df['marital'].to_frame().head()

# %%
df[['mode','energy']].tail() # selecting multiple specific columns

# %%
# selecting rows where a value matches a value
df_hits_only = df[df['target']==1]
df_hits_only.head()

# %%
# we can also select rows where values are less than a value
df_low_danceavility = df[df['danceability'] < 0.7]
df_low_danceavility.head()

# %%
df_danceability_6_7 = df[ (df['balance'] >= 0.6) & (df['balance'] <= 0.7) ]
df_danceability_6_7.head()

# %%
df.iloc[5:10] # returns rows 5 to 9 based on their index values

# ## Add: groupby

# %%
# Matplotlib

# This library is responsible for plotting numerical data. And that’s why it is used in data analysis.
# It is also an open-source library and plots high-defined figures like pie charts, histograms, scatterplots,
# graphs, etc.

# (source: https://www.geeksforgeeks.org/libraries-in-python/)

# pip install matplotlib
import matplotlib.pyplot as plt

# matplotlib cheat sheets and handouts: https://matplotlib.org/cheatsheets/

# Matplotlib examples presented below are based on w3schools Matplotlib Tutorial: https://www.w3schools.com/python/matplotlib_intro.asp


# %%
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints) # draw a line in a diagram from position (0,0) to position (6,250)
                           # by default, the plot() function draws a line from point to point
                           # note that if we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc.,
                           # depending on the length of the y-points.
plt.show()

# %%

plt.plot(xpoints, ypoints, 'o') # to plot only the markers, we can use shortcut string notation parameter 'o', which means 'rings'
plt.show()

# %%
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints) # we can plot as many points as we like, we just to make sure we have the same number of points in both axis
plt.show()

# %%

plt.plot(xpoints, ypoints,
        marker = 'o',           # emphasize each point with a specified marker
        linestyle = 'dashed',   # change the style of the plotted line
        color = '#4CAF50',      # change the color of the line
        linewidth = '5.5'       # change the line width
            )
plt.show()

# %%
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2) # adding more than one line
plt.show()

# %%
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Ice-Cream Data")
plt.xlabel("Average Ice-Cream Balls")
plt.ylabel("Calorie Burnage")

plt.show()

# %%
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y) # creating a scatter-plot
plt.show()

# %%
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y) # creating bar-plot
plt.show()

# %%
x = np.random.normal(170, 10, 250) # randomly generate an array with 250 values, where the values will concentrate around 170,
                                   # and the standard deviation is 10

plt.hist(x) # creating histogram
plt.show()

# %%
y = np.array([35, 25, 25, 15])

plt.pie(y) # creating pie-chart
plt.show()

# %%
# Seaborn

# Seaborn is a library for data visualization in Python. It is built on top of Matplotlib and provides a high-level interface
# for creating attractive and informative statistical graphics.

#pip install seaborn
import seaborn as sns


# %%
# Plotting a Distplot

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

# %%
sns.distplot([0, 1, 2, 3, 4, 5], hist=False) # without histogram
plt.show()


# To add - *handling several variables*, violin plots, etc.
