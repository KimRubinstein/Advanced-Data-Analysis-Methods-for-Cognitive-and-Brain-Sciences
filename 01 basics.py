# Anything after a "#" symbol is ignored by Python, so we can (and should!) use it to write comments

# %%
3 + 4 # execute a line with Ctrl + Enter
# Results of any command will appear in the "Cell Output" below

# %%
# ASSIGN a value to an object with =
# (it will now appear under "VARIABLES" section)
a = 3

# %%
# Running code with only the name of an object results in "printing" its contents:
a

# %%
# You can use the object just as you would its value:
a + 4
# Note that the value of "a" is not changed, 
# and that the results were not saved anywhere

# %%
b = 4

# %%
a + b

# %%
a * b

# %%
a = 8

# %%
c = a + b

# %%
c = a * b

# %%
c = b - a

# %%
c = B - A # Your first ERROR. Why?

# %%
c = a + b # assign without print
c          # then print


# %%
# Mutable vs. Immutable variables
a = [5]

# %%
b = a

# %%
a[0] =7 #what will happen now?

# %%
b

# %%
a = [2] # what will happen now?

 # %%
b

 # %%
# The variables we created above were all type "int".
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
type(a)

# Let's look at other types of variables that we can use when writing a code.

# %%
# Strings:

# A string is a sequence of characters (Python does not have a character data type, 
# a single character is simply a string with a length of 1)

string = "sequence of characters (letters/ numbers/ symbols)"

Group1 = "77"

Group2 = "experimental"

# %%
Group1 / a

# %%
# add exmaple: adding strings to each other


# %%
# Floats:
# used for defining decimal values
a = 3.1

# %%
d = c - a

# %%
# another example is needed here

# %%
# Logical:
# TRUE/FALSE object
a > b

# %%
a = 7

# %%
a == 7

# %%
a = a == 7

# %%
a != 7

# %%
a < 10 & b > 8

# %%
a < 10 | b > 8

# %%
# "isinstance" functions

# %%
# type a == type b (example)

# %%
# add example how to change the type of object

# %%
# Operators:

# (+)   addition  
# (-)   subtraction  
# (*)   multiplication  
# (/)   division  
# (^)   power  
# (%%)  modulo. The remainder after division. E.g., 5 %% 2  gives  1  
# (%/%) integer division. E.g., 7 %/% 3  gives  2

# %%
a + b / 2

# %%
a + (b / 2)

# %%
(a + b) / 2


# %%
# Lists & Dictionary & Tuple


