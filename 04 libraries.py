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
# learning library that supports large matrices and multi-dimensional data. It consists of in-built
# mathematical functions for easy computations. Even libraries like TensorFlow use Numpy internally to perform
# several operations on tensors. Array Interface is one of the key features of this library.  

# (origin: https://www.geeksforgeeks.org/libraries-in-python/)

# In contrast to "math" library, the NumPy library is an external library that needs to be installed before you can use it. 
# NumPy provides advanced mathematical functionality and support for arrays, which are not part of the built-in Python libraries. 
# To install NumPy, you can use the pip package manager "pip install numpy" in the Terminal



# %%
# Pandas

# Pandas are an important library for data scientists. It is an open-source machine learning library that 
# provides flexible high-level data structures and a variety of analysis tools. It eases data analysis, 
# data manipulation, and cleaning of data. Pandas support operations like Sorting, Re-indexing, Iteration, 
# Concatenation, Conversion of data, Visualizations, Aggregations, etc.

# (origin: https://www.geeksforgeeks.org/libraries-in-python/)

# pip install pandas
import pandas as pd

# %%
data = {
    "Name": ["John", "Jane", "Jim", "Joan"],
    "Age": [32, 28, 41, 35],
    "Country": ["USA", "UK", "Canada", "Australia"]
}

df = pd.DataFrame(data)
print(df)

# %%
# Matplotlib

# This library is responsible for plotting numerical data. And that’s why it is used in data analysis. 
# It is also an open-source library and plots high-defined figures like pie charts, histograms, scatterplots, 
# graphs, etc.

# (origin: https://www.geeksforgeeks.org/libraries-in-python/)

import matplotlib.pyplot as plt


# %%
# Seaborn

# Seaborn is a library for data visualization in Python. It is built on top of Matplotlib and provides a high-level interface 
# for creating attractive and informative statistical graphics.

#!pip install seaborn
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
diamonds = sns.load_dataset("diamonds")
sns.scatterplot(x="carat", y="price", data=diamonds)
plt.show()
