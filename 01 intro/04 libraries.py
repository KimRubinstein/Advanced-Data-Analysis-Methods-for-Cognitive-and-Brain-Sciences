
# %%
# Modules, Packages, Libraries and Frameworks - what’s the difference between them? 

# text below was based (and sometimes quote) from: https://learnpython.com/blog/python-modules-packages-libraries-frameworks/

# (1) A module is basically a bunch of related code saved in a file with the extension ".py". 
# You may choose to define functions, classes, or variables in a module. It’s also fine to include runnable code in modules.

# (2) Python packages are basically a directory of a collection of modules. 
# Packages allow the hierarchical structure of the module namespace. 
# Just like we organize our files on a hard drive into folders and sub-folders, we can organize our modules into packages and subpackages.

# We can import specific modules from this package using the dot notation. 
# For example, to import a dataset module from the a package, we can use one of the following code snippets:

# "import my_package.module1" -OR- "from my_package import module1"

# we may choose to import only one function from our module. Either of the following options will do the job:

# import my_package.module1.function1() -OR- from "my_model.module1 import function1()"

# There are a lot of built-in and open-source Python packages, we will learn about some of them later on.
# For example, two packages that we'll learn about in this class are 
# NumPy, which is the fundamental Python package for scientific computing
# and Pandas, which is a Python package for fast and efficient processing of tabular data, time series, matrix data, etc.

# (3) A library is an umbrella term referring to a reusable chunk of code.
# Usually, a Python library contains a collection of related modules and packages. 
# Actually, this term is often used interchangeably with “Python package” because packages can also contain modules and other packages 
# (subpackages). However, it is often assumed that while a package is a collection of modules, a library is a collection of packages.

# NumPy and pandas packages that were mentioned before are also often referred to as libraries. 
# That is because these are complex packages that have wide applications (i.e. scientific computing and data manipulation, respectively). 
# They also include multiple subpackages and so basically satisfy the definition of a Python library. 
# This is quite confuising, I know...

# (4) Last (but not least), Python frameworks. 
# Similar to libraries, Python frameworks are a collection of modules and packages that help programmers to fast track the 
# development process. However, frameworks are usually more complex than libraries. Also, while libraries contain packages that 
# perform specific operations, frameworks contain the basic flow and architecture of the application.

# %%
# There are two type of modules, built-in modules and external modules.
# The main difference between them is that built-in modules are part of the Python standard library and are 
# included in every Python installation. External modules, on the other hand, need to be installed separately.

# For example, the math module is a built-in module in the Python 3 standard library that provides mathematical functions such as 
# trigonometry, logarithms, and square roots. You don't need to install anything to use the math module,
# it is already included with Python. To use the math module, you simply need to import it into your Python script

# %%
import math # import the whole module
b = 4
print(math.sqrt(b))

# %%
from math import sqrt, sin # importing only specific functions

print(sqrt(b))
print(sin(b))

# %%
# NumPy

# The name “Numpy” stands for “Numerical Python”. It is the commonly used package (or you can also call it a library). 
# It is a popular machine learning package that supports large matrices and multi-dimensional data. 
# It consists of built-in mathematical functions for easy computations. Even libraries like TensorFlow use Numpy internally to perform
# several operations on tensors. Array Interface is one of the key features of this library.  

# (origin: https://www.geeksforgeeks.org/libraries-in-python/)

# In contrast to "math" module, the NumPy package is external and needs to be installed before you can use it. 
# NumPy provides advanced mathematical functionality and support for arrays, which are not part of the built-in Python libraries. 

# To install NumPy (and other external libraries/packages), you can use the pip package manager "pip install numpy" in the Terminal.

# BUTTTTTT, you should not ever do that. why?

# Each version of Python (or external packages/libraries) could react differently to the same code. 
# Moreover, there might be some functions that won’t be available after updating your Python version. 
# To keep your code safe and to make sure it will be able to run, you can download packages using conda. 
# This means that you create an environment that will be used with a specific version of Python and 
# a specific version of your packages which you can always come back and use. 
# This is useful for managing dependencies and ensuring that your code runs on different machines without version conflicts. 

# If conda is not installed, you can download and install it from the Anaconda website
# https://www.anaconda.com/products/distribution

# %%
# You can create an environment using "conda create" command in the Terminal (Terminal > New Terminal)
# "conda create --name labs2023"

# Once an environment is created, you can activate it using the "conda activate" command. 
# "conda activate labs2023"

# After finishing, you can deactivate it using the "conda deactivate" command. 
# "conda deactivate"

# You can also list all available environments using the "conda info --envs" command.

# after actiavting the relevant environment, we should install our packages/libraries using "conda install *package_name*".

# You can update packages in an environment using the "conda update" command. 

# For example, if you want to update the package "numpy" to the latest version in your "labs2023" environment, 
# you can run the command conda activate labs2023 && conda update numpy. 
# This will activate the "labs2023" environment and update the "numpy" package. 
# You can also specify a specific version of a package to update to by running the command "conda update package_name=version_number".

# After creating your environment, and installing the packages/libraries you need to run your code,
# you should make sure that you chose the right Interpreter
# (Select + Shift + P) > Python: Select Intertperter

# NumPy examples presented below are based on w3schools NumPy Tutorial: https://www.w3schools.com/python/numpy/default.asp

# %%
# "conda activate labs2023"
# "conda install numpy"
import numpy as np

# %%
# A vector is a single one-dimension array of lists and behaves same as a Python list.
# Numpy provides numpy.array() method which creates a one dimensional array (vector) which can be horizontal or vertical.

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
print(arr.shape)

# %%
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# These are the most common and basic arrays.
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.shape)

# %%
# An array that has 1-D arrays as its elements is called a 2-D array.
# These are often used to represent matrix or 2nd order tensors.
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.shape)

# %%
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim,a.shape)
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
x = np.random.choice([3, 5, 7, 9], size=(3, 5)) # generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9)

print(x)
print(x)

# %%
# Using the choice() method we can also generate random numbers based on defined probabilities.

x = np.random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
# The probability for the value to be 3 is set to be 0.1
# The probability for the value to be 5 is set to be 0.3
# The probability for the value to be 7 is set to be 0.6
# The probability for the value to be 9 is set to be 0

print(x)

# %%
# NumPy ufuncs (universal functions) operate on the ndarray object.
# ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
# They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y) # sums the content of two lists, and return the results in a new array

print(z)

# %%
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr1 = np.add(arr1, arr2)  # sums the content of two arrays, and return the results in a new array
newarr2 = np.subtract(arr1, arr2) # subtract the values in arr2 from the values in arr1
newarr3 = np.multiply(arr1, arr2) # multiply the values in arr1 with the values in arr2
newarr4 = np.divide(arr1, arr2) # divide the values in arr1 with the values in arr2
newarr5 = np.power(arr1, arr2) # raise the valules in arr1 to the power of values in arr2

print(newarr1)
print(newarr2)
print(newarr3)
print(newarr4)
print(newarr5)

# which is the same as using +, -, *, /, **

# examples of sum, mean, total average, row avg, col avg 
# reshaping, transpose, extension, flatting, squizzing, npstack
# https://www.analyticsvidhya.com/blog/2020/04/the-ultimate-numpy-tutorial-for-data-science-beginners/



# %%
# Pandas

# Pandas are an important library for data scientists. It is an open-source machine learning library that 
# provides flexible high-level data structures and a variety of analysis tools. It eases data analysis, 
# data manipulation, and cleaning of data. Pandas support operations like Sorting, Re-indexing, Iteration, 
# Concatenation, Conversion of data, Visualizations, Aggregations, etc.

# (source: https://www.geeksforgeeks.org/libraries-in-python/)

# Pandas examples presented below are based on w3schools Pandas Tutorial: https://www.w3schools.com/python/pandas/default.asp

# %%
# "conda activate labs2023"
# "conda install pandas"

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
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html add groupby

df1 = pd.DataFrame({'Animal': ['Falcon', 'Falcon','Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})
df1

# %%
df1.groupby(['Animal']).mean()

# %%
df1.groupby(['Animal']).sum()

# %%
df1.groupby(by=['Animal']).count()

# %%
df1.groupby('Animal')['Max Speed'].agg(['sum','count'])

# note that in all the outputs above we did not create a new data frame!

# %%
# data was taken from:
# https://github.com/rfordatascience/tidytuesday/blob/master/data/2021/2021-09-14/readme.md

audio_df = pd.read_csv('audio_features.csv')

# you can also write the whole path to a certain csv file as below (notice to add an "r" before!)
# df = pd.read_csv(r"C:\data_folder\data.csv")

print(audio_df) 

# %%
print(audio_df.head(10)) # print only the first 10 rows (default of .head() is 5)
print(audio_df.tail(7))  # print only the last 7 rows (default of .tail() is 5)

# %%
print(audio_df.info()) 

# we can see that there are 41,111 rows and 16 columns
# the "info" method show us the name of each column, with the data type
# the method also tells us how many Non-Null values are present in each column


# %%
new_df = audio_df.dropna() # creating new df with no empty cells (remove all rows that contain empty cells)
                     # note that by default, the dropna() method returns a new DataFrame, and will not change the original
                     # if you do want to change the original DataFrame, use the inplace = True argument


# %%
# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value

audio_df.fillna(130, inplace = True) # replace NULL values with the number 130


# %%
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column

x = audio_df["speechiness"].mean()
audio_df["speechiness"].fillna(x, inplace = True)

# In general, it is not a good idea to replace empty cells with a fixed value. We should either
# remove the entire row, or find mark the missing values as NaN and make sure the operations we perform on the data treat NaN values correctly.
# %%
audio_df.loudness.head()      # selecting an individual column
# df['loudness'].head() 

# %%
audio_df[['loudness']].head() # will return a dataframe containing only this column
# audio_df['loudness'].to_frame().head()

# %%
audio_df[['mode','energy']].tail() # selecting multiple specific columns

# %%
# selecting rows where a value matches a value
df_hits_only = audio_df[audio_df['target']==1]
df_hits_only.head()

# %%
# we can also select rows where values are less than a value
df_low_danceavility = audio_df[audio_df['danceability'] < 0.7]
df_low_danceavility.head()

# %%
df_danceability_6_7 = audio_df[ (audio_df['balance'] >= 0.6) and (audio_df['balance'] <= 0.7) ]
df_danceability_6_7.head()

# %%
audio_df.iloc[5:10] # returns rows 5 to 9 based on their index values

# %%
# Matplotlib

# This library is responsible for plotting numerical data. And that’s why it is used in data analysis. 
# It is also an open-source library and plots high-defined figures like pie charts, histograms, scatterplots, 
# graphs, etc.

# (source: https://www.geeksforgeeks.org/libraries-in-python/)

# "conda activate labs2023"
# "conda install matplotlib"
import matplotlib.pyplot as plt

# matplotlib cheat sheets and handouts: https://matplotlib.org/cheatsheets/

# Matplotlib examples presented below are based on w3schools Matplotlib Tutorial: https://www.w3schools.com/python/matplotlib_intro.asp


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
        marker = 'o',           #emphasize each point with a specified marker
        linestyle = 'dashed',   # change the style of the plotted line
        color = '#4CAF50',       # change the color of the line
        linewidth = '5.5'      # change the line width
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

plt.scatter(x, y) # creating scatter-plot
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

# "conda activate labs2023"
# "conda install seaborn"
import seaborn as sns


# %%
# Plotting a Distplot


sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

# %%
sns.distplot([0, 1, 2, 3, 4, 5], hist=False) # without histogram
plt.show()



# %%
sns.regplot(x='loudness', y='danceability', data=audio_df) # create a scatter plot with regression line
plt.show()

# %%
sns.boxplot(x='performer', y='loudness', data=audio_df, order=['Andy Williams','Britney Spears'])
plt.show()

# more examples here: https://seaborn.pydata.org/examples/index.html
# https://seaborn.pydata.org/examples/grouped_barplot.html